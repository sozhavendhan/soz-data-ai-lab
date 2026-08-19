"""
Simple TensorFlow example (train a tiny model on random data) - illustrative only.

Requirements: tensorflow
Run:
python ai-engineering/deep-learning/simple_tf_mnist.py
"""
import numpy as np
import tensorflow as tf

# Tiny synthetic dataset
x = np.random.random((100, 20)).astype('float32')
y = np.random.randint(0, 2, size=(100,))

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(20,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=2, batch_size=16)
