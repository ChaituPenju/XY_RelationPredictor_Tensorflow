
# Import required dependenciesw
import tensorflow as tf
import numpy as np

# Check if the above are imported correctly.
print('Tensorflow version is {}'.format(tf.__version__))
print('Numpy Version is {}'.format(np.__version__))


# Passing input(x) and output(y) in form of y = 2x-1
npX = np.array([1, 3, 4, 6, 8, 2, 9, 5], dtype=float)
npY = np.array([1, 5, 7, 11, 15, 3, 17, 9], dtype=float)

# Define a layer with 1 unit and 1 input shape
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
# Define the model
model = tf.keras.models.Sequential([
    layer0
])


# Compile the model with loss, optimizer and metrics
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1), metrics=['mean_squared_error'])
# Fit the model with features(input), labels(output) and epochs
model.fit(npX, npY, epochs=500, verbose=False)


# Check if model is predicting correctly
model.predict([12.0])

# Below code (line 33 to 37) is to generate a .tflite model file
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('predict_xy_model.tflite', 'wb') as f:
    f.write(tflite_model)
