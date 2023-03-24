import tkinter as tk
import random
x=random.randint(10,100)
y=random.randint(10,100)

def dessincercle():
    canvas.create_oval(x+20,y+20,x-20,y-20,fill='blue')

root=tk.Tk()
root.title("mon dessin")
couleur=tk.Button(root,text="choisir une couleur")
cercle=tk.Button(root,text="cercle",bg='red',fg='black',command=dessincercle)
carré=tk.Button(root,text="carré",bg='grey',fg='black')
croix=tk.Button(root,text="crois",bg='grey',fg='black')



couleur.grid(column=1,row=0)
cercle.grid(column=0,row=1)
croix.grid(column=0,row=2)
carré.grid(column=0,row=3)
canvas=tk.Canvas(root,width=400,height=400,bg="black")
canvas.grid(column=1,row=1,rowspan=3)
root.mainloop()



