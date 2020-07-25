from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk

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
  
def ajoutPlan(msg,nomval,detailval,dateval):
    plan = {
        'lib':nomval.get(),
        'detail':detailval.get(),
        'date': dateval.get()
        }
    plans.append(plan)
    add_plan( nomval.get(),detailval.get(), dateval.get())
    
    msg.grid(row=5,column=2)

def ajouterInterface():
    clearframe2grid()
    frameajout = Frame(frame2)
    frameajout.grid(row=2,column=2, padx=100,pady=40)

    titre=Label(frame2,text=" Ajouter un plan",bg="white",fg="black",font=("Arial ", 10,"bold"),width=15)
    titre.grid(row=1,column=2, padx=200,pady=10)

    nomlib=Label(frameajout,text="plan",fg="black",font=("Times",12))
    nomval=Entry(frameajout)
    detailib=Label(frameajout,text="details",fg="black",font=("Times",12))
    detailval=Entry(frameajout)
    datelib=Label(frameajout,text="date(YYYY-MM-DD)",fg="black",font=("Times",12))
    dateval=Entry(frameajout)
    msg=Label(frameajout,text="Plan Ajoute",fg="green",font=("Verdana", 9))
    button1=Button(frameajout,text="Ajouter",bg="blue",fg="white",width=10,command=partial(ajoutPlan,msg,nomval,detailval,dateval))

    nomlib.grid(row=2,column=2, padx=20,pady=12)
    nomval.grid(row=2,column=3, padx=20,pady=12)
    detailib.grid(row=3,column=2, padx=20,pady=12)
    detailval.grid(row=3,column=3, padx=20,pady=12)
    datelib.grid(row=4,column=2, padx=20,pady=12)
    dateval.grid(row=4,column=3, padx=20,pady=5)
    
    button1.grid(row=5,column=3)


def afficherInterface():
    
    

    framelis = Frame(frame2)
    framelis.grid(row=2,column=2, padx=20)

    tree =ttk.Treeview(framelis, columns = (1,2,3), height = 10, show = "headings")
    tree.pack(side = 'left')

    tree.heading(1, text="Plan ")
    tree.heading(2, text="Detail")
    tree.heading(3, text="Date")

    tree.column(1, width = 100)
    tree.column(2, width = 300)
    tree.column(3, width = 120)

    scroll = ttk.Scrollbar(framelis, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')

    tree.configure(yscrollcommand=scroll.set)

    for val in plans:
        tree.insert('', 'end', values = (val['lib'], val['detail'], val['date']) )



    
    titre2=Label(frame2,text=" Plans",bg="white",fg="black",font=("Arial ", 10,"bold"),width=15)

    titre2.grid(row=1,column=2, padx=200)
    
   
       

def CalenderAffiche(mois,moisnom):
    plansm=[]
    sql = ("SELECT * FROM planing where MONTH(date_plan)=%s")
    cursor.execute(sql, (mois,))
    result = cursor.fetchall()
    for row in result:
        plan = {
        'lib':row[1],
        'detail':row[2],
        'date': row[3]
        }

        plansm.append(plan)

    frameliscal = Frame(frame2)
    frameliscal.grid(row=2,column=2, padx=20)
    titrelib=Label(frame2,text="plan de "+moisnom,fg="black",font=("Times",12))
    titrelib.grid(row=1,column=2, padx=20)

    tree =ttk.Treeview(frameliscal, columns = (1,2), height = 10, show = "headings")
    tree.pack(side = 'left')

    tree.heading(1, text="Plan ")
    tree.heading(2, text="Date")

    tree.column(1, width = 150)
    tree.column(2, width = 300)
    scroll = ttk.Scrollbar(frameliscal, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')

    tree.configure(yscrollcommand=scroll.set)

    for val in plansm:
        tree.insert('', 'end', values = (val['lib'], val['date']) )

    
def calenderInterface():
    clearframe2grid()
    framecal = Frame(frame2,bg="white")
    framecal.grid(row=2,column=2, padx=20)
    image = Image.open("calen.png")
    photo = ImageTk.PhotoImage(image)

    calenimg = Label(framecal,image=photo,bg="white")

    calenimg.image = photo 

    calenimg.grid(row=2,column=2, padx=20)

    calenimg2 = Label(framecal,image=photo,bg="white")

    image2 = Image.open("calen.png")
    photo2 = ImageTk.PhotoImage(image2)
    calenimg2.image = photo2 

    calenimg2.grid(row=2,column=3, padx=20)

    libjan=Button(framecal,text="Janvier 2020",fg="black",font=("Times",12),command=partial(CalenderAffiche,1,"Janvier"))
    libfeb=Button(framecal,text="Fevrier 2020",fg="black",font=("Times",12),command=partial(CalenderAffiche,2,"Fevrier"))
    libjan.grid(row=3,column=2, padx=20)
    libfeb.grid(row=3,column=3, padx=20)

 

    
def placeMenu():
    
    fenetre.geometry("800x350+500+200")
    clearfenetregrid()
    titre=Label(fenetre,text="demo ERP",fg="grey",width=30,font=("Arial ", 10,"bold"),pady=7)
    titre.grid(row=0,column=2)

    

    BT1=Button(frame1,text="Ajoutez un planning",command=ajouterInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)
    BT2=Button(frame1,text="Liste planning",command=afficherInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)
    BT3=Button(frame1,text="Calendar",command=calenderInterface,bg="black",fg="white",width=20,font=("Verdana", 9),padx=9, pady=9)


 
    BT1.grid(row=1,column=1,pady=15)
    BT2.grid(row=2,column=1,pady=15)
    BT3.grid(row=3,column=1,pady=15)
    frame1.grid(row=1,column=1,padx=5)
    frame2.grid(row=1,column=2)

def clearfenetregrid():
    list = fenetre.grid_slaves()
    for l in list:
        l.destroy()

def clearframe2grid():
    list = frame2.grid_slaves()
    for l in list:
        l.destroy()


def placetopgrid():
    titre=Label(fenetre,text="demo ERP",fg="grey",width=30,font=("Arial ", 10,"bold"),pady=7)
    titre.grid(row=0,column=1)

def placeLogin():
    placetopgrid()
    password=Label(fenetre,text="Mot de passe",fg="black",font=("Times",10))
    password.grid(row=1)
    entry_1.grid(row=1,column=1)
    
    button1=Button(fenetre,text="Connecter",command=login,bg="green",fg="white",width=15)
    button1.grid(row=2,column=1,padx=5)

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
plans=get_plans()
frame1 =Frame(fenetre, height = 100, width = 100,borderwidth=2)
frame2 =Frame(fenetre, height = 300, width = 575, bg = "WHITE", borderwidth=2,highlightbackground="black", highlightthickness=1)
frame2.grid_propagate(0)
entry_1=Entry(fenetre,show="*")
erreur=Label(fenetre,text="mot de passe incorrect",fg="red")
placeLogin()
fenetre.mainloop()


