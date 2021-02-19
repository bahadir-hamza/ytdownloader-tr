__author__ = "Bahadır Hamza Öztürk"
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Klasör seçin!",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        tkinter.messagebox.showinfo('Bilgi', 'İndiriliyor, Lütfen Bekleyin...')
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
           ytdError.config(text="Linki tekrar girin!",fg="red") 
    select.download(Folder_Name)
    ytdError.config(text=  "İndirme Tamamlandı!!1")




root = Tk()
root.title("Youtube indirme")
root.geometry("350x400")
root.columnconfigure(0,weight=1)


ytdLabel = Label(root,text="Url girin",font=("jost",15))
ytdLabel.grid()



ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root,text="hatamsg",fg="red",font=("jost",10))
ytdError.grid()

saveLabel = Label(root,text="dosya konumu",font=("jost",15,"bold"))
saveLabel.grid()

saveEntry = Button(root,width=10,bg="red",fg="white",text="konum seç",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="yolhata",fg="red",font=("jost",10))
locationError.grid()

ytdQuality = Label(root,text="kalite seçin",font=("jost",15))
ytdQuality.grid()

choices = ["720p","144p","Ses"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="İndir",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root,text="Bahadır Hamza Öztürk",font=("jost",15))
developerlabel.grid()





root.mainloop()
