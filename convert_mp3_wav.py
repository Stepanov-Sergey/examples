'''
Конвертер файлов mp3 в wav
Требуется указать путь к кодеку
'''
import os
import subprocess

# Путь к директории с файлами mp3
mp3_directory = "mp3"

# Путь к директории, в которую будут сохранены файлы wav
wav_directory = "wav"

# Создание директории wav, если она не существует
if not os.path.exists(wav_directory):
    os.makedirs(wav_directory)

# Проход по файлам в директории mp3
for filename in os.listdir(mp3_directory):
    if filename.endswith(".mp3"):
        mp3_path = os.path.join(mp3_directory, filename)
        wav_path = os.path.join(wav_directory, os.path.splitext(filename)[0] + ".wav")

        # Конвертирование файла mp3 в wav с помощью ffmpeg
        subprocess.run(["E:/Temp/ffmpeg.exe", "-i", mp3_path, wav_path])
