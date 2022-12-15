import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

epochs = 10
batch_size = 16
margin = 1

x = np.load("Dataset/X_8020.npy")
y = np.load("Dataset/Y_8020.npy")
y = np.reshape(y, (y.shape[0], 1))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.0909, random_state=0)

x_train_1 = x_train[:,0]
x_train_2 = x_train[:,1]

x_test_1 = x_test[:,0]
x_test_2 = x_test[:,1]

y_train = tf.cast(y_train, tf.float32)
y_test = tf.cast(y_test, tf.float32)

def euclidean_distance(vects):
    x, y = vects
    sum_square = tf.math.reduce_sum(tf.math.square(x - y), axis=1, keepdims=True)
    return tf.math.sqrt(tf.math.maximum(sum_square, keras.backend.epsilon()))

input = keras.layers.Input((100, 100, 1))
x = tf.keras.layers.BatchNormalization()(input)
x = layers.Conv2D(2, (10, 10), activation="tanh", padding = 'same')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Conv2D(4, (10, 10), activation="tanh", padding = 'same')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Conv2D(8, (10, 10), activation="tanh", padding = 'same')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Conv2D(16, (10, 10), activation="tanh", padding = 'same')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Conv2D(32, (10, 10), activation="tanh", padding = 'same')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Flatten()(x)

x = tf.keras.layers.BatchNormalization()(x)
x = layers.Dense(100, activation="tanh")(x)
embedding_network = keras.Model(input, x)


input_1 = keras.layers.Input((100, 100, 1))
input_2 = keras.layers.Input((100, 100, 1))


tower_1 = embedding_network(input_1)
tower_2 = embedding_network(input_2)

merge_layer = keras.layers.Lambda(euclidean_distance)([tower_1, tower_2])
normal_layer = keras.layers.BatchNormalization()(merge_layer)
output_layer = keras.layers.Dense(1, activation="tanh")(normal_layer)
siamese = keras.Model(inputs=[input_1, input_2], outputs=output_layer)

def loss(margin=1):
    def contrastive_loss(y_true, y_pred):
        square_pred = tf.math.square(y_pred)
        margin_square = tf.math.square(tf.math.maximum(margin - (y_pred), 0))
        return tf.math.reduce_mean((1 - y_true) * square_pred + (y_true) * margin_square)
    return contrastive_loss

siamese.compile(loss=loss(margin=margin), optimizer="Adam", metrics=["accuracy"])
siamese.summary()

history = siamese.fit([x_train_1, x_train_2], y_train,batch_size=batch_size,epochs=epochs)
siamese.evaluate([x_test_1, x_test_2], y_test)
'''
plt.ylim([0,1])
plt.plot(history.history['accuracy'])
plt.ylim([0,0.6])
plt.plot(history.history['loss'])
'''