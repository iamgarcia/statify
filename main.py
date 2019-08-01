# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import webapp2
import jinja2
import os
import spotipy
from spotipy import util
from spotipy import oauth2

def get_songs(token):
    songs = []
    sp = spotipy.Spotify(auth=token)
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='long_term')
    return top_tracks
    for item in top_tracks['items']:
        song_length = sp.track(item['uri'][-22:])['duration_ms']
        song_length = round(song_length/60000, 2)
        songs += [{'name': item['name'], 'artists': item['artists'][0]['name'], 'album_title': item['album']['name'], 'song_length': song_length}]
    return songs

def get_token(current_url):
    sp_oauth = oauth2.SpotifyOAuth('d1043c275ddc4f64a60b2438db8ef839', 'fe8389b1944e44199785a6607fc68da4', 'https://new-statify-app.appspot.com/profile', scope='user-top-read')
    code = sp_oauth.parse_response_code(current_url)
    access_token = sp_oauth.get_access_token(code)
    return access_token


# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# The handler section
class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/login.html')
        # mutian url: https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fclient_id%3Dd1043c275ddc4f64a60b2438db8ef839%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fnew-statify-app.appspot.com%252Fprofile%26scope%3Duser-top-read
        # alex url: https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fclient_id%3D6e1c71fa7d494c1db9a1e02dff1351ef%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fstatify-app.appspot.com%252Fprofile%26scope%3Duser-top-read
        token_url = "https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fclient_id%3Dd1043c275ddc4f64a60b2438db8ef839%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fnew-statify-app.appspot.com%252Fprofile%26scope%3Duser-top-read"
        # self.request.url gets current url
        new_dict = {'token_url': token_url}
        self.response.write(login_template.render(new_dict))  # the response

    def post(self):
        pass

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = the_jinja_env.get_template('templates/profile.html')

        current_url = self.request.url
        token = get_token(current_url)
        songs = get_songs(token)
        # token = current_url[49:]
        test_dict = {"current_url": 'this is a test'}
        new_dict = {"current_url": current_url, "songs": songs}
        if current_url == "https://new-statify-app.appspot.com/profile":
            self.response.write(profile_template.render(test_dict))  # without oauth token response
        else:
            self.response.write(profile_template.render(new_dict)) # with oauth token response

    def post(self):
        pass

class ArtistsPage(webapp2.RequestHandler):
    def get(self):
        artists_template = the_jinja_env.get_template('templates/artists.html')
        self.response.write(artists_template.render())  # the response

    def post(self):
        pass

class TracksPage(webapp2.RequestHandler):
    def get(self):
        tracks_template = the_jinja_env.get_template('templates/tracks.html')
        self.response.write(tracks_template.render())  # the response

    def post(self):
        pass
    
class RecentPage(webapp2.RequestHandler):
    def get(self):
        recent_template = the_jinja_env.get_template('templates/recent.html')
        self.response.write(recent_template.render())  # the response

    def post(self):
        pass

class PlaylistsPage(webapp2.RequestHandler):
    def get(self):
        playlists_template = the_jinja_env.get_template('templates/playlists.html')
        self.response.write(playlists_template.render())  # the response

    def post(self):
        pass

class FeaturesPage(webapp2.RequestHandler):
    def get(self):
        features_template = the_jinja_env.get_template('templates/features.html')
        self.response.write(features_template.render())  # the response

    def post(self):
        pass

class ContactPage(webapp2.RequestHandler):
    def get(self):
        contact_template = the_jinja_env.get_template('templates/contact.html')
        self.response.write(contact_template.render())  # the response

    def post(self):
        pass

class PrivacyPage(webapp2.RequestHandler):
    def get(self):
        privacy_template = the_jinja_env.get_template('templates/privacy.html')
        self.response.write(privacy_template.render())  # the response

    def post(self):
        pass

class OSLPage(webapp2.RequestHandler):
    def get(self):
        osl_template = the_jinja_env.get_template('templates/osl.html')
        self.response.write(osl_template.render())  # the response

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/profile', ProfilePage),
    ('/artists', ArtistsPage),
    ('/tracks', TracksPage),
    ('/recent', RecentPage),
    ('/playlists', PlaylistsPage),
    ('/features', FeaturesPage),
    ('/contact', ContactPage),
    ('/privacy', PrivacyPage),
    ('/osl', OSLPage)
], debug=True)
