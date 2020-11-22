from tkinter import *
from PIL import Image as image
from PIL import ImageTk
from tkinter import filedialog
from load_image import predict






# Cette fonction juste pour qlq modification sur le button
def on_enter(bg):
    button['background'] = bg

def on_leave(bg):
    button['activebackground'] = bg

def clear():
    for item in zone_image.winfo_children():
        item.destroy()

def clear_result():
    for item in zone_resultat.winfo_children():
        item.destroy()

def message(operation):
    if operation == 0:
        #clear_result()
        L_message.config(text="You can predict now")
        
        

def open_pic():
    
    global image_afficher
    global path_image

    path_image = None

    path_image = filedialog.askopenfilename(initialdir = '/home/pycad/Documents/Project/Projet oiseaux/New images',
                title = "Select file",
                filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    # Après qu'on a lu le path de l'image qu'on veut prédire, il faut assurer que le path n'est pas vide
    if path_image:
        clear()
        
        image_choisi = image.open(path_image)
        image_choisi = image_choisi.resize((300,300), image.ANTIALIAS)
        image_afficher = ImageTk.PhotoImage(image=image_choisi)

        image_dans_frame = Label(zone_image, image=image_afficher)
        image_dans_frame.pack()
        message(0)


def cherche():
    if path_image:
        p = predict(path_image)[0]
        proba = predict(path_image)[1]
        m = "Your bird is: " + p + "\n" +"twith a proba of: " + str(proba * 100) + "%"
        L_message.config(text=m)


if __name__ == "__main__":
    

    # La configuration de la face de notre application

    bg = '#002929'                      # La colour du background de tous les élements de notre app
    root = Tk()                         # La création d'un fenetre vide
    root.geometry("500x700")            # Initiation de longuer et largeur de l'app
    root.title('WHAT IS YOUR BIRD!')    # Pour donner un nom de l'application
    root.configure(bg=bg)               # Ici on a donné la couleur du background a notre application
    root.resizable(width=0, height=0)   # Pour bloquer toutes les redimensions

    # On va utiliser ce logo comme un bouton pour ouvrir l'image qu'on va la prédire.
    logo = PhotoImage(file='logo_s.png') 

    # Juste un petit titre au début de l'app.
    title = Label(root, 
                text="We will tell you your bird's name", 
                font="agencyFB 20 bold", 
                bg=bg, 
                fg="white") 

    title.pack(pady=(10,0))

    # C'est le bouton pour ouvrir l'image
    button = Button(root, 
                image=logo, 
                bg=bg, 
                borderwidth=0, 
                command=open_pic) 

    button.pack(pady=(20, 0))
    button.bind("<Enter>", on_enter(bg))
    button.bind("<Leave>", on_leave(bg))

    # Maintenant on a déclaré cette frame pour la mette comme zone pour les images aperçus (qu'on veut savoir leur nom).
    zone_image = Frame(root, width=300, height=300, bg=bg)
    zone_image.pack(pady=(30,0))
    zone_image.propagate(0)

    # Cette zone c'est pour mettre les messages d'erreu, d'attand et de résultat.
    zone_resultat = Frame(root, width=300, height=50, bg=bg)
    zone_resultat.pack(pady=(30,0))

    # Le message
    global L_message
    L_message = Label(zone_resultat, 
                text="Choose your image", 
                bg=bg, 
                font="none 15 bold")

    L_message.pack()


    # Bouton pour prédire
    predict_b = Button(root, 
                text="PREDICT", 
                font="agencyFB 25 bold", 
                borderwidth=0, 
                width=10, 
                command=cherche)

    predict_b.pack(pady=(40,0))


    root.mainloop()