import discord
from gtts import gTTS
import os
import asyncio  # Import asyncio for sleep functionality
import random  # To randomly choose a greeting message

intents = discord.Intents.default()
intents.members = True  # To detect member join events
intents.voice_states = True  # Required for voice channel updates

bot = discord.Client(intents=intents)

# Set the specific user IDs for the special greetings
special_user_id_1 =   # Replace with the first special user ID
special_user_id_2 =   # Replace with the second special user ID
special_user_id_3 =   # Replace with the third special user ID (User ID 3)
bot_role_id =   # The bot's role ID that should not trigger the greeting

# Event: When a member joins or leaves a voice channel
@bot.event
async def on_voice_state_update(member, before, after):
    # If the member joins a voice channel and is not already in one
    if after.channel is not None and before.channel is None:
        # Exclude the bot itself from being greeted
        if member.bot:  # Check if the member is the bot itself
            return

        # Check if the bot is already in a voice channel
        if bot.voice_clients:
            # The bot is already in a voice channel, so don't try to join again
            return

        # Bot joins the same channel as the user
        vc = await after.channel.connect()

        # If the member is user ID 3, set the English greeting for them
        if member.id == special_user_id_3:
            greeting_text = "King is back!"  # English greeting for user 3

        # If the member is the first special user, set a special greeting message
        elif member.id == special_user_id_1:
            greeting_options = [
                f"មេ {member.display_name} មកហើយ!",  # Special greeting for the first user
                f"មេ {member.display_name} បានចូលរួម!"  # Special greeting for the first user
            ]
            greeting_text = random.choice(greeting_options)  # Randomly choose a greeting for the first special user

        # If the member is the second special user, set a unique greeting
        elif member.id == special_user_id_2:
            greeting_options = [
                f"មេ {member.display_name} មកហើយបើក Valorant!",  # Special greeting for the second user
                f"មេ {member.display_name} មកហើយឈុបលេង​ Game បើក Valorant !"  # Special greeting for the second user
            ]
            greeting_text = random.choice(greeting_options)  # Randomly choose a greeting for the second special user

        else:
            # List of greeting messages for other users
            greeting_options = [
                f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ឆានែលនេះ!",  # Welcome message in Khmer
                f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់គេហទំព័រនេះ!",  # Welcome message in Khmer
                f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ក្រុមនេះ!",  # Welcome message in Khmer
                f"ហេ {member.display_name}! រីករាយដែលបានឃើញអ្នក!",  # Welcome message in Khmer
                f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ឆានែលនេះ!",  # Welcome message in Khmer
                f"មិនដឹងស្អីទេ {member.display_name}! ចូលមកធ្វើអី!"  # Welcome message in Khmer
            ]

            # Randomly choose a greeting message for other users
            greeting_text = random.choice(greeting_options)

        # Use gTTS (Google Text-to-Speech) to convert text to speech
        # Check the language based on the user's ID
        if member.id == special_user_id_3:
            tts = gTTS(greeting_text, lang='en')  # English language for user 3
        else:
            tts = gTTS(greeting_text, lang='km')  # Khmer language for other users

        tts.save("welcome.mp3")  # Save the audio file

        # Play the generated audio in the voice channel
        vc.play(discord.FFmpegPCMAudio("welcome.mp3", executable="C:\\ffmpeg\\bin\\ffmpeg.exe"), after=lambda e: print(f'Finished playing for {member.name}'))

        # Wait for 5 seconds before disconnecting
        await asyncio.sleep(5)

        # Disconnect from the voice channel after the 5-second wait
        if vc.is_connected():
            await vc.disconnect()

# Event: Bot is ready and connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Run the bot with your token
bot.run('token')
