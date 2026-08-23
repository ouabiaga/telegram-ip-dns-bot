# Telegram IP and DNS Lookup Bot

A simple Telegram bot written in Python for looking up IP address and DNS information.

## Features

- Get location and ISP information for an IP address
- Look up DNS information for a domain name
- Use simple Telegram commands
- Run the bot with Telegram long polling

## Requirements

- Python 3.8 or newer
- A Telegram bot token
- Internet access

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ouabiaga/telegram-ip-dns-bot.git
   cd telegram-ip-dns-bot
   ```

2. Install the required Python packages:

   ```bash
   pip install python-telegram-bot requests
   ```

   On some systems, use:

   ```bash
   python -m pip install python-telegram-bot requests
   ```

## Telegram Bot Setup

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Send the `/newbot` command.
3. Follow the instructions and copy the bot token.
4. Open `telegram_bot.py`.
5. Replace the placeholder token:

   ```python
   token = "YOUR_TELEGRAM_BOT_TOKEN"
   ```

   with your real token:

   ```python
   token = "123456789:your-telegram-bot-token"
   ```

   Keep your token private and do not commit it to GitHub.

## Usage

Start the bot from the project directory:

```bash
python telegram_bot.py
```

Open your bot in Telegram and use these commands:

| Command | Description | Example |
| --- | --- | --- |
| `/help` | Shows the available command | `/help` |
| `/ip <IP_ADDRESS>` | Returns country, region, city, and ISP information | `/ip 8.8.8.8` |
| `/dns <DOMAIN_NAME>` | Returns DNS information for a domain | `/dns example.com` |

The bot must remain running in the terminal to receive messages.

## Example Response

For an IP lookup, the bot may respond with:

```text
IP Address: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ISP: Google LLC
```

## APIs Used

- [IP-API](http://ip-api.com/) for IP geolocation and ISP information
- [EDNS IP-API](http://edns.ip-api.com/) for DNS information

The availability and accuracy of the results depend on these external services. Their usage limits and terms may apply.

## Security Notes

- Never publish your Telegram bot token.
- Do not hard-code private credentials in public repositories.
- For a production project, load the token from an environment variable and add local secret files to `.gitignore`.

## Troubleshooting

### `ModuleNotFoundError`

Install the dependencies again:

```bash
python -m pip install python-telegram-bot requests
```

### The bot does not respond

- Check that the script is still running.
- Verify that the Telegram token is correct.
- Make sure your computer has internet access.
- Confirm that the command format is correct, for example `/ip 8.8.8.8`.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
