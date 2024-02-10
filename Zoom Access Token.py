from flask import Flask, redirect, request
import requests
import base64
import json

app = Flask(__name__)

# Replace 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET', and 'YOUR_REDIRECT_URI'
# with your actual Zoom OAuth credentials and the redirect URI you specified in your Zoom app settings.
CLIENT_ID = ''
CLIENT_SECRET = ''  # Your Zoom app's client secret
REDIRECT_URI = ''

ZOOM_AUTH_URL = 'https://zoom.us/oauth/authorize'
ZOOM_TOKEN_URL = 'https://zoom.us/oauth/token'

@app.route('/')
def home():
    # Construct the authorization URL
    params = {
        'client_id': CLIENT_ID,
        'response_type': '',
        'redirect_uri': REDIRECT_URI,
    }
    authorization_url = f"{ZOOM_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        # Exchange the authorization code for an access token
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        headers = {
            'Authorization': f"Basic {base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()}"
        }

        response = requests.post(ZOOM_TOKEN_URL, data=data, headers=headers)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            return f"Access Token: {access_token}"
        else:
            return "Failed to get the access token."
    else:
        return "Authorization code not found."

if __name__ == '__main__':
    app.run(port=8000)