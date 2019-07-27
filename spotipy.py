import os
import sys
import json
import secret

import spotipy
from spotipy import util

token = util.prompt_for_user_token('', 'user-top-read', client_id=secret.CLIENT_ID, client_secret=secret.CLIENT_SECRET, redirect_uri=secret.REDIRECT_URI)
print(token)