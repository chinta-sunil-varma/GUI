from tkinter import *
from pywhatkit import * #for all funtions in the project
from pyttsx3 import *  #for conversion of text into  voice
import random

#functions section




def maketop():
    if num.get()==1:    #Radio button value corresponding to open whatsappp application
        #define functions
        def click():
            num = '+91'+ent.get()  #country code of india is concatinated in advance
            message=txt.get(1.0,END)  #retriving text from the text widget
            hr,min=map(int,(ent1.get()).split(":"))  #spliting the hour:minute format entered by the user to store in variabe


            sendwhatmsg(num, message, hr, min) # this function shall do the rest of the work when above parameters are passed
        def voice():
            a = txt.get(1.0, END)  # retriving the text entred in the text box to convert into voice
            engine = init()
            engine.say(a)     # passing the retrived funtion
            engine.runAndWait()  # Master function which does our job done

        top = Toplevel(root)  #creating a top level widget
        top.title("WHATSAPP")
        top.geometry('550x400')
        top.resizable(0,0)
        top.iconbitmap('whatsapp icon')
        frm1 = Frame(top, width=500, height=35) # this frame contains welcome to whatsapp text

        frm1.pack(pady=7)
        frm1.pack_propagate(0)  #making the frm1 vunerable to pack operations

        lab1 = Label(frm1, text='Welcome to WhatsApp!', font=('ariel', 20, 'bold'))
        lab1.pack(anchor='w')

        frm2 = Frame(top, width=550, height=35, bg='green')  # this frame contains entry widgets of phone no and time
        frm2.pack(pady=(0, 7))
        frm2.grid_propagate(0)
        lab2 = Label(frm2, text='phone:', font=('ariel', 10, 'bold'))
        lab2.grid(row=0, column=0, padx=5, pady=5)

        ent = Entry(frm2)
        ent.grid(row=0, column=1, padx=5, pady=5)

        lab3 = Label(frm2, text='Time:', font=('ariel', 10, 'bold'))
        lab3.grid(row=0, column=2, padx=5, pady=5)

        ent1 = Entry(frm2)
        ent1.grid(row=0, column=3, padx=5, pady=5)

        but = Button(frm2, text='Submit', command=click)  #submit button which links the data to pywhat kit funtion
        but.grid(row=0, column=4, padx=5, pady=5)

        frm3 = Frame(top, width=550, height=250, bg='green')  # this frame contains text widget
        frm3.pack(pady=(0, 7))
        frm3.pack_propagate(0)

        scry = Scrollbar(frm3)   # creating a vertical scroll bar
        scry.pack(side=RIGHT, fill=Y)  # packing it to right side

        txt = Text(frm3, yscrollcommand=scry.set)  #making the text widget responsive to scroll(one way)
        txt.pack(fill=BOTH, expand=True)
        scry.config(command=txt.yview)  #making the scroll responsive to text(one way)

        frm4 = Frame(top, bg='green', width=550, height=50)  # this frame handles voice button
        frm4.pack()
        frm4.grid_propagate(0)

        but1 = Button(frm4, text='voice!', command=voice)
        but1.grid(row=0, column=0, padx=5, pady=12)


    elif num.get()==2:
        top_h = Toplevel(root)   # creating a top level window for the text ot handwriting converter
        top_h.title('HAND WRITING CONVERTER')
        top_h.geometry("500x500")

        # define fun
        def voice():
            n = my_text.get(1.0, END)  # (check the whatsapp code above to get a glimpse of voice module and its syntax)
            # create pyttsc3 object
            engine = init()

            voices = engine.getProperty("voices")
            engine.setProperty("voice", voices[1].id) # 1 coresponds to male voide
            # volume it may 0-1
            engine.setProperty("volume", 0.8 ) # volume range

            # rate
            engine.setProperty("rate", 120)
            # Speech
            engine.say(n)
            # run
            engine.runAndWait()

        def text():
            n = my_text.get(1.0, END) # retrive data from the text widget

            fi='hey'+str(random.randint(0,48795236))
            text_to_handwriting(n,
                                "C:\\Users\\user\\Desktop\\output\\{}.png".format(fi),
                                (10, 10, 10))  # create a folder with a name of your wish and paste the path here




        top_h.resizable(0, 0)
        # making frames
        frame1 = Frame(top_h, bg="orange", width=500, height=30)
        frame1.grid(row=0, column=0, pady=(0, 10))
        frame1.grid_propagate(0)
        frame2 = Frame(top_h, bg="white", width=500, height=320)
        frame2.grid(row=1, column=0, pady=(20, 10))
        frame2.pack_propagate(0)
        frame3 = Frame(top_h, bg="#F62817", width=500, height=150)
        frame3.grid(row=2, column=0, pady=(20, 10))
        frame3.grid_propagate(0) # making frame 3 vunerabel to grid placing system
        # scrolling
        scroll_v = Scrollbar(frame2)
        scroll_v.pack(side=RIGHT)



        # creating the text
        my_text = Text(frame2, bg="white", width=450)
        my_text.pack(fill=BOTH, expand=True)

        scroll_v.config(command=my_text.yview)
        # creating buttons
        button1 = Button(frame3, text="CONVERT", borderwidth=5, command=text)
        button1.grid(row=0, column=0, ipadx=30, padx=10, pady=10)
        button2 = Button(frame3, text="VOICE CONVERSION", borderwidth=5, command=voice)
        button2.grid(row=0, column=1, ipadx=50, padx=10, pady=10)
        # make label
        label = Label(frame1, text="ENTER YOUR TEXT BELOW", bg="orange", font=('arial', 10))
        label.pack(fill=BOTH, expand=True, padx=10, pady=10)

        top_h.mainloop()



    elif num.get()==3:
        global google_inter,img2# for dealing with images in funtion you should use only global statement
        top=Toplevel(root)
        top.title("GOOGLE SEARCH")
        top.iconbitmap("GOOGLE.ico")
        top.geometry("400x400")
        top.resizable(0,0)

        lab = Label(top, image=img2)
        lab.place(x=0, y=0, relwidth=1, relheight=1)



        # create a frame
        frame1 = Frame(top, bg="grey", width=400, height=50)
        frame1.grid(row=0, column=0, pady=(0, 10))

        #create image
        google_inter=PhotoImage(file="rsz_google.png",width=400,height=50) # setting the google image into our top level window
        label=Label(frame1,image=google_inter)
        label.grid(row=0,column=0)

        def searchengine():
            v = google.get()  # retriving the data from  the entry widtget googel
            search(v)
        google = Entry(top)
        google.grid(row=1,column=0,padx=100,pady=10)
       # top.config(bg="blue")
        google.insert(0, "SEARCH")  # inserting a defalut
        Bt = Button(top, text="Search", padx=10, pady=10,bg="#ffe3df",activebackground="white",command=searchengine).grid(row=2,column=0)

    elif num.get()==4:

        global utube_inter,img1
        top=Toplevel(root)
        top.title("YOU TUBE")   # creating top level window for the youtube
        top.iconbitmap("YOU TUBE.ico")
        top.geometry("400x400")
        top.resizable(0,0)

        lab = Label(top, image=img1)
        lab.place(x=0, y=0, relwidth=1, relheight=1)
        # create a frame
        frame1 = Frame(top, bg="white", width=400, height=50)
        frame1.pack( pady=(0, 10))

        # create image
        utube_inter = PhotoImage(file="utuberesize.png", width=400, height=50)  #inserting youtube logo
        label = Label(frame1, image=utube_inter)
        label.grid(row=0, column=0)

        def song():
            n = youtube.get() # this function will get the data from youtube entry box
            playonyt(n,use_api=True)
        youtube=Entry(top)
        youtube.insert(0,"SEARCH")  #adds default value to entry widget
        youtube.pack(padx=100,pady=10)
        bt1=Button(top,text="SEARCH",bg="#ffe3df",padx=10,pady=10,command=song).pack()


