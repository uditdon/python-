from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import matplotlib.pyplot as plt

from MySQL import Save_Data_MySql

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

from backend import *

BACKGROUNG = "#f0ddd5"
FRAMEBG = "#62a7ff"
FRAMEFG= "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg = BACKGROUNG)



#analysis
def analysis():
    global prediction
    name = Name.get()
    DI=Date.get()
    today= datetime.date.today()
    A=today.year-Dob.get()

    try:
       B = selection()
    except:
       messagebox.showerror("missing", "Please select gender!!")
       return

    try:
       F = selection2()
    except:
       messagebox.showerror("missing", "Please select fbs!!")
       return
    #
    try:
       I = selection3()
    except:
       messagebox.showerror("missing", "Please select exang !!")
       return


    try:
        C = selection4()
    except:
        messagebox.showerror("missing", "Please select CP!!")
        return

    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restecg!!")
        return

    try:
        K = selection5()
    except:
        messagebox.showerror("missing", "Please select slope!!")
        return
    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca !!")
        return
    try:
        M = int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal!!")
        return
    try:
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = int(oldpeak.get())
    except:
        messagebox.showerror("missing", "Few missing data entries!!")
        return

    print("A is age:" ,A)
    print("B is gender :", B)
    print("C is cp:", C)
    print("D is trestbps:", D)
    print("E is chol", E)
    print("F is fbs:",F)
    print("g is restcg:",G)
    print("H is thalach:" ,H)
    print("I is Exang:", I)
    print("J is oldpeak:" ,J)
    print("K is slop:" ,K)
    print("L is ca:",L)
    print("M is thal:",M)

    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex", "fbs", "exang"], [B, F, I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)
    canvas._tkcanvas.place(width = 255, height=255,x=600 , y=240)

    f2 = Figure(figsize=(5, 5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age", "trestbps", "chol", "thalach"], [A, D, E, H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget() .pack(side=tk.BOTTOM, fill =tk.BOTH, expand=True)
    canvas2._tkcanvas.place(width=255, height=255, x=860, y = 240)

    f3 = Figure(figsize=(5, 5), dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak", "resticg", "cp"], [J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget() .pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=255, height=255, x=600, y = 470)


    ####fourth graph
    f4 = Figure(figsize=(5, 5), dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope", "ca", "thal"], [K, L, M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget() .pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas4._tkcanvas.place(width=255, height=255, x=860, y = 470)

    input_data = (A, B, C, D, E, F, G, H, I, J, K, L, M)
    input_data_as_numpy_array = np.asanyarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshape= input_data_as_numpy_array.reshape (1, -1)
    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0] == 0):
        print("The Person does not havea Heart disease")
        report.config(text=f"Report: {0}", fg="#8dc63f")
        report1.config(text=f" (name], you do not have a heart disease")
    else:
        print("The Person has Heart disease")
        report.config(text=f"Report: (1)", fg="Hed1c24")
        report1.config(text=f" (name), you have a heart disease")





#info window
def info():


    icon_nwindow = Toplevel(root)
    icon_nwindow.title("info")
    icon_nwindow.geometry("700x600+400+100")

    icon_photo = PhotoImage(file="Images/info.png")
    icon_nwindow.iconphoto(False, icon_photo)

    Label(icon_nwindow, text="information related  to dataset", font="robot 19 bold").pack(padx=20, pady=20)

    Label(icon_nwindow, text="age - age in years", font="arial 11").place(x=20, y=100)
    Label(icon_nwindow, text="sex - (1-male; 0 - female)", font="arial 11").place(x=20, y=130)
    Label(icon_nwindow,
          text="cp = chest pain type (0 - Typical Angina ; 1 - Atypical Angina ;2- Non- anginal pain ; 3 = Asymtomatic)",
          font="arial 11").place(x=20, y=160)
    Label(icon_nwindow, text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",
          font="arial 11").place(x=20, y=190)
    Label(icon_nwindow, text="chol - serum cholestroral in mg/dl", font="arial 11").place(x=20, y=220)
    Label(icon_nwindow, text="fbs = Fasting blood sugar >120 mg/dl( 1=true ; 0 = false)", font="arial 11").place(x=20,
                                                                                                                 y=250)
    Label(icon_nwindow,
          text="restecg - resting elesctrocardiographic results (0-normal ; 1 = having ST - T ; 2 = hypertrophy)",
          font="arial 11").place(x=20, y=280)
    Label(icon_nwindow, text="thalach - maximum heart rate achieved", font="arial 11").place(x=20, y=310)
    Label(icon_nwindow, text="exang - excersie induced angina(1-yes; 0= no)", font="arial 11").place(x=20, y=340)
    Label(icon_nwindow, text="oldpeak - ST depression induced by exercise relative to rest ", font="arial 11").place(
        x=20, y=370)
    Label(icon_nwindow,
          text="slope - the slope of peak exercise ST segment (0= unslopping ;1 = flat ; 2= downslopping) ",
          font="arial 11").place(x=20, y=400)
    Label(icon_nwindow, text="ca - number ofmajor vessels (0-3) colored by floirosopy", font="arial 11").place(x=20,
                                                                                                               y=430)
    Label(icon_nwindow, text="thal - 0 = normal; 1= fixed defcet ; 2= reversable defect ", font="arial 11").place(x=20,
                                                                                                                  y=460)

    icon_nwindow.mainloop()


def logout ():
    root.destroy()


#clesr
def Clear():
    Name.get("")
    Dob.get("")
    trestbps.get("")
    chol.get("")
    thalach.get("")
    oldpeak.get("")


#saveee

def Save():
   B2=Name.get ()
   C2=Date.get ()
   D2=Dob.get ()



   today = datetime.date.today ()
   E2=today.year-Dob.get ()


   try:
      F2=selection()
   except:
      messagebox.showerror ("Mission Data", "Please select Gender!")

   try:
       J2 =selection2()
   except:
       messagebox.showerror("Mission Data", "Please select fbs!")

   try:
       M2 = selection3()
   except:
       messagebox.showerror("Mission Data", "Please select Exang!")
   try:
       G2 = selection4()
   except:
        messagebox.showerror("Mission Data", "Please select cp!")
   try :
        K2 = restecg_combobox.get()
   except:
       messagebox.showerror("Mission Data", "Please select restecg!")

   try:
       O2 = selection5()
   except:
       messagebox.showerror("Mission Data", "Please select slope!")

   try:
        P2 = restecg_combobox.get()
   except:
        messagebox.showerror("Mission Data", "Please select restecg!")

   try:
        Q2 = thal_combobox.get()
   except:
        messagebox.showerror("Mission Data", "Please select thal!")

   H2 = trestbps.get()
   I2 = chol.get()
   L2 = thalach.get()
   N2 = float(oldpeak.get())
   print(B2)
   print(C2)
   print(D2)
   print(E2)
   print(F2)
   print(G2)
   print(H2)
   print(I2)
   print(J2)
   print(K2)
   print(L2)
   print(M2)
   print(N2)
   print(O2)
   print(P2)
   print(Q2)

   # Save_Data_MySql(B2,C2, int (D2), int(E2), int(F2), int(G2), int (H2), int (I2), int(J2), int(K2), int(L2), int (M2), float (N2), int(O2),int(P2) , int(Q2), int(prediction[0]))
   # Clear()
   #
   # root.destroy()
   # os.system("main.py")

#-------------------------------------------------
#icon1
image_icon=PhotoImage(file = "Images/icon.png")
root.iconphoto(False, image_icon )


#
logo = PhotoImage(file="Images/header.png")
my_image= Label(image=logo , bg = BACKGROUNG)
my_image.place(x=0,y=0)


Heading_ebtry= Frame(root , width = 800, height = 190 , bg ="#df2d4b" )
Heading_ebtry.place(x=600 , y=20)
#
#
# register= Label(Heading_ebtry, text="Registration No." , font= ("ariel", 13), bg ="#df24db" , fg = FRAMEFG)
# register.place(x=30,y=0)
#


Label (Heading_ebtry, text="Registration No. ", font="arial 13", bg="#df2d4b", fg=FRAMEFG).place(x=20,y=0)
Label (Heading_ebtry, text="Date", font="arial 13", bg= "#df2d4b" , fg=FRAMEFG) .place(x=430, y=0)
Label (Heading_ebtry, text="Patient Name", font="arial 13", bg="#df2d4b", fg=FRAMEFG).place(x=20, y=90)
Label (Heading_ebtry, text="Birth Year", font="arial 13", bg="#df2d4b" , fg=FRAMEFG) .place(x=430, y=90)



# Label(Heading_ebtry, text="Date" , font= ("ariel", 13), bg ="#df24db" , fg = FRAMEFG).place(x=30,y=0).place(x=30,y=2)
#
# Label(Heading_ebtry, text="PatientName" , font= ("ariel", 13), bg ="#df24db" , fg = FRAMEFG).place(x=30,y=0).place(x=30,y=90)
#
# #

# birthyear= Label(Heading_ebtry, text="Birth Year" , font= ("ariel", 13), bg ="#df24db" , fg = FRAMEFG).place(x=30,y=0)
# birthyear.place(x=30,y=90)

Entry_image1= PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2=PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(Heading_ebtry, image=Entry_image1, bg="#df2d4b").place(x=20,y=30)
Label(Heading_ebtry, image=Entry_image1, bg="#df2d4b").place(x=430,y=30)

Label(Heading_ebtry, image=Entry_image2, bg="#df2d4b").place(x=20,y=120)
Label(Heading_ebtry, image=Entry_image2, bg="#df2d4b").place(x=430,y=120)

Registration= IntVar()
reg_entry= Entry(Heading_ebtry, textvariable= Registration,  width = 30 ,font=("ariel" , 15 ) ,bg= "#0e5363" , fg="white", bd=0 , highlightthickness=0)
reg_entry.place(x=30,y =45)


Date = StringVar()
today= date.today()
di= today.strftime("%d/%m/%Y")
data_entry =  Entry(Heading_ebtry, textvariable= Date,  width = 30 ,font=("ariel" , 15 ) ,bg= "#0e5363" , fg="white", bd=0,highlightthickness=0)
data_entry.place(x=450, y=45)
Date.set(di)

Name= StringVar()
name_entry=  Entry(Heading_ebtry, textvariable= Name,  width = 30 ,font=("ariel" , 15 ) ,bg= "#ededed" , fg="#222222", bd=0 ,highlightthickness=0)
name_entry.place(x=30 , y= 135)


Dob=IntVar()
dob_entry = Entry(Heading_ebtry, textvariable= Dob,  width = 30 ,font=("ariel" , 15 ) ,bg= "#ededed" , fg="#222222", bd=0 , highlightthickness=0)
dob_entry.place(x=450 , y = 135)



#
Detail_entry = Frame(root , width=490 , height = 260 , bg= "#dbe0e3")
Detail_entry.place(x=30,y=450)


Label(Detail_entry, text = "sex : " , font= "ariel 13", bg=FRAMEBG ,fg =FRAMEFG ).place(x=10,y=10)
Label (Detail_entry, text="fbs:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG).place (x=180, y=10)
Label (Detail_entry, text="exang:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) . place (x=335, y=10)





def selection():
    if gen.get() == 1:
       Gender = 1
       return (Gender)
       print(Gender)

    elif gen.get() == 2:
       Gender = 0
       return (Gender)
       print(Gender)

    else:
        print(Gender)


def selection2():
    if fbs.get() == 1:
        Fbs = 1
        return (Fbs)
        print(Fbs)

    elif fbs.get() == 2:
        Fbs = 0
        return (Fbs)
        print(Fbs)

    else:
        print(Fbs)


def selection3():
    if exang.get() == 1:
        Exang = 1
        return (Exang)
        print(Exang)

    elif exang.get() == 2:
        Exang = 0
        return (Exang)
        print(Exang)

    else:
        print(Exang)


gen = IntVar()
R1 = Radiobutton (Detail_entry, text= 'Male', variable=gen, value=1 ,bg= "WHITE", fg="#222222", command = selection)
R2 = Radiobutton (Detail_entry, text="Female", variable=gen, value=2 ,bg= "white" ,fg="#222222",command = selection)
R1.place (x=43, y=10)
R2.place (x=95, y=10)

fbs = IntVar ()
R3 = Radiobutton (Detail_entry, text='True', variable=fbs, value=1,bg= "white" ,fg="#222222", command = selection2)
R4 = Radiobutton (Detail_entry, text= "False", variable=fbs, value=2 ,bg= "white" ,fg="#222222" ,command = selection2)
R3 .place (x=213,y=10)
R4.place (x=268, y=10)


exang = IntVar()
R5 = Radiobutton (Detail_entry, text= 'Yes', variable=exang, value=1,bg= "white" ,fg="#222222",command = selection3)
R6 = Radiobutton (Detail_entry, text="No", variable=exang, value=2 ,bg= "white" ,fg="#222222", command = selection3)
R5.place (x=387,y=10)
R6.place (x=435,y=10)



Label (Detail_entry, text="cp:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) . place(x=10, y=50)
Label (Detail_entry, text="restecg", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) .place (x=10, y=90)
Label (Detail_entry, text="slope:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) .place(x=10, y=130)
Label(Detail_entry, text="ca:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) .place (x=10, y=170)
Label(Detail_entry, text="thal:", font="arial 13", bg=FRAMEBG, fg=FRAMEFG) .place (x=10, y=210)

def selection4():

    input = cp_combobox.get()
    if input == " 0 = Typical Angina":
        return (0)
    elif input == "1 = Atypical Angina":
        return (1)
    elif input == "2 = Non-Anginal pain":
        return (2)
    elif input == "3 = Asymptomatic":
        return (3)
    else:
        print(Exang)



def selection5():

    input = slope_combobox.get()
    if input == " 0 = Upslopping":
        return (0)
    elif input == "1 = Flat":
        return (1)
    elif input == "2 = Downslopping":
        return (2)
    else:
        print(Exang)


cp_combobox=Combobox (Detail_entry, values= ['0 = Typical Angina', '1 = Atypical Angina' , '2 = Non-Anginal pain', '3 = Asymptomatic'], font="arial 12", state="r" ,width=15)
restecg_combobox=Combobox(Detail_entry, values=['0','1','2'],font="arial 12", state="r" ,width=15)
slope_combobox=Combobox (Detail_entry, values=['0 = Upslopping','1 = Flat', '2 = Downslopping'], font="arial 12", state="p",width=15)
ca_combobox=Combobox (Detail_entry, values=['0','1','2','3','4'], font="arial 12", state="r" ,width=15)
thal_combobox=Combobox (Detail_entry, values=['0','1','2','3'], font="arial 12", state="r" ,width=15)

cp_combobox. place (x=50, y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place (x=70, y=130)
ca_combobox.place (x=50, y=170)
thal_combobox.place (x=50, y=210)



Label(Detail_entry, text="Smoking:", font="arial 13",width=7,bg="#dbe0e3",fg="black") .place (x=240, y=50)

Label(Detail_entry, text="trestbps:", font="arial 13" ,width=7, bg=FRAMEBG, fg=FRAMEFG) . place (x=240, y=90)

Label(Detail_entry, text="chol:", font="arial 13", width=7, bg=FRAMEBG, fg=FRAMEFG) .place (x=240, y=130)

Label(Detail_entry, text="thalach:", font="arial 13" ,width=7 ,bg=FRAMEBG, fg=FRAMEFG) .place (x=240, y=170)

Label(Detail_entry, text="oldpeak:", font="arial 13", width=7 ,bg=FRAMEBG, fg=FRAMEFG) .place (x=240, y=210)

trestbps=StringVar()
chol=StringVar ()
thalach=StringVar ()
oldpeak=StringVar ()

trestbps_entry = Entry (Detail_entry,textvariable=trestbps,width=10, font="arial 15",bg="#ededed", fg="#222222", bd=0)
chol_entry = Entry (Detail_entry, textvariable=chol,width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
thalach_entry = Entry (Detail_entry, textvariable=thalach, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
oldpeak_entry = Entry (Detail_entry, textvariable=oldpeak,width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
trestbps_entry.place (x=320, y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place (x=320, y=210)

#report
square_report_image = PhotoImage(file="Images/Report.png")
report_background= Label(image=square_report_image, bg=BACKGROUNG)
report_background .place (x=1120, y=340)
report=Label(root, font="arial 25 bold",bg="white" ,fg="#8dc63f")
report.place(x=1170,y=550)
report1=Label (root, font="arial 10 bold", bg="white")
report1.place (x=1130, y=610)

#graph
graph_image=PhotoImage (file="Images/graph.png")
Label (image=graph_image) .place (x=600, y=270)
Label(image=graph_image) .place(x=860, y=270)
Label (image=graph_image) . place (x=600, y=500)
Label (image=graph_image) .place(x=860, y=500)

#analysis button
analysis_button=PhotoImage (file="Images/Analysis.png")
Button (root, image=analysis_button, bd=0, bg="#f0ddd5", cursor= 'hand2' , highlightthickness=0, command=analysis) .place(x=1130, y=240)

#info Button
info_button=PhotoImage (file="Images/info.png")
Button (root, image=info_button, bd=0, bg=BACKGROUNG, cursor='hand2',highlightthickness=0 , command=info) .place(x=10, y=240)

#save button ＃＃＃＃＃
save_button=PhotoImage (file="Images/save.png")
Button(root, image=save_button, bd=0, bg=BACKGROUNG, cursor= 'hand2',highlightthickness=0) .place (x=1370, y=240)

#smoking
button_mode=True
choice="smoking"
def changemode() :
   global button_mode
   global choice

   if button_mode:
        choice="non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode=False
   else:
        choice="smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode=True

   print(choice)


smoking_icon=PhotoImage (file="Images/smoker.png")
non_smoking_icon=PhotoImage(file="Images/non-smoker.png")
mode=Button(root, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2", command=changemode)
mode.place (x=350, y=495)


#logout
logout_icon=PhotoImage (file="Images/logout.png")
logout_button=Button(root, image=logout_icon, bg="#df2d4b", cursor="hand2", bd=0, highlightthickness=0 ,command = logout)
logout_button.place(x=1390, y=60)



root.mainloop()



