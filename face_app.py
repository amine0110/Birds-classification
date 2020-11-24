from tkinter import *
from PIL import Image as image
from PIL import ImageTk
from tkinter import filedialog
from load_image import predict






# This functions will control the hover color in the upload button
def on_enter(bg):
    button['background'] = bg

def on_leave(bg):
    button['activebackground'] = bg

# This function will clear all the the item in the frame (in this case it will delete the image displayed)
def clear():
    for item in zone_image.winfo_children():
        item.destroy()

def clear_result():
    for item in result_zone.winfo_children():
        item.destroy()

def message(operation):
    if operation == 0
        L_message.config(text="You can predict now")
        
        

def open_pic():
    
    global image_printed
    global path_image

    path_image = None

    path_image = filedialog.askopenfilename(initialdir = '/home/pycad/Documents/Project/Projet oiseaux/New images',
                title = "Select file",
                filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    # After that we read the put of the image that we want to predict we need to check if the path is true
    if path_image:
        clear()
        
        image_chosen = image.open(path_image)
        image_chosen = image_chosen.resize((300,300), image.ANTIALIAS)
        image_printed = ImageTk.PhotoImage(image=image_chosen)

        image_in_frame = Label(zone_image, image=image_chosen)
        image_in_frame.pack()
        message(0)


def search():
    if path_image:
        p = predict(path_image)[0]
        proba = predict(path_image)[1]
        m = "Your bird is: " + p + "\n" +"twith a proba of: " + str(proba * 100) + "%"
        L_message.config(text=m)


if __name__ == "__main__":
    

    # The configuration of our application

    bg = '#002929'                      # The unique background color for all the items in the application
    root = Tk()                         # Here we create the empty application
    root.geometry("500x700")            # Here we give the initial values for the dimensions
    root.title('WHAT IS YOUR BIRD!')    # Her we give the title of the app
    root.configure(bg=bg)               # Here we gived the background color to our application background
    root.resizable(width=0, height=0)   # Here we blocked the the dimensions so that we can't change it after

    # We will use this logo as a button to open the images for the prediction
    logo = PhotoImage(file='logo_s.png') 

    # Here we have a title inside the app
    title = Label(root, 
                text="We will tell you your bird's name", 
                font="agencyFB 20 bold", 
                bg=bg, 
                fg="white") 

    title.pack(pady=(10,0))

    # This is the button to choose the images
    button = Button(root, 
                image=logo, 
                bg=bg, 
                borderwidth=0, 
                command=open_pic) 

    button.pack(pady=(20, 0))
    button.bind("<Enter>", on_enter(bg))
    button.bind("<Leave>", on_leave(bg))

    # This frame is for the image
    zone_image = Frame(root, width=300, height=300, bg=bg)
    zone_image.pack(pady=(30,0))
    zone_image.propagate(0)

    # This frame for displaying the messages
    result_zone = Frame(root, width=300, height=50, bg=bg)
    result_zone.pack(pady=(30,0))

    
    global L_message
    L_message = Label(result_zone, 
                text="Choose your image", 
                bg=bg, 
                font="none 15 bold")

    L_message.pack()


    # Prediction button
    predict_b = Button(root, 
                text="PREDICT", 
                font="agencyFB 25 bold", 
                borderwidth=0, 
                width=10, 
                command=search)

    predict_b.pack(pady=(40,0))


    root.mainloop()
