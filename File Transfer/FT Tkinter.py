# IMPORTING ALL REQUIRED MODULES
from tkinter import * # FOR THE GUI
from tkinter import filedialog
from turtle import width # TO OPEN OS DOCUMENT DIALOG BOX TO SELECT FILE
import FileTransfer_app # FOR THE TRANSFER OF FILES
from tkinter import messagebox # FOR THE GUI
import os # TO CONNECT TO THE DEVICE
import socket # TO GET THE IP ADDRESS,

# Defining functions
def send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("450x450")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)
    # Icon
    image_icon1 = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\send icon.png")
    window.iconphoto(False,image_icon1)
    label = Label(window,text="Select file/document category",font=("Arial",18)).pack()
    
    # Defining Commands  
    def create_connection():
        # Getting Ip Address
        while True: 
            hostname = socket.gethostname() # PC Hostname
            ip = socket.gethostbyname(hostname)
            if len(str(ip)) >= 12:
                ip_address = ip
                label = Label(root,text="CONNECTION CREATED", font=("Arial",20,"bold")).place(x=145,y=260)
                label = Label(root,text=f"IPV4 Address: {ip_address}", font=("Arial",10,"bold")).place(x=210,y=230)
                filepath = file_dir() # Gets the Absolute path of the file
                # Calling the Server connection from the FileTransfer_app Python document
                FileTransfer_app.server_connection(ip_address,filepath)
                label = Label(window,text="TRANSFER COMPLETE!", font=("Arial",20,"bold")).place(x=80,y=230)
                
            else: 
                messagebox.showinfo(title="Connection problem",message="Connect to a wireless network and Try again. Note: No data usage required")
                break
    # File Path 
    def file_dir():
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file format type",filetypes=[("all files","*.*"),("file_types","*.pdf")])
        return filename
    # Final Send and Connection creatinf button button
    button1 = Button(window,bg="#000",text="Create Connection",fg="#fefdfc",command=create_connection).place(x=165,y=200)
    window.mainloop()
def recv():
    window = Toplevel(root)
    window.title("Receive")
    window.geometry("450x450")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)
    # Icon
    image_icon2 = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\receive icon.png")
    window.iconphoto(False,image_icon2)
    # Text Box
    input_addr = Text(window,height=1,width=15, font=("Arial",16))
    input_addr.place(x=80,y=100)
    # Accept/Receive Button
    def accepted():
        ip_add = input_addr.get("1.0",END).rstrip()
        FileTransfer_app.receiver_connection(ip_add)
        label = Label(window,text="FINISHED!", font=("Arial",20,"bold")).place(x=145,y=260)
    accept_button = Button(window,text="Connect",font=("Arial",14),bg="#000",fg="#f4fdfe",command=accepted).place(x=290,y=95)
    window.mainloop()
# CREATING THE USER INTERFACE
root = Tk() 
root.title("Sharelink") # Title of the App
root.geometry("600x600") # Dimensions of the App
root.configure(bg="#f4fdfe") # White Hex color code
root.resizable(False,False)

# Icon
image_icon = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\General icon.png")
root.iconphoto(False,image_icon)
# Label
label = Label(root,text="File Transfer Application", font=("Arial",20,"bold"))
label.pack(pady=3) # Adding a padding to the Y-Axis
# Frame
frame = Frame(root,height=2,bg="#c4eedd" ,width=600).pack()
# Send buttons
send_image = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\send icon.png")
send_button = Button(root,image=send_image,bg="#f4fdfe",bd=0,command=send).place(x=100,y=100)
# Recieve buttons
recv_image = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\receive icon.png")
recv_button = Button(root, image=recv_image,bg="#f4fdfe",bd=0,command=recv).place(x=400,y=100)
# Send and Recieve Button Label
label = Label(root,text="Send",bg="#f4fdfe",font=("Arial",20,"bold")).place(x=110,y=210)
label = Label(root,text="Recieve",bg="#f4fdfe",font=("Arial",20,"bold")).place(x=400,y=210)

# Image
img = PhotoImage(file=r"C:\Users\HELLO\Documents\Programming Files\FCC Junior dev projects\File Transfer\background.png")
label = Label(root,bg="#0114fb",image=img).place(x=-2,y=300)
root.mainloop()