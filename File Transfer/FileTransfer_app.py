# Importing Pickle to send dictionary objects
import pickle
# Importing python-docx and PyPDF
import PyPDF2
from PyPDF2 import PdfFileWriter
import docx
# Importing sockets in order to get IP_Address
import socket
# Importing reportlab to create new PDF from Scratch
from fpdf import FPDF

def server_connection(ip_address,filedir):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating the socket server
    server_socket.bind((ip_address,9497)) # Getting reading to bind with clients
    server_socket.listen(5) # Max number of connection devices is 5
    # Reading the file to be copied
    file_dict = dict()
    path = filedir #
    filepath = (path)
    filepath = filepath.split("\\")
    index = len(filepath) - 1 # Getting the Last index in the List
    filename = filepath[index]
    file_dict["Filename"] = filename
    # ******Flow statements for type of document to be sent******
    TOD = filename.split(".") # TOD ==> Type of Document e.g .txt,.MP4,.MP4,.Docx 
    # Condition for Documents such as texts, Ms word, Excel, PDF formats
    if TOD[1].lower() == "txt":
        file = open(path)
        file_content = ""
        for line in file:
            file_content += line
        file_dict["Filecontents"] = file_content
        print(file_content)
    elif TOD[1].lower() == "pdf": # If type of document is .MP3, i.e Music:
        file_content = ""
        reader = PyPDF2.PdfFileReader(path)
        num_page = reader.numPages # Getting number of pages to loop over
        for i in range(num_page):
            page = reader.getPage(i)
            content = page.extract_text()
            file_content += content
        file_dict["Filecontents"] = file_content  # Contents of the PDF
        print(file_content)
        print("***************************************")
        file_dict["Num_Pages"] = num_page
        print(num_page)
    elif TOD[1].lower() == "docx":
        pass
    elif TOD[1].lower() == "png" or TOD.lower() == "jpeg" or TOD.lower() == "jpg": # For image formats
        file_content = b""
        file = open(path,"rb")
        for line in file:
            file_content += line
        file_dict["Filecontents"] = file_content
    while True:
        client,addr = server_socket.accept() # Accepting connections
        print("Connected with",addr)
        message = client.recv(1024).decode()
        print(f"Message from client is {message}")
        file = pickle.dumps(file_dict) # Sending the document using Pickle module
        client.send(file) # Sending content of file
        client.close() # Closing connections
        print(f"Connection with {addr} ended!") # To be removed when app is complete
        break
def receiver_connection(ip_add):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating the socket
    client.connect((ip_add,9497)) ## Issue is here when receiving
    client.send(bytes("Ready to Receive","utf-8"))
    # To store incoming dictionary object
    data = b""
    full_content = "" # To store the contents of the file
    while True:
        received_content = (client.recv(5120))
        if len(received_content) < 1:
            break
        data += received_content
    file = pickle.loads(data)
    TOD = file["Filename"].split(".")[0] # Selecting the File name except type
    TOD1 = file["Filename"].split(".")[1] # Selecting the File extention, e.g pdf,txt,docx
    
    # Duplicating filename, content of file
    if TOD1 == "txt":
        full_content += file["Filecontents"]
        filename = open(TOD+".txt", "a")
        filename.write(full_content)
        filename.close() # Closing the file
    # Converting to required document format e.g. pdf,Docx
    elif TOD1 == "pdf":
        # Writing into text document first before deleting
        full_content += file["Filecontents"]
        print(full_content)
        filename = open(TOD+".txt", "a")
        filename.write(full_content)
        filename.close() # Writing into text document complete
        # Creating the PDF page
        pdf = FPDF()
        pdf.add_page()
        # Re-Opening the File
        document = open(TOD +".txt")
        for line in document:
            pdf.set_font("Arial",size=15) # Setting characterisitcs of the page
            line_convert = line.encode("latin-1","replace").decode("latin-1")
            pdf.multi_cell(w=0,h=10,txt=line_convert,align="L") # Writing those characteristics to the page
        pdf.output(TOD + ".pdf") # Creating the file with the sent name
    elif TOD1 == "docx":
        pass
    elif TOD1.lower() == "png" or TOD1.lower() == "jpeg" or TOD1.lower() == "jpg":
        full_content = file["Filecontents"]
        filename = open(TOD+"."+TOD1,"wb")
        filename.write(full_content)
        filename.close()
    client.close() # Closing the socket connection

