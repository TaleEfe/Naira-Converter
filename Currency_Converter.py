from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json

#color assignment
cor0 = "#FFFFFF" # White
cor1 = "#2E2E2E" # Black
cor2 = "#008B00" # Green


window = Tk()
window.geometry("300x320")
window.title("Nigerian Naira Converter")
window.configure(bg=cor0)
window.resizable(height= FALSE, width=FALSE)

#frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1 = combo1.get()
    currency2 = combo2.get()
    amount = value.get()
    querystring = {"from": currency1, "to": currency2, "amount": amount}

    headers = {
        "X-RapidAPI-Key": "aeedc1be3fmsh9d24984edf4ab12p1a9fffjsn3a431bedb9c9",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = "{:,.2f}".format(converted_amount)
    result["text"] = formatted
    print(formatted)

#top frame

icon = Image.open("imagess/icons8-naira-100.png")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text="Naira Converter", height=50, padx=13, pady=30, anchor=CENTER, font=("Arial 16 bold"), bg=cor2, fg=cor0)
app_name.place(x=0,y=0)

#main frame
result = Label(main, text="", width=16, height=2, relief = "solid", pady=7, anchor=CENTER, font=("Ivy 15 bold"), bg=cor0, fg=cor1)
result.place(x=50,y=10)

from_currency = ["NGN"]

From = Label(main, text="From", width=8, height=1, relief = "flat", padx=0, pady=0, anchor=NW, font=("Ivy 10"), bg=cor0, fg=cor1)
From.place(x=48, y=90)
combo1 = ttk.Combobox(main,width=8,justify=CENTER, font=("Ivy 12 bold"))
combo1["values"] = (from_currency)
combo1.place(x=50,y=115)

to_currency = ["CAD","BRL","EUR","INR","USD"]
To = Label(main, text="To", width=8, height=1, relief = "flat", padx=0, pady=0, anchor=NW, font=("Ivy 10"), bg=cor0, fg=cor1)
To.place(x=158, y=90)
combo2 = ttk.Combobox(main,width=8,justify=CENTER, font=("Ivy 12 bold"))
combo2["values"] = (to_currency)
combo2.place(x=160,y=115)

value= Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"))
value.place(x=50, y=155)

button = Button(main, text="Convert  Naira",width=19,padx=5,height=1,font="Ivy 12 bold",bg=cor2,fg=cor1, command=convert)
button.place(x=50,y=210)
window.mainloop()