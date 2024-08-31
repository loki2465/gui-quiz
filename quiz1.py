from tkinter import *
from pygame import mixer

#mixer.init()

#mixer.music.load('sound.mp3')


#mixer.music.play(-1)

current_question_index = 0  # Declare current_question_index at the beginning

def select(event):
    b = event.widget
    value = b['text']

    for i in range(10):
        if value == correct_answers[i]:
            if value == correct_answers[9]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountimage)

                    # Hide the next question button
                    next_button.place_forget()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 0 pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=50)

                winLabel = Label(root2, text='You Won 2000 rupees', font=('arial', 35, 'bold'), bg='black', fg='green')
                winLabel.pack()

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black',
                                         fg='white', activebackground='black', bd=0, cursor='hand2',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                      activebackground='black', bd=0, cursor='hand2',
                                      command=close)
                closeButton.pack()

                root.mainloop()
                break

            # Show the next question button
            next_button.place(relx=0.5, rely=0.95, anchor=CENTER)
            break
    else:
        # Incorrect answer
        show_try_again_window()

#def reset_timer():
#    global timer_seconds
#    timer_seconds = 60

#def start_timer():
#    global timer_seconds
 #   timer_seconds = 60
  #  update_timer()

#def update_timer():
 #   global timer_seconds
  #  timer_label.config(text=f"Timer: {timer_seconds} s")
  #  if timer_seconds > 0:
   #     timer_seconds -= 1
    #    timer_label.after(1000, update_timer)
    #else:
    #    # Timer ran out
        show_try_again_window()

# Initialize current question index
current_question_index = 1

def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)

    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton1.config(text=' ')
        optionButton3.config(text=' ')

    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton1.config(text=' ')
        optionButton3.config(text=' ')

    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton1.config(text=' ')
        optionButton4.config(text=' ')

def show_try_again_window():
    def close():
        root.destroy()

    def tryagain():
        root1.destroy()
        questionArea.delete(1.0,END)
        questionArea.insert(END,questions[0])

        optionButton1.config(text=first_option[0])
        optionButton2.config(text=second_option[0])
        optionButton3.config(text=third_option[0])
        optionButton4.config(text=fourth_option[0])

        amountLabel.config(image=amountimage)

        # Hide the next question button
        next_button.place_forget()

    root1=Toplevel()
    root1.overrideredirect(True)
    root1.config(bg='black')
    root1.geometry('500x400+140+30')
    root1.title('You won 0 pounds')
    imgLabel=Label(root1,image=centerImage,bd=0)
    imgLabel.pack(pady=30)


    loseLabel=Label(root1,text='You Lose',font=('arial',40,'bold'),bg='black',fg='red')
    loseLabel.pack()

    tryagainButton=Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',
                          activebackground='black',bd=0,cursor='hand2'
                          ,command=tryagain)
    tryagainButton.pack()

    closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                            activebackground='black', bd=0, cursor='hand2',
                         command=close)
    closeButton.pack()


    root1.mainloop()

correct_answers=["3.1%", "Elephant", "98.6", "Agriculture", "Madhya Pradesh", "February 26",
                 "Amazon", "Amendment Bill", "Financial Week", "80th"]

questions=["1.DOB of Kishore",
           "2.Kishore red flower or not",
           "KIshore pedda ?",
           "4.Dr.M.S.Swaminathan has distinguished himself in which of the following fields?",
           "5.Which Indian state has introduced the 'Bag-less School' initiative?",
           "6.On which date did the Indian Air Force conduct the Balakot Airstrike in Pakistan?",
           "7.As of January 2024, which company holds the title of the most valuable brand in the world with a market value of $299.3 billion?",
           "8.Which one of the following Bills must be passed by each House of the Indian parliament separately by special majority?",
           "9.What event did the Reserve Bank of India observe from February 26 to March 1, 2024?",
           "10.In the global cybercrime report for 2023, what was India's ranking?"]

first_option=["3.6%", "Whistle",
              "57.7", "Agriculture",
              "Tamil Nadu", "February 14",
              "Apple", "Ordinary Bill", "National Savings Week", "34th "]

second_option=["3.1%", "Elephant",
               "72.8", "Medicine",
               "Madhya Pradesh", "February 24",
               "Amazon", "Money Bill", "Financial Week", "56th"]

