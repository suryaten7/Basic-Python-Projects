import tkinter as tk
import instaloader
window=tk.Tk()
window.title("new")
window.iconbitmap("E:\PYTHON\github\Insta profile pic downloader")
window.minsize(400,400)
def new():
	mod=instaloader.Instaloader()
	a=e1.get()
	return mod.download_profile(a,profile_pic_only=True)
	
#label
label1=tk.Label(text="Enter instagram id: ")
label1.grid(column=0,row=0)
#entry
e1=tk.Entry()
e1.grid(column=1,row=0)
#button
b1=tk.Button(text="click",command=new)
b1.grid(column=1,row=2)
window.mainloop()
