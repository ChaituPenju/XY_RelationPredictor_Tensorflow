
# Import required dependencies
import tensorflow as tf
import numpy as np


# Get the interpreter object from model file path
interpreter = tf.lite.Interpreter(model_path="predict_xy_model.tflite")
# Allocate the tensors to the interpreter
interpreter.allocate_tensors()


# Initialize input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# Initialize all input parameters
input_shape = input_details[0]['shape']
input_data = np.array(([[11]]), dtype=np.float32) # For now, passing static input value 11


# Set the inputs via tensor and invoke the interpreter
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()


# Get the predicted value via output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data) # Check if it is printing value near to [[21.0]] on the console(as we are passing 11.0 as input)
