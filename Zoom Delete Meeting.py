import requests

meeting_id = ''
access_token = ''

url = f'https://api.zoom.us/v2/meetings/{meeting_id}'

params = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.delete(url, params=params)

if response.status_code == 204:
    print("Meeting deleted successfully!")
else:
    print(f"Failed to delete meeting. Status code: {response.status_code}")
