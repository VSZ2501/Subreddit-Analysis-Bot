# Subreddit Analysis Bot and Export to Google Sheets

## Welcome

Hello and welcome to the Subreddit Analysis Bot project! This tool is designed to help you gather and organize data from Reddit and export it to Google Sheets effortlessly.

## Project Description

This project is a bot that retrieves information on the top 30 posts from the "Top - This Month" section of a specified subreddit and exports them into a Google Sheets file.

## Features

- **Data Retrieval**:
  - Targets a subreddit specified in a text file named `subreddit.txt`.
  - Extracts the following information for each post:
    - Date (format: YYYY-MM-DD).
    - Time (format: HH:MM, without seconds).
    - Number of upvotes.
    - Post title.

- **Export to Google Sheets**:
  - Adds data to an existing Google Sheets file.
  - Expected structure:
    - Columns: Date | Time | Number of upvotes | Title.
    - Appends data without overwriting previous entries.

## Prerequisites

- Python installed on your machine.
- Google Cloud account with access to Google Sheets and Google Drive APIs.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**:

   ```bash
   pip install praw gspread oauth2client
   ```

3. **Set up Google Sheets credentials**:

   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project and enable the Google Sheets and Google Drive APIs.
   - Create a service account and download the JSON key file.
   - Rename this file to `credentials.json` and place it in the root directory of the project.
   - Share your Google Sheets file with the service account email address.

4. **Configure the `subreddit.txt` file**:

   - Create a file named `subreddit.txt` in the root directory.
   - Write the name of the subreddit you wish to analyze (e.g., `python`).

## Additional Setup for Reddit API

To use this program, you need to create a Reddit application:

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps).
2. Log in with your Reddit account.
3. Click "Create App" or "Create Another App".
4. Fill out the form:
   - **Name**: Give your application a name.
   - **App type**: Select "script".
   - **Redirect URI**: Enter `http://localhost:8080`.
5. Click "Create app".
6. Note your `client_id`, `client_secret`, and set a `user_agent`.

## Running the Program

1. Ensure all necessary files are in place (`credentials.json`, `subreddit.txt`).

2. Run the script:

   ```bash
   python main.py
   ```

3. Enter your Reddit API credentials and the name of your Google Sheets file in the interface.

4. The program will save your Reddit API credentials in `reddit_config.txt` for future use. If this file exists, the program will automatically fill in the credentials for you.

## Script Functionality

- The script reads the subreddit name from `subreddit.txt`.
- It uses the Reddit API to retrieve the top 30 posts of the month.
- The data is formatted and exported to a Google Sheets file.
- New data is appended to the end of the file without overwriting existing data.

## Notes

- Ensure your Google Sheets file is properly shared with the service account.
- The Reddit API credentials are saved in `reddit_config.txt` for convenience.

---

© 2023 Sofian Lahlou. All rights reserved.
