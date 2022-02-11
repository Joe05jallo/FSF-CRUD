from tkinter import *
from tkcalendar import *
import mysql
from tkinter import ttk,messagebox


class FormMysql:
     def __init__(self, root):
         self.root=root
         self.root.title("Formulaire avec une base donnée")
         self.root.geometry("1900x1000")
         
         #Champs du formulaire
         frame1 = Frame(self.root, bg="teal")
         frame1.place(x=300, y=100, width=700, height=500)
         
         
         title = Label(frame1, text="formulaire", font=('time new roman', 20, 'bold'), fg="black").place(x=50, y=30)
         #prenom
         txt_prenom = Label(frame1, text='prenom', font=("time new roman", 15), bg="teal", fg="black").place(x=50, y=100)
         self.ecrir_prenom = Entry(frame1, font=("time new roman", 15), bg="white")
         self.ecrir_prenom.place(x=50, y=130, width=250)
         
                  #nom
         txt_nom = Label(frame1, text='nom', font=("time new roman", 15), bg="teal", fg="black").place(x=370, y=100)
         self.ecrir_nom = Entry(frame1, font=("time new roman", 15), bg="white")
         self.ecrir_nom.place(x=370, y=130, width=250)
         
                  #email
         txt_email = Label(frame1, text='email', font=("time new roman", 15), bg="teal", fg="black").place(x=50, y=160)
         self.ecrir_email = Entry(frame1, font=("time new roman", 15), bg="white")
         self.ecrir_email.place(x=50, y=190, width=250)
         
                  #Téléphone
         txt_Téléphone = Label(frame1, text='Téléphone', font=("time new roman", 15), bg="teal", fg="black").place(x=370, y=160)
         self.ecrir_Téléphone = Entry(frame1, font=("time new roman", 15), bg="white")
         self.ecrir_Téléphone.place(x=370, y=190, width=250)
         
         
                          #sexe
         txt_sexe = Label(frame1, text='sexe', font=("time new roman", 15), bg="teal", fg="black").place(x=50, y=220)
         self.ecrir_sexe = ttk.Combobox(frame1, font=("time new roman", 15), state='readonly')
         self.ecrir_sexe["values"]=( "Homme", "Femme")
         self.ecrir_sexe.place(x=50, y=250, width=250) 
         self.ecrir_sexe.current(0)
         
                           #nationalite
         txt_nationalite = Label(frame1, text='nationalite', font=("time new roman", 15), bg="teal", fg="black").place(x=370, y=220)
         self.ecrir_nationalite = Entry(frame1, font=("time new roman", 15), bg="white")
         self.ecrir_nationalite.place(x=370, y=250, width=250)
         
         
         bouton = Button(frame1, text="valider", font=("time new roman", 15, "bold"), bg='green', fg="black").place(x=100, y=350) 

         bouton = Button(frame1, text="annuler", font=("time new roman", 15, "bold"), bg='red', fg="black").place(x="300", y=350) 
         
         
     
root=Tk()
obj = FormMysql(root)  



       
root.mainloop()     