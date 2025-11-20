from Numpy.Question import Question

question_prompts=[
    "What color are apples? \n(a)Red \n (b)Purple\n (c)Orange\n\n",
    "What color are Bananas? \n(a)Teel \n (b)Yellow\n (c)Pink\n\n",
    "What color are strawberries? \n(a) Yellow \n (b)Red \n (c)Blue\n\n"
]
questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"b")
]

#function to ask question then give score card
def run_test(questions):
    score=0
    for question in questions:
         answer=input(question.prompt)
         if answer==question.answer:
             score+=1
    print("You got"+str(score)+"/"+str(len(questions))+"correct")

run_test(questions)
