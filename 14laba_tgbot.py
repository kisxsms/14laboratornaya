import os
import telebot
from pydub import AudioSegment

bot = telebot.TeleBot('7049407767:AAFWjT3qzUBJfEchmE0usj0kTYfutbtGjLw')

def welcome_message():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет!! Чтобы получить найткор версию нужной песни, просто перешли ее в этот ботик или отправь в формате mp3^^")

welcome_message()

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    process_audio(message)

@bot.message_handler(content_types=['audio'])
def handle_forwarded_audio(message):
    process_audio(message)

def process_audio(message):
    file_id = message.audio.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    original_filename = message.audio.file_name
    with open(original_filename, 'wb') as file:
        file.write(downloaded_file)

    audio = AudioSegment.from_file(original_filename, format="mp3")

    speed = 1.3

    audio = audio.speedup(playback_speed=speed)

    new_filename = original_filename.replace(".mp3", f" @shashanightcore.mp3")
    audio.export(new_filename, format="mp3")

    with open(new_filename, 'rb') as file:
        bot.send_audio(message.chat.id, file)

    os.remove(original_filename)
    os.remove(new_filename)


bot.polling()