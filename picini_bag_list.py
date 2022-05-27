# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:32:52 2022

@author: dell
"""
from tkinter import*
import random
root = Tk()
root.title("Picnic Bag List")
root.geometry("800x800")
root.configure(background = "lightgreen")
List_of_items = ["Bottle" , "Tiffin" , "ID Card" , "Chocolates" , "Chips" , "Tickets" , "Hanky" ]
label_list_of_items = Label(root,text = "Listed Items : " ,bg  ="lightgreen" ,  fg = "darkgreen"  , font = 25)
label_picnic_bag_items = Label(root,bg = "lightgreen" , fg = "darkgreen" ,  font = 25)
label_list_of_items.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
label_picnic_bag_items.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

label_list_of_items["text"] = "Listed Items : " + str(List_of_items)

def picnic_list():
    length_of_list = len(List_of_items)
    random_number = random.randint(0 , length_of_list - 1)
    label_picnic_bag_items["text"] = "Put item no " + str(random_number) + " in bag"

btn = Button(root ,text = "Which item to put in bag?" , bg = "darkgreen" , fg = "yellow" , font = 25 ,command = picnic_list )
btn.place(relx = 0.5 , rely = 0.5, anchor = CENTER)   
    
    
root.mainloop()
