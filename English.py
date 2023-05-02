import requests,tkinter
window = tkinter.Tk()
window.title("WebIn")
window.geometry("400x300")
while True:
    r = requests.get('http://www.bing.com/')
    if r.status_code==200:
        TXT='Network link is fine' 
    else:
        if r.status_code==404:
            TXT='Network is not linked'
        TXT='Network link abnormality'
    labell2 = tkinter.Label(window, text="Use Microsoft Bing(http://www.bing.com/)test", fg="black",font=("宋体"),width=350,height=20)
    labell = tkinter.Label(window, text=TXT, fg="black",font=("宋体"),width=20,height=3)
    labell.pack()
    labell2.pack()
    window.mainloop()

