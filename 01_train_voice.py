'''
***Выполнение обучения и сохранение модели***
'''
import os
import tensorflow as tf
from tensorflow.keras.layers import Conv1D, MaxPooling1D, GlobalAveragePooling1D, Dropout, Dense, LSTM, Input
from tensorflow.keras.models import Sequential, Model
import librosa  

# Путь к папке с файлами .wav и .txt, которые нужно обработать
data_path = 'path/to/data/folder'

# Создайте список файлов .wav в заданной папке
wav_files = [file for file in os.listdir(data_path) if file.endswith('.wav')]

# Создайте модель генерации речи
input_layer = Input(shape=(None, 1))
x = Conv1D(32, 3, activation='relu')(input_layer)
x = MaxPooling1D(2)(x)
x = Conv1D(64, 3, activation='relu')(x)
x = MaxPooling1D(2)(x)
x = Conv1D(128, 3, activation='relu')(x)
x = MaxPooling1D(2)(x)
x = Conv1D(256, 3, activation='relu')(x)
x = GlobalAveragePooling1D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(512, activation='relu')(x)
output_layer = Dense(len(output_text), activation='softmax')(x)

model = Model(input_layer, output_layer)

# Обучите модель генерации речи на основе предоставленных записей голоса и текстов
for wav_file in wav_files:
    # Загрузите каждый файл .wav и соответствующий текст из файла .txt
    input_audio, sr = librosa.load(os.path.join(data_path, wav_file))
    text_file = os.path.join(data_path, 'text', wav_file.split('.')[0] + '.txt')
    with open(text_file, 'r') as f:
        output_text = f.read().replace('\n', '')
    
    # Обучите модель на каждой записи голоса и соответствующем тексте
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    model.fit(input_audio, output_text, epochs=20)

# Сохраните обученную модель в файл
model.save('path/to/saved/model')
