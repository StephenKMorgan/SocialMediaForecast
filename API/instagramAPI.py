from instascrape import Profile, scrape_posts

# Replace 'your-instagram-username' with the Instagram username you want to scrape
username = 'your-instagram-username'

# Instantiate a Profile object and scrape it
profile = Profile(username)
profile.scrape()

# Scrape the last 10 posts
posts = scrape_posts(profile.recent_posts[:10])

# Print details of each post
for post in posts:
    print(f"Post ID: {post.id}")
    print(f"Post URL: {post.url}")
    print(f"Number of likes: {post.likes}")
    print(f"Caption: {post.caption}\n")