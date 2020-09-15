class Questions():
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

question_1 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_2 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_3 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_4 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_5 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_6 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_7 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_8 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")
question_9 = Questions("The new code will establish for the first time a clear pecking order in our streets, with different groups of road users taking different places in a hierarchy. Which shows the correct order - from highest priority to lowest?", "3")

answers = {

    "answer_1": "A",
    "answer_2": "3",
    "answer_3": "3",
    "answer_4": "3",
    "answer_5": "3",
    "answer_6": "3",
    "answer_7": "3",
    "answer_8": "3",
    "answer_9": "3"

}

print(answers)





for i in range(9):

    user = input("What is the correct order? Input 1, 2 or 3 as your answer ")
    if user == answer_[i]:
        print("Correct")
    else:
        print("Incorrect")

