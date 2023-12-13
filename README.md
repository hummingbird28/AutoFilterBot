# Auto Filter Bot

## Introduction

This bot is designed to perform various functions based on user interactions. The configuration is done using environment variables, making it easy to customize the bot's behavior.

## Getting Started

### Prerequisites

- Python 3.x
- `python-dotenv` library: Install it using `pip install python-dotenv`

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/hummingbird28/AutoFilterBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AutoFilterBot
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure the following variables:

   ```env
   BOT_TOKEN=<your_bot_token>
   CACHE_TIME=300
   DATABASE_URI=
   ADMINS=10
   # Add other configuration variables as needed
   ```

5. Run the bot:

   ```bash
   python bot.py
   ```

## Configuration

### Bot Information and Settings

- `BOT_TOKEN`: switch bot token obtained from the BotFather.
- `CACHE_TIME`: Cache time for certain bot operations.
- `USE_DESCRIPTION_FILTER`: Boolean indicating whether a description filter should be used.
- `PICS`: List of URLs for pictures.

### Admins, Channels & Users

- `ADMINS`: List of admin user IDs.
- `CHANNELS`: List of channel IDs.
- `AUTH_USERS`: List of authorized user IDs.
- `AUTH_CHANNEL`: Chat ID for authorized channel.
- `AUTH_GROUPS`: List of authorized group chat IDs.

### Database Configuration

- `DATABASE_URI`: Database URI.
- `DATABASE_NAME`: Database name.
- `COLLECTION_NAME`: Collection name.

### Other Settings

- `LOG_CHANNEL`: Chat ID for log channel.
- `SUPPORT_CHAT`: Support chat username.
- `P_TTI_SHOW_OFF`: Boolean indicating whether to redirect users to send `/start` in Bot PM.
- `IMDB`: Boolean indicating whether to enable IMDB results.
- `SINGLE_BUTTON`: Boolean indicating whether to show filename and file size in a single button.
- `CUSTOM_FILE_CAPTION`: Custom caption for files.
- ... (other variables)

### Logging Configuration

- `LOG_STR`: Summary of current customized configurations.

## Usage

Provide instructions on how users can interact with the bot and any available commands.

## Contributing

If you'd like to contribute to the project, please follow the standard GitHub flow:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
