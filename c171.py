from tkinter import *
from PIL import ImageTk,Image
import pytz
from datetime import datetime
import time

root=Tk()
root.title("world clock")
root.geometry("600x600")

clock_img=ImageTk.PhotoImage(Image.open("clock.jpg"))

label_ind=Label(root,text="India")
label_ind.place(relx=0.2,rely=0.05,anchor=CENTER)
label_img=Label(root)
label_img["image"]=clock_img
label_img.place(relx=0.2,rely=0.35,anchor=CENTER)
label_indtime=Label(root)
label_indtime.place(relx=0.2,rely=0.65,anchor=CENTER)


#------US-----------------------------------

label_us=Label(root,text="US")
label_us.place(relx=0.7,rely=0.05,anchor=CENTER)
label_img_us=Label(root)
label_img_us["image"]=clock_img
label_img_us.place(relx=0.7,rely=0.35,anchor=CENTER)
label_ustime=Label(root)
label_ustime.place(relx=0.7,rely=0.65,anchor=CENTER)


class India():
    def times(self):
        time_zone=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(time_zone)
        current_time=local_time.strftime("%H:%M:%S")
        label_indtime["text"]="time:"+current_time
        label_indtime.after(200,self.times)
        
class US():
    def times(self):
        time_zone=pytz.timezone("US/Central")
        local_time=datetime.now(time_zone)
        current_time=local_time.strftime("%H:%M:%S")
        label_ustime["text"]="time:"+current_time
        label_ustime.after(200,self.times)
        
obj_ind=India()
obj_us=US()
btn_ind=Button(root,text="time",command=obj_ind.times)
btn_ind.place(relx=0.2,rely=0.8,anchor=CENTER)
btn_us=Button(root,text="time",command=obj_us.times)
btn_us.place(relx=0.7,rely=0.8,anchor=CENTER)


root.mainloop()
