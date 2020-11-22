import cv2
import tensorflow as tf
import os
import numpy as np

# Cette fonction nous aide pour construire la liste qui contient les noms des oiseaux.
def get_birds_names(path_to_folders):
    birds_names = os.listdir(path_to_folders)
    birds_names.sort()
    return birds_names



 
path_to_folders = 'The path where the folders that contain the birds names'      
path_to_model = 'The path where you saved your model'  


model = tf.keras.models.load_model(path_to_model)       # Here we load the model

def predict(path_of_new_image):

    birds_names = get_birds_names(path_to_folders)          # We called the function that will fill our birds list
    

    image_new_size = 229                                    # We defined new sizes for the image because we did the trainig on images with 229 pixels
    img_array = cv2.imread(path_of_new_image)               # We used openCv to read the image because we need it as an array
    img = img_array.copy()
    img_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        # The issue with openCv is that it will reverse the channel when it open the image so we need to put every channel on its place as at the training

    img_array = cv2.resize(img_array, (image_new_size, image_new_size)) # Here we gived the new dimensions to the image that we will predict
    img_array = img_array.astype("float32")                 # Here we converted the pixel values to float because in the next step we will divide it by 255 so if we will let it intger all the values will be either 0 or 1 but we want it between 0 and 1
    
    img_array = img_array / 255.0                           # Here we did the scalling as we did in the training because in the deep learning we have to use values between 0 and 1
    np_image = np.expand_dims(img_array, axis=0)            # Here we added a channel to have much channel as the training(in the training there is a new channel for the indexe of the picture entred in our case we did just 2 images)

    predictions = model(np_image)                           # As we know the prediction result will give us an array of probabilities so we will take the mas value which corespond to the right class
    predicted_class_idx = np.argmax(predictions)            # We need to take the indexe of the max value which will help us to get the bird name from the names list

    probability = np.max(predictions)                       # And here to take the probability value if we need to print it for example
    predicted_class = birds_names[predicted_class_idx]      # This line will return the name of the bird selected

    return predicted_class, probability                     # We returned an array of two values, the bird name and its probability









    
