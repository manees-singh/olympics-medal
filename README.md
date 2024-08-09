# Olympics Medal Tracker Bot

This project contains a Python-based Twitter bot that tracks Olympic medals and posts regular updates on Twitter. The bot scrapes data from an API and formats it for a Twitter post, displaying the top-performing countries with their respective medal counts and flag emojis.

## Project Structure

- **scraper.py**: This script fetches data from an Olympic Games API, processes the data to extract medal counts for each country, and maps country codes to flag emojis. The results are saved in a `medal_data.json` file.
- **bot.py**: This script loads the medal data from `medal_data.json`, formats it into a tweet, and posts it on Twitter using the Twitter API.
- **schedule.yml**: A GitHub Actions workflow that runs the bot on a regular schedule.
- **requirements.txt**: A list of dependencies required to run the Python scripts.

## How It Works

### 1. Scraper Script (scraper.py)
- Fetches Olympic medal data from an API.
- Processes the data to extract and organize medal counts for each country.
- Maps country codes to flag emojis.
- Saves the processed data into a `medal_data.json` file.

### 2. Twitter Bot (bot.py)
- Loads the processed medal data from the `medal_data.json` file.
- Formats the data into a tweet-friendly format.
- Posts the update to Twitter using the Tweepy library.

### 3. GitHub Actions Workflow (schedule.yml)
- The workflow is set to run the bot on a regular schedule, updating Twitter with the latest medal counts.

## Setup Instructions

### Prerequisites

- Python 3.x
- Tweepy library
- A Twitter Developer account with API keys and tokens

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/olympics-medal-tracker.git
    cd olympics-medal-tracker
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Twitter API credentials as environment variables:
    - `API_KEY`
    - `API_SECRET`
    - `BEARER_TOKEN`
    - `ACCESS_TOKEN`
    - `ACCESS_TOKEN_SECRET`

4. Run the scraper script to fetch and process the latest medal data:
    ```bash
    python scraper.py
    ```

5. Run the bot
