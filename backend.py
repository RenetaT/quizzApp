class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer= answer

    def getQuestion(self):
        return self.question

    def checkAnswer(self,userAnswer):
        return self.answer == userAnswer

class Quiz:
    def __init__(self):
        self.questions =[]

    def addQuestions(self,question,answer):
        newQuestion = Question(question,answer)
        self.questions.append(newQuestion)

    def removeQuestionAt(self,index):
        return self.questions[index].getQuestion()
    #the index parameter is essential for identifying which question in the list of questions to work with.
    # It allows for the flexibility of interacting with different questions within the list based on their position.

    def checkAnswerAt(self,index,):
        return self.questions[index].checkAnswer(userAnswer)

    def getNumQuestion(self):
        return len(self.questions)
