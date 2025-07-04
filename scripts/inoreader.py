import requests
from scripts.config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN

def get_access_token():
    response = requests.post('https://www.inoreader.com/oauth2/token', data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN
    })
    token = response.json().get('access_token')
    if not token:
        raise Exception("Failed to get access token.")
    print("Access Token Obtained.")
    return token

def fetch_articles(access_token, stream_id="user/-/label/AI%20News", n = 100):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        f'https://www.inoreader.com/reader/api/0/stream/contents/{stream_id}?n={n}',
        headers=headers
    )
    return response.json().get('items', [])
