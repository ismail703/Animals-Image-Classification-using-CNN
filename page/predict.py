import os
import numpy as np
import tensorflow as tf
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image

def predict_marine(image):
    model_path = os.path.join(settings.MODELS, "Marine_Animals_ResNet101_Tuned_Model.h5")
    loaded_model = load_model(model_path)

           
    image = load_img(image, target_size=(224, 224))
    image_array = img_to_array(image) 
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = tf.keras.applications.resnet50.preprocess_input(image_array)

    result = loaded_model.predict(processed_image)

    classes = [
        "clam", "crab", "dolphin", "eel", "fish", "jellyfish", "lobster",
        "octopus", "otter", "puffer", "sea Horse", "sea Ray", "sea Turtle",
        "sea Urchin", "seal", "shark", "shrimp", "squid", "starfish", "whale"
    ]
        
    predicted_class = classes[np.argmax(result)]

    return predicted_class

def predict_replite(image):
    model_path = os.path.join(settings.MODELS, "Reptiles_and_Amphibians_ResNet101_Tuned_Model.h5")
    loaded_model = load_model(model_path)
           
    image = load_img(image, target_size=(224, 224))
    image_array = img_to_array(image) 
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = tf.keras.applications.resnet50.preprocess_input(image_array)

    result = loaded_model.predict(processed_image)

    classes = ["Chameleon", "Crocodile", "Frog", "Gecko", "Iguana", "Kumodo Dragon", "Salamander", "Snake", "Tuatara", "Turtle"]
    predicted_class = classes[np.argmax(result)]

    return predicted_class

def predict_bird(image):
    model_path = os.path.join(settings.MODELS, "birds_model.h5")
    loaded_model = load_model(model_path)
           
    image = load_img(image, target_size=(224, 224))
    image_array = img_to_array(image) 
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = image_array / 255.0 

    result = loaded_model.predict(processed_image)
    classes = ["CHICKEN","CROW","DOVE","DUCK","EAGLE","FLAMINGO","GULL","HAMMINGBIRD","MACAW","OSTRICH","OWL","PEACOCK","PENGUIN","TURKEY","WOODPECKER"]
    predicted_class = classes[np.argmax(result)]

    return predicted_class

def predict_wild(image):
    model_path = os.path.join(settings.MODELS, "Wild_model.h5")
    loaded_model = load_model(model_path)
           
    image = load_img(image, target_size=(224, 224))
    image_array = img_to_array(image) 
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = tf.keras.applications.resnet50.preprocess_input(image_array)

    result = loaded_model.predict(processed_image)
    classes = ['BEAR', 'BISON', 'CHEETAH', 'ELEPHANT', 'FOX', 'GAZELLE', 'GIRAFFE', 'GORILLA', 'HIPPO', 'HORSE', 'HYENA', 'KOALA', 'LEOPARD', 'LION', 'MEERKAT', 'PIG', 'PORCUPINE', 'RHINO', 'TIGER', 'WOLF', 'ZEBRA']
    predicted_class = classes[np.argmax(result)]

    return predicted_class


def predict_category(image):
    model_path = os.path.join(settings.MODELS, "Categorical_Model_Classifier.h5")
    loaded_model = load_model(model_path)

    image_path = image
    image = load_img(image, target_size=(224, 224))
    image_array = img_to_array(image) 
    image_array = np.expand_dims(image_array, axis=0)
    processed_image = tf.keras.applications.vgg16.preprocess_input(image_array)

    result = loaded_model.predict(processed_image)

    classes = ['Birds', 'Marine', 'Replite', 'Wild Animal']
    predicted_class = classes[np.argmax(result)]

    print(predicted_class)

    if predicted_class == "Marine":
        return predict_marine(image_path)
    elif predicted_class == "Replite":
        return predict_replite(image_path)
    elif predicted_class == "Birds":
        return predict_bird(image_path)
    elif predicted_class == "Wild Animal":
        return predict_wild(image_path)
    else:
        return "Unknown"
