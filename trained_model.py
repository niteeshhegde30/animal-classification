#Import the necessary packages, functions and library
from tensorflow.lite.python.interpreter import Interpreter
import numpy as np
import cv2



#dictionary to translate the label to respective animal name
translate = {"cane": "dog", "cavallo": "horse", "elefante": "elephant", 
"farfalla": "butterfly", "gallina": "chicken", "gatto": "cat", 
"mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel", "dog": "cane",
"cavallo": "horse", "elephant" : "elefante", "butterfly": "farfalla",
"chicken": "gallina", "cat": "gatto", "cow": "mucca", "spider": "ragno",
"squirrel": "scoiattolo"}

#label of the trained species
LABELS = ['cane', 'cavallo', 'elefante', 'gatto', 'mucca', 'pecora']



#deserialise the saved model and make it ready to use to predict 
interpreter = Interpreter(model_path="animal_classification/animall_person_other_v2_fine_tuned.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



#function to get the name of the saved image sent using api or uploaded in streamlit webapp
#and to predict and return the name of the animal in the image 
def predict_the_image(img_name):
    img = cv2.imread(img_name)
    img = cv2.resize(img, (100,100), cv2.INTER_AREA)
    img = np.expand_dims((img)/255, axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print(output_data)

    value = np.argmax(output_data)
    # print(translate.get(LABELS[value]))
    return(translate.get(LABELS[value]))




