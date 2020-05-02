import requests
import pyperclip
import urllib
from urllib.request import urlopen
import PIL.Image
import PIL.ImageTk
import io

from tkinter import *

master = Tk()
master.configure(bg = "#3D5A6C")
master.iconbitmap(r'C:\Users\ghjyo\Py_Pro\runeterra\poro.ico')
master.title("LOR Card Viewer 1.0")

# Create Header
header = Label(master, text='Enter LOR card name and hit enter:', 
               font=("Lato", 14), wraplength=300, 
               justify="center", bg = "#3D5A6C", foreground="#DFF8EB")
header.pack(pady=20)

#Create Entry form
e = Entry(master, font = ("Open Sans", 16), justify ="center")
e.pack()
e.focus_set()

# Create canvas to display card
c=Canvas(master, width = 350, height = 500)

# Initialize URL opener
# class AppURLopener(urllib.request.FancyURLopener):
#     version = "Mozilla/5.0"
# opener = urllib.request.FancyURLopener({})

def callback():

    # name = e.get()
    # url = f"https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/{name}"

    # querystring = {"collectible":"1"}

    # headers = {
    #     'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com",
    #     'x-rapidapi-key': "2b7c311c98mshd1f9398161f2ab7p1ebdd8jsn29e872848476"
    #     }


    # response = requests.request("GET", url, headers=headers, params = querystring)

    # imgurl = response.json()[0]['img']
    # print(imgurl)
    card_name = e.get().lower().replace(" ", "-")
    imgurl = "http://www.runeterrafire.com/images/cards/" + card_name + ".png"
    # print(imgurl)
    # Open the url and read raw data

    raw_data = requests.get(imgurl, stream=True).content

    # Store img reference
    images = []

    # Convert raw data to open image data
    img = PIL.Image.open(io.BytesIO(raw_data))
    # img = img.resize((300, 454))
    photo = PIL.ImageTk.PhotoImage(img)

    c.delete("all")
    # Display imagehttps://art.hearthstonejson.com/v1/render/latest/enUS/512x/BT_601.png
    c.create_image(0, 0, anchor = NW, image = photo)
    master.mainloop()
    images.append(photo)

def func(event):
    callback()
master.bind('<Return>', func)

b = Button(master, text = "Get Card!", width = 10, command = callback)
b.pack(pady=(10,0))

c.pack(padx=20, pady=20)

mainloop()

