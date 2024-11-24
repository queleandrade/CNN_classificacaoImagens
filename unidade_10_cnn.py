# -*- coding: utf-8 -*-
"""Unidade 10 CNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12X0AfpqX6Vdn0PdeFzSnPBTdx5TpkJ1d
"""

import os

!pip install kaggle
!kaggle datasets download -d arbazkhan971/cuhk-face-sketch-database-cufs --force
!unzip -oq "cuhk-face-sketch-database-cufs.zip"

def list_files_in_folder(folder_path):
  """Lists all files in a given folder."""
  try:
    file_list = os.listdir(folder_path)
    return file_list
  except FileNotFoundError:
    print(f"Error: Folder not found at {folder_path}")
    return []

photos_folder = "photos"
files_in_photos = list_files_in_folder(photos_folder)

print(files_in_photos)
print(len(files_in_photos))

"""# Preparação dos Dados"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def load_and_preprocess_images(photo_folder):
    photos = []
    labels = []

    file_list = os.listdir(photo_folder)

    for filename in file_list:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(photo_folder, filename)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (250, 200))
            img = img / 255.0
            photos.append(img)
            if 'm' in filename.lower():
                labels.append(0)
            elif 'f' in filename.lower():
                labels.append(1)

    photos = np.array(photos)
    labels = np.array(labels)

    return photos, labels

photos_folder = "photos"
X, y = load_and_preprocess_images(photos_folder)

plt.imshow(X[0])
plt.title(f"Classe: {y[0]}")
plt.show()

"""# Divisão do Conjunto de Dados"""

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.5, random_state=23)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.4, random_state=23)

print(f"Treinamento: {X_train.shape[0]} imagens")
print(f"Validação: {X_val.shape[0]} imagens")
print(f"Teste: {X_test.shape[0]} imagens")

"""# Arquitetura da Rede Neural Convolucional"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(200, 250, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

"""# Treinamento do Modelo"""

history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

"""# Avaliação do Modelo"""

from sklearn.metrics import classification_report, roc_curve, auc

y_pred = (model.predict(X_test) > 0.5).astype("int32")

print(classification_report(y_test, y_pred))

fpr, tpr, thresholds = roc_curve(y_test, model.predict(X_test))
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc='lower right')
plt.show()

"""# Análise das Imagens Mal Classificadas"""

import matplotlib.pyplot as plt
import numpy as np

y_pred = (model.predict(X_test) > 0.5).astype("int32").flatten()

y_test = y_test.flatten()

misclassified_indices = np.where(y_pred != y_test)[0]

if len(misclassified_indices) > 0:
    print(f"Total de imagens mal classificadas: {len(misclassified_indices)}")

    num_columns = 4
    num_rows = int(np.ceil(len(misclassified_indices) / num_columns))
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(12, 6))
    axes = axes.ravel()

    for i, idx in enumerate(misclassified_indices):
        axes[i].imshow(X_test[idx])
        axes[i].set_title(f"Real: {y_test[idx]}, Pred: {y_pred[idx]}")
        axes[i].axis('off')

    for j in range(len(misclassified_indices), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Não há imagens mal classificadas.")