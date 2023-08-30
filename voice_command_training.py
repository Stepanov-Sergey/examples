'''
Примерный код, показывающий, как обучить модель на основе файлов WAV
В этом коде мы проходим по файлам WAV,
извлекаем признаки MFCC из каждого аудиофайла и добавляем их в список данных data,
а также добавляем соответствующую метку класса в список меток labels.
Затем мы разбиваем данные на обучающую и проверочную выборки,
создаем модель нейронной сети с LSTM слоем,
компилируем модель и обучаем ее на данных.
При необходимости вы можете настроить параметры модели и обучения в соответствии с вашими требованиями.

Если вы хотите, чтобы скрипт мог извлекать метку класса из имени файла, вам нужно наименовать файлы согласно определенной схеме. Например, вы можете использовать следующий формат имени файла: {метка_класса}_{дополнительная_информация}.wav.
Вот пример файлов с правильными именами:
команда_1_001.wav
команда_2_002.wav
команда_1_003.wav
'''

import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM

# Путь к директории с файлами WAV
wav_directory = "путь_к_директории_wav"

# Список классов команд
classes = ["команда_1", "команда_2", "команда_3"]

# Параметры аудио
sample_rate = 22050
duration = 1  # Длительность каждого аудиофайла

# Загрузка данных
data = []
labels = []

for filename in os.listdir(wav_directory):
    if filename.endswith(".wav"):
        wav_path = os.path.join(wav_directory, filename)
        label = filename.split("_")[0]  # Извлечение метки класса из имени файла
        
        # Извлечение признаков из аудиофайла
        y, sr = librosa.load(wav_path, sr=sample_rate, duration=duration)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        
        # Добавление признаков и метки в списки данных
        data.append(mfcc)
        labels.append(classes.index(label))

# Разбиение данных на обучающую и проверочную выборки
train_data, test_data, train_labels, test_labels = train_test_split(
    np.array(data), np.array(labels), test_size=0.2, random_state=42
)

# Создание модели нейронной сети
model = Sequential()
model.add(LSTM(64, input_shape=(train_data.shape[1], train_data.shape[2])))
model.add(Dense(len(classes), activation="softmax"))

# Компиляция модели
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Обучение модели
model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_data=(test_data, test_labels))
