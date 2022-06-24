import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time


#connecting to the database

import face_recognizer

from face_recognizer import returncardno

db = mysql.connector.connect(host="127.0.0.1",user="root",passwd="1234",database="creditcardınformation")
mycur = db.cursor()


# converting list to string using iteration
def listToString(text):
    print("The formatted output is : ")
    text = ''.join(text)
    print(text)


def listToStringNew(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1



def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    creditcardno_info = creditcardno.get()
    if username_info == "":
        error()
    elif creditcardno_info == "":
        error()
    else:
        sql = "insert into creditcardınformation.usercreditcard values(%s,%s)"
        t = (username_info, creditcardno_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("300x250")
    global email
    global phonenumber
    global username
    global adress
    global month
    global year
    global cvc_code
    global creditcardno
    Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    email = StringVar()
    phonenumber = StringVar()
    username = StringVar()
    adress = StringVar()
    month = IntVar
    year = IntVar
    cvc_code = IntVar
    creditcardno = StringVar()
    Label(root1,text="").pack()
    Label(root1, text="E-mail :", font="bold").pack()
    Entry(root1, textvariable=email).pack()
    Label(root1, text="").pack()
    Label(root1, text="Phone Number :", font="bold").pack()
    Entry(root1, textvariable=phonenumber).pack()
    Label(root1, text="").pack()
    Label(root1, text="Location adress :", font="bold").pack()
    Entry(root1, textvariable=adress).pack()
    Label(root1, text="").pack()
    Label(root1,text="Name-Surname :",font="bold").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Credit Card No :").pack()
    Entry(root1, textvariable=creditcardno,show="*").pack()
    Label(root1, text="").pack()
    Label(root1, text="Month :", font="bold").pack()
    Entry(root1, textvariable=month).pack()

    Label(root1, text="Year :", font="bold").pack()
    Entry(root1, textvariable=year).pack()

    Label(root1, text="CVC :", font="bold").pack()
    Entry(root1, textvariable=cvc_code).pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="orange",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Payment Portal")
    root2.geometry("500x500")
    global username_varify
    global creditcardno_varify
    global email
    global phonenumber
    global adress
    global month
    global year
    global cvc_code
    def Capture():
        import OCR_reader
        exec(open("OCR_reader.py").read())
        text = OCR_reader.showcardno()
        print("{}".format(text))
        print(type(text))  # ['4', '3', '1', '9', '5', '3', '1', '2', '0', '2', '1', '5', '5', '1', '2', '8', '9']
        print(listToString(text))
        print(type(text))  # 43195312021551289
        text = listToStringNew(text)
        entrycard.delete(0, "end")
        entrycard.insert(0, text)

    def takeimage():
        import face_taker
        face_taker

    def facetrain():
        import face_train
        face_train


    Label(root2, text="Payment Portal", bg="bisque", fg="black", font="bold", width=300).pack()
    username_varify = StringVar()
    creditcardno_varify = StringVar()
    email = StringVar()
    phonenumber = StringVar()
    adress = StringVar()
    month = IntVar
    year = IntVar
    cvc_code = IntVar
    Label(root2, text="").pack()
    Label(root2, text="E-mail :", font="bold").pack()
    Entry(root2, textvariable=email).pack()
    Label(root2, text="").pack()
    Label(root2, text="Phone Number :", font="bold").pack()
    Entry(root2, textvariable=phonenumber).pack()
    Label(root2, text="").pack()
    Label(root2, text="Location adress :", font="bold").pack()
    Entry(root2, textvariable=adress).pack()
    Label(root2, text="").pack()
    Label(root2, text="Name-Surname :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Credit Card No :").pack()
    entrycard = tk.Entry(root2, textvariable=creditcardno_varify)
    entrycard.pack()
    Label(root2, text="Month :", font="bold").pack()
    Entry(root2, textvariable=month).pack()

    Label(root2, text="Year :", font="bold").pack()
    Entry(root2, textvariable=year).pack()

    Label(root2, text="CVC :", font="bold").pack()
    Entry(root2, textvariable=cvc_code).pack()
    Label(root2, text="").pack()
    Label(root2, text="").pack()
    Button(root2, text="Pay", bg="bisque", command=login_varify).pack()
    Label(root2, text="")
    Label(root2, text="You can scan your credit card information by clicking the button below.")
    Label(root2, text="")
    Label(root2, text="It is recommended that you do not enter information manually with the keyboard.")
    Label(root2, text="")
    Button(root2, text="Scan Credit Card", height="1", width="15", bg="bisque", font="bold", command=Capture).pack()

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()



def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="burlywood1", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="bisque", width=8, height=1, command=logg_destroy).pack()

def facerecoglogged(user_namex, cardno):
    Xname = user_namex
    Xcardno = cardno
    print("facerecoglogged crdd no is:")
    print(Xcardno)

    global logg2
    logg2 = Toplevel(root2)
    logg2.title("Welcome")
    logg2.geometry("500x500")
    Label(logg2, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg2, text="").pack()
    Label(logg2, text="To complete the shopping payment, you need to have your face scanned. Click Face Recognition button ", fg="orange", font="bold").pack()
    Label(logg2, text="").pack()
    Button(logg2, text="Face Recognition", bg="orange", width=16, height=1, command= lambda: recognition_func(Xname, Xcardno)).pack()
    Label(logg2, text="").pack()
    Button(logg2, text="Log-Out", bg="orange", width=8, height=1, command=logg_destroy).pack()



def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

def recognition_func(n, cn):
    #face_recognizer
    #exec(open('face_recognizer.py').read())
    os.system('python face_recognizer.py')
    #name = n
    cardno = cn
    #check_name = face_recognizer.returnname()
    check_cardno = face_recognizer.returncardno()
    print("check_cardno is:")
    print(check_cardno)
    print("cardno is:")
    print(cn)
    x = int(cn)
    print("x is:")
    print(x)
    y = int(check_cardno)


    if x == y:
        print("x")
        logged()
    elif x != y:
        print("Not equal")
    else:
        print("Bye")
        failed()




def login_varify():
    user_varify = username_varify.get()
    cardno_varify = creditcardno_varify.get()
    sql = "select * from creditcardınformation.usercreditcard where user_name = %s and creditcardno = %s"
    mycur.execute(sql, [(user_varify), (cardno_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            facerecoglogged((user_varify), (cardno_varify))
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    Label(root,text="Welcome to Log-In Protal",font="bold",bg="tan1",fg="orange4",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="bisque",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="bisque",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root, text="").pack()
    Label(root,text="Developed By Gizem Sener").pack()

main_screen()
root.mainloop()