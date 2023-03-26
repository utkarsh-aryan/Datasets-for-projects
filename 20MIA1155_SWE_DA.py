from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
root=Tk()
root.title("Check Availability")
root.geometry("1350x700+0+0")
root.config(bg="blue")
url1 = 'https://raw.githubusercontent.com/utkarsh-aryan/Datasets-for-projects/main/E-s42MaVgAAahX_.jpeg'
response1 = requests.get(url1)
image=Image.open(BytesIO(response1.content))
backgroundimage=ImageTk.PhotoImage(image)
imagelabel1=Label(root, image=backgroundimage).place(x=0, y=0, relwidth=1, relheight=1)
url2 = 'https://raw.githubusercontent.com/utkarsh-aryan/Datasets-for-projects/main/Easy-Fish-Tacos-with-the-Best-Fish-Taco-Sauce-4.jpg'
response2 = requests.get(url2)
aboveimage=Image.open(BytesIO(response2.content))
abimage=ImageTk.PhotoImage(aboveimage)
imagelabel=Label(root, image=abimage).place(x=200, y=120, width=400, height=500)

formframe=Frame(root, bg="white")
formframe.place(x=600, y=120, width=700, height=500)

title=Label(formframe, text="Check Availability", font=("times new roman",20,"bold"),
            bg="white",fg="black").place(x=50,y=20)
C_name=Label(formframe, text="Reservation Date", font=("times new roman",15,"bold"),
            bg="white",fg="grey").place(x=50,y=100)
entry_fname=Entry(formframe, font=("times new roman",15), bg="lightgray").place(x=50, y=130, width=250)
contact=Label(formframe, text="Number of guest", font=("times new roman",15,"bold"),
            bg="white",fg="grey").place(x=50,y=180)
entry_contact=Entry(formframe, font=("times new roman",15), bg="lightgray").place(x=50, y=210, width=250)
slot=Label(formframe, text="Slot", font=("times new roman",15,"bold"),
            bg="white",fg="grey").place(x=50,y=260)
slot=ttk.Combobox(formframe, font=("Times new roman", 14), state="readonly", justify=CENTER)
slot['values']=("Select", "Pre-theatre", "Dinner", "Supper")
slot.place(x=50,y=290)
slot.current(0)

terms_chek=Checkbutton(formframe, text="I Agree The Terms & Conditions.", onvalue=1, offvalue=0, bg="white", font=("times new roman", 13, "bold")).place(x=50, y=400)
btn1=Button(formframe, text="Check", bg="green", font=("Times new roman", 15), fg="black", cursor="hand2").place(x=50, y=430, width=150)
SIGNUP=Button(formframe, text="Cancel", bg="white", font=("Times new roman", 15), fg="black", cursor="hand2").place(x=300, y=430, width=150)
title_label=Label( text="20MIA1155 Utkarsh Aryan", background="White", foreground="Black",padx=340, pady=4, font="Verdana 10 bold", borderwidth=3, relief=SUNKEN)
title_label.pack(side=BOTTOM,fill="y")
f1=Label(root,text="Restaurant Booking System", font=("times new roman", 30,"bold"),fg="white", bg="blue", bd=0)
f1.pack(side=TOP, fill="x")
root.mainloop()

