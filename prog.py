from tkinter import * 
from functools import partial
import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'demoprojet'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()




def add_plan(lib,detail,date):
    sql = ("INSERT INTO planing(libelle,detail,date_plan) VALUES ( %s,%s,%s)")
    cursor.execute(sql, (lib,detail,date))
    db.commit()
 


def get_plans():
    plans=[]
    sql = ("SELECT * FROM planing")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        plan = {
        'lib':row[1],
        'detail':row[2],
        'date': row[3]
        }

        plans.append(plan)
    return plans
  

def ajouterInterface():
    print("ajouter")

def afficherInterface():
    plans=get_plans()
    titre2=Label(frame2,text="Liste Plan",bg="green",fg="black",width=40)

    titre2.grid(row=1,column=2)
   
       



    
def calenderInterface():
    print("calender")
    
def placeMenu():
    
    fenetre.geometry("800x350+500+200")
    clearfenetregrid()
    titre=Label(fenetre,text="Gestion de planning",fg="grey",width=30,font=("Arial ", 10,"bold"),pady=7)
    titre.grid(row=0,column=2)

    

    BT1=Button(frame1,text="Ajoutez un planning",command=ajouterInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)
    BT2=Button(frame1,text="Liste planning",command=afficherInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)
    BT3=Button(frame1,text="Calendar",command=calenderInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)


 
    BT1.grid(row=1,column=1)
    BT2.grid(row=2,column=1)
    BT3.grid(row=3,column=1)
    frame1.grid(row=1,column=1)
    frame2.grid(row=1,column=2)

def clearfenetregrid():
    list = fenetre.grid_slaves()
    for l in list:
        l.destroy()


def placetopgrid():
    titre=Label(fenetre,text="Gestion de planning",fg="grey",width=30,font=("Arial ", 10,"bold"),pady=7)
    titre.grid(row=0,column=1)

def placeLogin():
    placetopgrid()
    password=Label(fenetre,text="Mot de passe",fg="black",font=("Times",10))
    password.grid(row=1)
    entry_1.grid(row=1,column=1)
    
    button1=Button(fenetre,text="Connecter",command=login,bg="green",fg="white",width=15)
    button1.grid(row=2,column=1)

def login(): 
    passwordvalue = entry_1.get()

    if(passwordvalue=="1"):
        clearfenetregrid()
        placetopgrid()
        placeMenu()
    else:
        erreur.grid(row=5,column=1)






#add_plan( 'plan 1','details de  plan 4','2020-02-13')
#get_plans()

fenetre = Tk()
fenetre.geometry("320x130+500+200")
frame1 =Frame(fenetre, height = 100, width = 100, bg = "WHITE", borderwidth=2)
frame2 =Frame(fenetre, height = 300, width = 575, bg = "WHITE", borderwidth=2,highlightbackground="black", highlightthickness=1)
entry_1=Entry(fenetre,show="*")
erreur=Label(fenetre,text="mot de passe incorrect",fg="red")
placeLogin()
fenetre.mainloop()


