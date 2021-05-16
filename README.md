Predict relation between input(x) and output(y) values using Tensorflow
==============================

<h3>This project is deployed locally in this Android App. <a target="_blank" href="https://github.com/ChaituPenju/XY_RelationPredictor_Tensorflow/">HERE</a>.#TensorFlow</h3>


Getting Started
------------
1. Must have python installed.
2. Must have pip, and required dependencies(tensorflow)


Project Structure
------------

    ├── README.md          
    │
    ├── predict_xy_relation.ipynb             <- A jupyter notebook file containing code to create ml model and create .tflite file
    │
    ├── predict_xy_relation.py             <- Python script of predict_xy_relation.ipynb
    │
    ├── interpret_xy_relation.ipynb          <- A jupyter notebook file containing code to test ml model(.tflite file)
    │
    ├── interpret_xy_relation.py         <- Python script of interpret_xy_relation.ipynb
    │
    ├── predict_xy_model.tflite            <- Generated local ml model(.tflite file).
    │
    ├── LICENSE   


--------


Code Snippets
------------

***Input Values***
<img src="https://raw.githubusercontent.com/ChaituPenju/XY_RelationPredictor_Tensorflow/main/screens/input_values.PNG">

***Output(predicted) Value***
<img src="https://raw.githubusercontent.com/ChaituPenju/XY_RelationPredictor_Tensorflow/main/screens/output_values.PNG">

***Testing local .tflite file via interpreter***
<img src="https://raw.githubusercontent.com/ChaituPenju/XY_RelationPredictor_Tensorflow/main/screens/input_output_test.PNG">