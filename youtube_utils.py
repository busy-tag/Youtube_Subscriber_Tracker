import os
import googleapiclient.discovery
import time

def get_channel_id(api_key, username):
    try:
        # Disable OAuthlib's HTTPS verification when running locally.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
        
        # Use the search.list method to find the channel ID by username
        request = youtube.search().list(
            part="id",
            type="channel",
            q=username
        )
        response = request.execute()
        
        # Extract the channel ID from the response
        if "items" in response and len(response["items"]) > 0:
            channel_id = response["items"][0]["id"]["channelId"]
            return channel_id, username
        else:
            print("Channel not found. Please check your username and restart program.")
            return None, None
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your API key and restart program.")
        return None, None

def get_subscriber_count(api_key, channel_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    
    # Use the channels.list method to retrieve channel information, including subscriber count
    request = youtube.channels().list(
        part="statistics",
        id=channel_id
    )
    response = request.execute()
    
    # Extract the subscriber count from the response
    subscriber_count = int(response["items"][0]["statistics"]["subscriberCount"])
    return subscriber_count

def get_api_key_and_channel():
    # Prompt the user to enter their YouTube API key
    api_key = input("\nEnter your YouTube API key: ")
    
    # Prompt the user to enter the username (channel name)
    username = input("Enter the username (channel name) you want to query: ")
    
    return api_key, username

def get_interval():
    while True:
        try:
            interval = int(input("Enter the interval in seconds for checking subscriber count (e.g., 60) allow minimum of 20 seconds: "))
            if interval <= 0:
                print("Interval must be greater than zero.")
            else:
                return interval
        except ValueError:
            print("Invalid input. Please enter a valid integer.")