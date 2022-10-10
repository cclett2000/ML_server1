import numpy as np
import tensorflow as tf
from tensorflow import keras

def prediction(list, numberToPredict):
    # TODO
    #  training ratio; will determine the size of the training model vs testing model
    #  we'll do some weird multiplication

    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    x = np.array(list[0:4], dtype=float)
    y = np.array(list[5:-1], dtype=float)

    model.fit(x, y, epochs=500, verbose=0)
    predicted_val = str(model.predict([numberToPredict])[0][0])

    print("\nList Data:", list)
    print("Predicted Value:", predicted_val)

    return predicted_val