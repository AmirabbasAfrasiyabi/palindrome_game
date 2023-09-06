
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root =tk. Tk()

root.title("Palidrome" )
root.geometry("450x100")
root.config(bg = "#C7E3EF")
root.resizable(width=False ,height= False)

#frame

Frame_up = Frame(root , width= 450 , height= 60 ,  bg="#DFB2F4")
Frame_up.grid (row=0 , column= 0 ,padx= 1 , pady= 1)

Frame_down = Frame(root , width= 450 , height= 40 ,  bg="#C7E3EF")
Frame_down.grid (row=1 , column= 0 ,padx= 1 , pady= 1)


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

def check_palindrome():
    input_text = entry.get()
    if is_palindrome(input_text):
        result = "It's a palindrome!"
    else:
        result = "It's not a palindrome."
    messagebox.showinfo("Palindrome Check", result)


# # Create and position widgets
Lable = tk.Label(Frame_up , text= " enter your text:" , height= 1  , width= 15,  font= ("Arial 10") , background="#C7E3EF" , foreground= "#27353B" )
Lable.place(x=20 , y=20)
entry = tk.Entry(Frame_up , width= 30 , justify= "left" , highlightthickness=1 , relief="solid"  )
entry.place( x=200 ,y = 20)

check_button = tk.Button(Frame_down, text="Check", command=check_palindrome , height= 1 , width=10 , font= ("Arial 10 ") , background="#DFB2F4" )
check_button.place(x = 300 , y= 5)

exit_button = tk.Button(Frame_down, text="Exit", command=check_palindrome , height= 1 , width=10 , font= ("Arial 10 ") , background="#DFB2F4")
exit_button.place( x = 50 , y = 5)

# Start the GUI event loop
root.mainloop()











