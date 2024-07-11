import time
import signal
from youtube_utils import get_api_key_and_channel, get_channel_id, get_interval, get_subscriber_count
from draw_subscription_info import draw_subscription_info
from led_config import update_led_config

# Global variable to control the tracking loop
tracking = True

def signal_handler(sig, frame):
    global tracking
    print("\nTracking stopped. Exiting the program.")
    tracking = False

def get_drive_letter():
    while True:
        drive_letter = input("Please enter the drive letter asigned to Busy Tag device (e.g., D): ").strip().upper()
        if len(drive_letter) == 1 and drive_letter.isalpha():
            return drive_letter
        else:
            print("Invalid drive letter. Please enter a single letter (e.g., D).")

def main():
    global tracking
    signal.signal(signal.SIGINT, signal_handler)

    if input("Have you connected the Busy Tag device? (y/n): ").strip().lower() == 'y':
    # Ask user for the drive letter
        drive_letter = get_drive_letter()

    else:
         print("Please connect the Busy Tag device and restart program.")
         return
    
    # Get API key and username (channel name) from user input
    api_key, username = get_api_key_and_channel()
    
    # Get the channel ID using the username
    channel_id, username = get_channel_id(api_key, username)

    if channel_id is None or username is None:
        return  # Exit the program if channel ID or username is invalid
    
    # Ask user if they want to start tracking
    if input(f"\nDo you want to start tracking subscriber count for {username}? (y/n): ").strip().lower() == 'y':
        # Ask user for interval
        interval = get_interval()
        
        # Initialize previous subscriber count
        previous_subscriber_count = None
        
        print(f"Tracking started. Subscriber count will be checked every {interval} seconds.")
        print("\nPress ctrl+c to stop tracking and exit the program")

        # Start tracking the subscriber count
        while tracking:
            try:
                # Get the current subscriber count
                subscriber_count = get_subscriber_count(api_key, channel_id)
                if subscriber_count is not None:
                    print(f"Subscriber count for channel {username}: {subscriber_count}")
                    
                    # Update LED configuration based on the subscriber count change
                    update_led_config(previous_subscriber_count, subscriber_count, drive_letter)
                    previous_subscriber_count = subscriber_count
                    
                    # Define paths
                    background_image_path = "background.png"  # Replace with your background image path
                    output_path = rf"{drive_letter}:\subscription_info.png"   # Replace with your desired output path
                    
                    # Draw the subscription info on the image
                    draw_subscription_info(username, subscriber_count, background_image_path, output_path)
                    
                # Sleep for the defined interval
                for _ in range(interval):
                    if not tracking:
                        break
                    time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}")
                break
    else:
        print("\nExiting the program.")

if __name__ == "__main__":
    main()