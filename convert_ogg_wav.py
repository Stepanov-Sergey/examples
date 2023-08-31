'''
Конвертер файлов из  /ogg/*.ogg в /wav/*.wav
в директории с convert_ogg_wav.py должен быть файл ffprobe.exe
'''
import os
from pydub import AudioSegment

ogg_folder = 'ogg'  # Путь к папке с файлами .ogg
wav_folder = 'wav'  # Путь к папке, в которую будут сохранены файлы .wav

if not os.path.exists(wav_folder):
    os.makedirs(wav_folder)

converted_files = []  # Список для хранения имен конвертированных файлов

for filename in os.listdir(ogg_folder):
    if filename.endswith('.ogg'):
        ogg_path = os.path.join(ogg_folder, filename)
        wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + '.wav')
        audio = AudioSegment.from_file(ogg_path, format='ogg')
        audio.export(wav_path, format='wav')
        converted_files.append(os.path.splitext(filename)[0] + '.wav')  # Добавляем имя конвертированного файла в список

print("Следующие файлы были успешно конвертированы:")
for file in converted_files:
    print(file)
