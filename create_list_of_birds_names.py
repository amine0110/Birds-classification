import os

# This function will help us to create the list of our birds using the folders of the images

birds_names = os.listdir('The path of the folder that contains the classes (folders of images)')
birds_names.sort()
print(birds_names)
