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

import webapp2
import jinja2
import os

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
        self.response.write(login_template.render())  # the response

    def post(self):
        pass

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = the_jinja_env.get_template('templates/profile.html')
        self.response.write(profile_template.render())  # the response

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
