from tkinter import *
import json
import requests
root = Tk()
def ShowQuote():
    request = requests.get('https://zenquotes.io/api/random')
    data = json.loads(request.text)
    quote = data[0]['q']
    arthor = data[0]['a']
    if len(quote) <100 :
        siege = Label(root,text="#"*len(quote))
        Quote = Label(root,text=quote)
        Arthor = Label(root,text=arthor)
        siege.pack()
        Quote.pack()
        Arthor.pack()
def main():
    welcome = Label(root,text="Welcome to The source of insipration source of \n comprehend the path you are taking \n to get a charge consider pressing the button below ",bg="#9370DB",fg="white")
    empt = Label(root,text="\n")
    btn = Button(root,text="Impresse Me God *_*",pady=10,bg="#000080",fg="#ffefd5",command=ShowQuote)
    welcome.pack()
    empt.pack()
    btn.pack()
    root.mainloop()
main()
