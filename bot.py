import tweepy
import os
import json
from PIL import Image, ImageDraw, ImageFont

# Load Twitter API credentials from environment variables
# api_key = os.getenv('API_KEY')
# api_secret = os.getenv('API_SECRET')
# bearer_token = os.getenv('BEARER_TOKEN')
# access_token = os.getenv('ACCESS_TOKEN')
# access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

api_key="BjxMbjnC1T1gmwzYmfF7sd4fD"                       #os.getenv('API_KEY')
api_secret="XnuPvFYnIZLwH9KcLX0sdv33lWKE9xt5yEn9Tm22QORWdZKS8x"                 #os.getenv('API_SECRET')
bearer_token="AAAAAAAAAAAAAAAAAAAAABHpvAEAAAAAq1u7G3c%2BYRW9OD%2FRh%2BMOhuDH9%2B4%3D0vDs9liZmoEeCMnELfFJSl61B0BtHiNogWjCYCD2X5GP3FcQ1G"                        #os.getenv('BEARER_TOKEN')
access_token="1820868688284696576-ENZYUbaoCwB8eSJMT4EXUSYlOAn8ku"                      #os.getenv('ACCESS_TOKEN')
access_token_secret="3HHspfQNsvcfKAz6H4ptJl4z3riaJufRkaCekO7idFLnP"                        #os.getenv('ACCESS_TOKEN_SECRET')


# Authenticate to Twitter using Client
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)

# Authenticate to Twitter using OAuth1 for compatibility
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Text for the tweet
# tweet_text = (
#     "1. Singapore 🇸🇬 🥇\n"
#     "=2. France 🇫🇷 🥈\n"
#     "=2. Germany 🇩🇪 🥉\n"
#     "=2. France 🇫🇷\n"
#     "=2. Germany 🇩🇪\n"
#     "=2. Italy 🇮🇹\n"
#     "=2. Spain 🇪🇸\n"
#     "=2. Japan 🇯🇵\n"
#     "=3. South Korea 🇰🇷\n"
#     "=3. Finland 🇫🇮\n"
#     "=3. Sweden 🇸🇪\n"
#     "=3. Austria 🇦🇹\n"
#     "=3. Ireland 🇮🇪\n"
#     "=3. Netherlands 🇳🇱\n"
#     "=3. Luxembourg 🇱🇺\n"
#     "=4. Denmark 🇩🇰\n"
#     "=4. Belgium 🇧🇪\n"
    
#     "~"
# )

hi='CHN'

tweet_text = chr(ord(hi[0]) + 127397) + chr(ord(hi[2]) + 127397)
# Post the tweet
response=client.create_tweet(text=tweet_text)

print("Tweet posted successfully!")


# # Load medal data
# with open('medal_data.json', 'r') as f:
#     medal_data = json.load(f)

# # Select the top 10 countries
# top_countries = list(medal_data.items())[:15]  # Fetching top 15 s

# # Prepare the tweet text
# tweet_text = "#Paris2024\n"+ "#Olympics2024\n"  + "#Olympics2024Paris\n" + "Gold Medals tally\n"+ "\n".join([f"{country_id}: {data[0]}" for country_id, data in top_countries])

# # Post the tweet with the text
# response = client.create_tweet(text=tweet_text)




 