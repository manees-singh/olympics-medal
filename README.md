# Olympics Medal Tracker Bot 
[𝕏/olympics_24](https://x.com/olympics_24)

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
    git clone https://github.com/your-username/olympics-medal.git
    cd olympics-medal
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

5. Run the bot script to post an update on Twitter:
    ```bash
    python bot.py
    ```

### GitHub Actions Workflow

The bot is set up to run on a regular schedule using GitHub Actions. The workflow file `schedule.yml` runs the scraper and bot scripts every 2 hours between 8 AM and 8 PM.

## Customization

- Modify the `scraper.py` script to add more countries or change the API endpoint.
- Adjust the `bot.py` script to change the tweet format or include additional data.
- Update the `schedule.yml` file to adjust the schedule as needed.

## Contributing

Feel free to fork this repository and make your own improvements. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [MIT](LICENSE) file for details.

