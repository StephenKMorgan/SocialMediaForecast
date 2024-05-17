import requests
import json

# Replace 'your-access-token' with your actual access token
access_token = 'your-access-token'

# The Graph API URL for getting the last 10 posts from your homepage
url = f'https://graph.facebook.com/me/feed?limit=10&access_token={access_token}'

# Make a GET request to the Graph API
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Loop through the posts and print their details
    for post in data['data']:
        print(f"Post ID: {post['id']}")
        print(f"Message: {post.get('message', 'No message provided')}\n")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")