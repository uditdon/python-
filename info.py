from tkinter import *


icon_nwindow= Tk()
icon_nwindow.title("info")
icon_nwindow.geometry("700x600+400+100")

icon_photo=PhotoImage(file="Images/info.png")
icon_nwindow.iconphoto(False,icon_photo)


Label(icon_nwindow, text="information related  to dataset" , font="robot 19 bold").pack(padx=20,pady=20)

Label (icon_nwindow, text="age - age in years", font="arial 11") .place (x=20, y=100)
Label (icon_nwindow, text="sex - (1-male; 0 - female)", font="arial 11").place(x=20, y=130)
Label (icon_nwindow, text="cp = chest pain type (0 - Typical Angina ; 1 - Atypical Angina ;2- Non- anginal pain ; 3 = Asymtomatic)", font="arial 11") .place (x=20, y=160)
Label (icon_nwindow, text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)", font="arial 11") .place (x=20, y=190)
Label (icon_nwindow, text="chol - serum cholestroral in mg/dl", font="arial 11") .place (x=20, y=220)
Label (icon_nwindow, text="fbs = Fasting blood sugar >120 mg/dl( 1=true ; 0 = false)", font="arial 11"). place (x=20, y=250)
Label (icon_nwindow ,text="restecg - resting elesctrocardiographic results (0-normal ; 1 = having ST - T ; 2 = hypertrophy)", font="arial 11") .place(x=20, y=280 )
Label (icon_nwindow,text="thalach - maximum heart rate achieved", font="arial 11").place (x=20, y=310)
Label (icon_nwindow, text="exang - excersie induced angina(1-yes; 0= no)", font="arial 11").place (x=20, y=340)
Label (icon_nwindow, text="oldpeak - ST depression induced by exercise relative to rest ", font="arial 11") .place (x=20, y=370)
Label (icon_nwindow, text="slope - the slope of peak exercise ST segment (0= unslopping ;1 = flat ; 2= downslopping) ", font="arial 11"). place(x=20, y=400)
Label (icon_nwindow, text="ca - number ofmajor vessels (0-3) colored by floirosopy", font= "arial 11") .place (x=20, y=430)
Label (icon_nwindow,text="thal - 0 = normal; 1= fixed defcet ; 2= reversable defect ", font="arial 11") .place (x=20, y=460)



icon_nwindow.mainloop()