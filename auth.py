import functools

from flask import (Blueprint, current_app, render_template, url_for, session, redirect, request, make_response)
import spotipy
import spotipy.util as util
import requests
from . import creds

bp = Blueprint('auth', __name__, url_prefix='/auth')

API_BASE = 'https://accounts.spotify.com'

REDIRECT_URI = 'http://127.0.0.1:5000/auth/api_callback'

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

SHOW_DIALOG = True

@bp.route('/login/')
def login():
  auth_url = f'{API_BASE}/authorize?client_id={creds.CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog={SHOW_DIALOG}'
  return redirect(auth_url)

@bp.route('/api_callback/')
def api_callback():
  session.clear()
  code = request.args.get('code')
  auth_token_url = f"{API_BASE}/api/token"
  res = requests.post(auth_token_url, data={
    "grant_type":"authorization_code",
    "code":code,
    "redirect_uri":"http://127.0.0.1:5000/auth/api_callback",
    "client_id":creds.CLI_ID,
    "client_secret":creds.CLI_SECRET
  })
  res_body = res.json()
  session["token"] = res_body.get("access_token")
  # print("token=" + str(session["token"]))
  return redirect('/dashboard')