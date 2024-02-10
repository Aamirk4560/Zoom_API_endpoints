import requests
client_id=""
client_secret=""
access_token=""

def create_zoom_meeting():
    url="https://api.zoom.us/v2/users/me/meetings"
    params={
        "Authorization": f"Bearer {access_token}"
    }
    data= {
        'topic': 'zoom meeting',
        'type': 1  # 1 for instant meeting, 2 for scheduled meeting
    }

    response=requests.post(url, params=params, json=data)

    if response.status_code == 201:
        meeting_info=response.json()
        print('Zoom meeting created successfully')
        print('Meeting ID: ', meeting_info['id'])
        print('Meeting Join Url', meeting_info['join_url'])

    else:
        print('Failed to create Zoom meeting.')
        print('Error: ', response.text)

# Call function to create a Zoom meeting
create_zoom_meeting()