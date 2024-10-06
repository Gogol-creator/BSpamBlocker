import tweepy
#You need API for this script
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
bearer_token = 'your_bearer_token'

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

user = client.get_user(username="")
user_id = user.data.id

followers = client.get_users_followers(id=user_id)

for follower in followers.data:
    try:
        client.block(follower.id)
        print(f"User is blocked with ID: {follower.id}")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
