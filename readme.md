# YOUTUBE_SUBSCRIBER_TRACKER

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Setup Youtube API KEY](#setup_youtube_api_key)

## Introduction

This script is designed to track YouTube subscriber count for a specific channel at regular intervals and update a visual representation of the subscriber count. Additionally, it updates an LED configuration based on changes in the subscriber count using a JSON configuration file.

### Project Purpose

The main goal of this project is to:

- Track YouTube subscriber counts at user-defined intervals.
- Update an image with the current subscriber count.
- Modify LED configurations based on changes in subscriber count.
- Provide a clear and interactive way for users to monitor their YouTube channel growth.

## Prerequisites

To run this script, ensure you have the following requirements installed:

- `Youtube API Key` - To setup your API Key follow [these instructions](#setup_youtube_api_key). 
- `Python 3.x`
- `requests` - Python library for making HTTP requests.
- `google-api-python-client` - Google API Client Library for Python.
- `oauth2client` - OAuth 2.0 client library for Python.
- `Pillow (PIL Fork)` - Python Imaging Library.
- `json` - JSON library for Python (typically included in the standard library).

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/YOUTUBE_SUBSCRIBER_TRACKER.git
2. Navigate to the cloned repository:

	```
	cd YOUTUBE_SUBSCRIBER_TRACKER
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install requests pillow google-api-python-client oauth2client
	```

## Configuration

The script uses a JSON configuration file to store pattern settings. Ensure that this file is correctly referenced and formatted.

### Key Fields

1. `custom_pattern_arr` : An array of pattern units where each unit contains `led_bits`, `color, speed`, and `delay` attributes.
2. `solid_color.color`: This field stores the color to be displayed on the LED.

## Usage
1. **Execute the script**:
You can run the script from the command line:
```
python main.py
```
2. **Provide API key and Channel Name:**

      Follow the prompts to enter your YouTube API key and the channel name you want to track.
  
3. **Start Tracking:**

    • When prompted, choose to start tracking the subscriber count.

    •  Set the interval for how often the script should check the subscriber count.
    
    • The script will display the subscriber count, update the LED configuration, and update the image with the subscriber count at each interval.
    
6. **Stopping the Script:**

	Press Ctrl+C to stop tracking and exit the program gracefully.

## Setup_Youtube_API_Key

1. Log in to Google Developers Console. (https://console.developers.google.com/project)
2. Create a new project.
3. On the new project dashboard, click Explore & Enable APIs.
4. In the library, navigate to YouTube Data API v3 under YouTube APIs.
5. Enable the API.
6. Create a credential.
7. A screen will appear with the API key.
8. Save your API key and use it to track subscriber count. 
