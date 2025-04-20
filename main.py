import praw
import time
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")


# Reddit API credentials
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="Redlogs by /u/Downtown_Anteater_42"
)

def get_karma():
    user = reddit.redditor(reddit.user.me().name)
    return user.link_karma, user.comment_karma

# Store previous karma values
prev_link_karma, prev_comment_karma = get_karma()
print(f"Initial Link Karma: {prev_link_karma}, Comment Karma: {prev_comment_karma}")

while True:
    time.sleep(10)  # Check every 5 minutes
    link_karma, comment_karma = get_karma()
    
    if link_karma != prev_link_karma or comment_karma != prev_comment_karma:
        print("📈 Karma updated!")
        print(f"Link Karma: {link_karma} (Δ {link_karma - prev_link_karma})")
        print(f"Comment Karma: {comment_karma} (Δ {comment_karma - prev_comment_karma})")
        prev_link_karma, prev_comment_karma = link_karma, comment_karma
    else:
        print("No karma change yet.")