root=Tk()     # creating the root level window
root.title("Engineering Exploration")
root.geometry('700x700')
root.resizable(0,0)
root.iconbitmap("badpiggy.ico") #icon insertion

#image background
img=PhotoImage(file='MOUNTAIN.png')
lab=Label(root,image=img)
lab.place(x=0,y=0,relwidth=1,relheight=1) #setting the background image

img1=PhotoImage(file='fog.png')
img2=PhotoImage(file='mount.png')



#define title
label=Label(root,text="EE PROJECT ",bg="#F0F0F0",font="times 15")  #main title
label.grid(row=0,column=1,padx=10,pady=10)
#define radio buttons
num=IntVar() #creating instance of the intvar for radio button
num.set(1)  #setting the default button to 1 i.e whats app


radio_1=Radiobutton(root,text="WHAT'S APP",bg="#FFB88E",font=('arial',10),variable=num,value=1)  #creaing of radio buttons
radio_2=Radiobutton(root,text="TEXT TO HANDWRITING",bg="#FFB88E",font=('arial',10),variable=num,value=2)
radio_3=Radiobutton(root,text=" GOOGLE SEARCH",bg="#FFB88E",font=('arial',10),variable=num,val=3)
radio_4=Radiobutton(root,text="YOU TUBE",bg="#FFB88E",font=('arial',10),variable=num,val=4)

#pack the radio buttons
radio_1.grid(row=1,column=0,padx=10)
radio_2.grid(row=1,column=1)
radio_3.grid(row=2,column=0,pady=10,padx=10)
radio_4.grid(row=2,column=1,pady=10)
button=Button(root,text="SUBMIT",bg="#ffe3df",activebackground="white",borderwidth=5,fg="red",command=maketop)
button.grid(row=3,column=0,columnspan=2,pady=10,ipadx=40)
root.mainloop()