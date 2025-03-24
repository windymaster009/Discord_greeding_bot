# import discord
# from gtts import gTTS
# import os
# import asyncio  # Import asyncio for sleep functionality
# import random  # To randomly choose a greeting message

# intents = discord.Intents.default()
# intents.members = True  # To detect member join events
# intents.voice_states = True  # Required for voice channel updates

# bot = discord.Client(intents=intents)

# # Event: When a member joins or leaves a voice channel
# @bot.event
# async def on_voice_state_update(member, before, after):
#     # If the member joins a voice channel and is not already in one
#     if after.channel is not None and before.channel is None:
#         # Check if the bot is already in a voice channel
#         if bot.voice_clients:
#             # The bot is already in a voice channel, so don't try to join again
#             return

#         # Bot joins the same channel as the user
#         vc = await after.channel.connect()

#         # List of greeting messages
#         greeting_options = [
#             f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ឆានែលនេះ!",  # Welcome message in Khmer
#             f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់គេហទំព័រនេះ!",  # Welcome message in Khmer
#             f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ក្រុមនេះ!",  # Welcome message in Khmer
#             f"ហេ {member.display_name}! រីករាយដែលបានឃើញអ្នក!",  # Welcome message in Khmer
#             f"សួស្ដី {member.display_name}! សូមស្វាគមន៍មកកាន់ឆានែលនេះ!"   # Welcome message in Khmer
#             f"មិនដឹងស្អីទេ {member.display_name}! ចូលមកធ្វើអី!"   # Welcome message in Khmer
#         ]

#         # Randomly choose a greeting message
#         greeting_text = random.choice(greeting_options)

#         # Use gTTS (Google Text-to-Speech) to convert text to speech
#         tts = gTTS(greeting_text, lang='km')  # Khmer language
#         tts.save("welcome.mp3")  # Save the audio file

#         # Play the generated audio in the voice channel
#         vc.play(discord.FFmpegPCMAudio("welcome.mp3", executable="C:\\ffmpeg\\bin\\ffmpeg.exe"), after=lambda e: print(f'Finished playing for {member.name}'))

#         # Wait for 2 seconds before disconnecting
#         await asyncio.sleep(5)

#         # Disconnect from the voice channel after the 2-second wait
#         if vc.is_connected():
#             await vc.disconnect()

# # Event: Bot is ready and connected
# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user}!')

# # Run the bot with your token
# bot.run('token')