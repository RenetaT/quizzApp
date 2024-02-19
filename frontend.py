from tkinter import *
class QuizApp:
    def __init__(self):
        self.root  = Tk()
        self.root.title("Math quiz")
        self.mainFrame=Frame(self.root)
        self.mainFrame.grid(row=0,column = 0)
        self.newQuestion = StringVar()
        self.newAnswer=StringVar()

    def run(self):
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        questionEntry=Entry(self.mainFrame,width=20,textvariable=self.newQuestion)
        questionEntry.grid(row = 0,column=0,padx=5,pady=5)

        answerEntry = Entry(self.mainFrame,width=20,textvariable= self.newAnswer)
        answerEntry.grid(row=0,column=1,padx=5,pady=5)

        new_question_button=Button(self.mainFrame,text="Add",command=self.addQuestion)
        new_question_button.grid(row=0,column=2,padx=5,pady=5)


    def addQuestion(self):
        question = self.newQuestion.get()
        questionLabel =Label(self.mainFrame,text=question)
        questionLabel.grid(row=1,column=0,padx=5,pady=5)

        answerEntry= Entry(self.mainFrame,width=20)
        answerEntry.grid(row=1,column=1,padx=5,pady=5)

def main():
    app=QuizApp()
    app.run()

main()