
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
​1. إعدادات نموذج التدريب والبيانات
​IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10
NUM_CLASSES = 4  # الفئات الأربع: Tumor, Cyst, Stone, Normal
​2. تجهيز مولد البيانات وتقنيات زيادة البيانات (Data Augmentation)
​train_datagen = ImageDataGenerator(
rescale=1./255,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
validation_split=0.2
)
​def build_model():
"""
بناء معماريّة شبكة التلافيف العصبية (CNN / Transfer Learning)
"""
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
​# تجميد طبقات النموذج الأساسي
for layer in base_model.layers:
layer.trainable = False
​model = Sequential([
base_model,
Flatten(),
Dense(256, activation='relu'),
Dropout(0.5),
Dense(NUM_CLASSES, activation='softmax')
])
​model.compile(
optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy']
)
​return model
​if name == 'main':
print("🚀 بدء إعداد نموذج تدريب تشخيص أمراض الكلى...")
model = build_model()
model.summary()
print("✅ اكتمل إعداد ملف التدريب بنجاح!")
