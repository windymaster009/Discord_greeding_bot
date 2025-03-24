# Discord Voice Greeting Bot 🎙️  

This is a Discord bot that joins a voice channel and greets users with a text-to-speech (TTS) message in Khmer or English when they join.  

## Features  
- Uses Google Text-to-Speech (gTTS) for voice greetings.  
- Custom greetings for specific users.  
- Randomized welcome messages for other members.  
- Automatically disconnects after greeting.  

## Installation  

1. Install dependencies:  
   ```sh
   pip install -r requirements.txt

Ensure you have `FFmpeg` installed and set the correct path in the script.

## Run the bot:
 `python main.py`

## Requirements
### Python 3.8+

`discord.py`, `gtts`, `asyncio`, `aiohttp`, `random2`

`FFmpeg`(for playing audio in voice channels)

Configuration
Replace `YOUR_BOT_TOKEN` in the script with your actual bot token.

Update `special_user_id_1`, `special_user_id_2`, `special_user_id_3`and  with the correct user IDs.