third_option=["4.2%", "Flower",
              "96.5", "Astrophysics",
              "Andhra Pradesh", "February 25",
              "Google", "Finance Bill", "Youth Awareness Week", "80th"]

fourth_option=["5.1%", "Broom",
               "98.6", "Physics",
               "Telangana","February 26", "Microsoft","Amendment Bill", "Economic Festival", "102nd"]

root=Tk()
root.geometry('1270x652+0+0')
root.title('who wants to be millionaire')
root.config(bg='black')

leftframe=Frame(root,bg='black',padx=100)
leftframe.grid(row=0,column=0)

topFrame=Frame(leftframe)
topFrame.grid()

centerFrame=Frame(leftframe,bg='black',pady=100,padx=100)
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftframe)
bottomFrame.grid(row=2,column=0)

rightframe=Frame(root,pady=25,padx=300,bg='black')
rightframe.grid(row=0,column=1)

image50=PhotoImage(file='50-50.png')
image50X=PhotoImage(file='50-50-X.png')

lifeline50Button=Button(topFrame,image=image50,bg='black',bd=0,activebackground='black',width=180,height=80,
                        command=lifeline50)
lifeline50Button.grid(row=0,column=0)

centerImage=PhotoImage(file='Center.png')

logolable=Label(centerFrame,image=centerImage,bg='black',width=350,height=250)
logolable.grid(row=1,column=2)

amountimage=PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='Picture1.png')
amountimage2=PhotoImage(file='Picture2.png')
amountimage3=PhotoImage(file='Picture3.png')
amountimage4=PhotoImage(file='Picture4.png')
amountimage5=PhotoImage(file='Picture5.png')
amountimage6=PhotoImage(file='Picture6.png')
amountimage7=PhotoImage(file='Picture7.png')
amountimage8=PhotoImage(file='Picture8.png')
amountimage9=PhotoImage(file='Picture9.png')
amountimage10=PhotoImage(file='Picture10.png')

amountImages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,amountimage7,
              amountimage8,amountimage9,amountimage10]

amountLabel=Label(rightframe,image=amountimage,bg='black')
amountLabel.grid(row=0,column=0)

layoutimage=PhotoImage(file='lay.png')

layoutLabel=Label(bottomFrame,image=layoutimage,bg='black')
layoutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',12,'bold'),width=45,height=3,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])

labelA=Label(bottomFrame,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)

optionButton1=Button(bottomFrame,text=first_option[0],font=('arial',12,'bold'),bg='black',fg='white',bd=0,activebackground='black',cursor='hand2')
optionButton1.place(x=100,y=100)

labelB=Label(bottomFrame,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomFrame,text=second_option[0],font=('arial',12,'bold'),bg='black',fg='white',bd=0,activebackground='black',cursor='hand2')
optionButton2.place(x=370,y=100)

labelC=Label(bottomFrame,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=190)

optionButton3=Button(bottomFrame,text=third_option[0],font=('arial',12,'bold'),bg='black',fg='white',bd=0,activebackground='black',cursor='hand2')
optionButton3.place(x=100,y=180)

labelD=Label(bottomFrame,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)

optionButton4=Button(bottomFrame,text=fourth_option[0],font=('arial',12,'bold'),bg='black',fg='white',bd=0,activebackground='black',cursor='hand2')
optionButton4.place(x=370,y=180)

#timer_label = Label(root, text="Timer: 30 s", bg='black', fg='yellow', font=('arial', 25, 'bold'))
#timer_label.place(x=10, y=10)

optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)

def next_question():
    global current_question_index  # Declare global here
    # Reset the timer
    #reset_timer()
    # Move to the next question
    questionArea.delete(1.0, END)
    questionArea.insert(END, questions[current_question_index])
    optionButton1.config(text=first_option[current_question_index])
    optionButton2.config(text=second_option[current_question_index])
    optionButton3.config(text=third_option[current_question_index])
    optionButton4.config(text=fourth_option[current_question_index])
    amountLabel.config(image=amountImages[current_question_index-1])

    # Increment the current question index
    current_question_index += 1

    # Hide the next question button
    next_button.place_forget()

next_button = Button(root, text="Next Question", bg="yellow", fg="black", font=("Arial", 20, "bold"), command=next_question)
next_button.place(relx=0.7, rely=0.95, anchor=CENTER)

# Hide the next question button initially
next_button.place_forget()

# Start the timer
#start_timer()

root.mainloop()