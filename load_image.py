import cv2
import tensorflow as tf
import os
import numpy as np

# Cette fonction nous aide pour construire la liste qui contient les noms des oiseaux.
def get_birds_names(path_to_folders):
    birds_names = os.listdir(path_to_folders)
    birds_names.sort()
    return birds_names



 
path_to_folders = '/home/pycad/Downloads/images/train'      # C'est le path pour les dossiers qui contienent les noms des oiseaux
path_to_model = '/home/pycad/Documents/Project/code/model'  # C'est le path pour le dossier qui contient le modèle


model = tf.keras.models.load_model(path_to_model)       # Dans cette ligne on a chargé le modèle

def predict(path_of_new_image):

    birds_names = get_birds_names(path_to_folders)          # On a appellé cette fonction pour remplir la liste des oiseaux
    

    image_new_size = 229                                    # On a mis les nouvelles dimenstions de l'image à 299 parce qu'on a fait l'apprentissage avec des images de 229 pixels
    img_array = cv2.imread(path_of_new_image)               # On a utilisé openCv pour ouvrir l'image parce qu'on a besoin d'une liste
    img = img_array.copy()
    img_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        # Le soucis de openCv c'est qu'il ouvre les images avec des bandes inversée (BGR) donc il faut les inverser 

    img_array = cv2.resize(img_array, (image_new_size, image_new_size)) # Cette ligne juste pour changer les dimensions de l'image avant de la traiter
    img_array = img_array.astype("float32")                 # On a converti les valeurs d'image on des floats parce que dans la prochaine étape on va les diviser par 255 donc si on n'a pas des valeurs floats on aura que des 0 et 1
    
    img_array = img_array / 255.0                           # On a fait le scalling parce que les réseaux de neurones fonctionent avec des valeurs normalisés alors il faut suivre l'apprentissage
    np_image = np.expand_dims(img_array, axis=0)            # Dans cette ligne on a ajouté un bande à notre image (c'est du au nombre d'epoch dans l'apprentissage)

    predictions = model(np_image)                           # Dans cette ligne on aura le résultat, le résultat sera un tableau des probabilités (30% oiseau A, 70% oiseau B, ...)
    predicted_class_idx = np.argmax(predictions)            # Donc pour prendre le meilleur oiseau on va prendre l'indexe de la valeur max du proba

    probability = np.max(predictions)                       # Et si on veut afficher sa probabilité on prend la valeur max directement
    predicted_class = birds_names[predicted_class_idx]      # Pour avoir le nom d'oiseau il faut prendre l'indexe est retirer l'oiseaux dans la liste des oiseaux avec le meme indexe tout simplement

    return predicted_class, probability                     # On a retourner une liste avec deux valeurs, le nom d'oiseau avec sa probabilité









    
