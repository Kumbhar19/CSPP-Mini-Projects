def loadData(filename):
    f=open(filename,"r")
    text=f.read()
    text=str(text)
    return text
def parseQuestions(data):
    l=[]
    k=[]
    s=data.split("\n") 
    for i in s:
        t=i.split(":")
        k.append(t)

    for i in k:
        dict={}
        dict['question_text']=i[0]
        dict['choices']=[i for i in i[1].split(",")]
        dict['correct_option']=int(i[2])
        dict['max_marks']=int(i[3])
        dict['penalty']=int(i[4])
        l.append(dict) 
    return l 


def startQuiz(questions):
    for i in questions:
        
        while True:    
            try:  
                print(i['question_text'])
                for j in i['choices']:
                    print(j,end="        ")   
                n=int(input("Enter the choice option as 1/2/3/4:")) 
                if n==1 or n==2 or n==3 or n==4:
                    i["user_choice"]=n
                    if n== i['correct_option']:
                        i['score']=i['max_marks']
                        break
                    else: 
                        i['score']=i['penalty'] 
                        break
                      
                else:
                    print("Invalid input")
            except:
                print("invalid input")  

    return questions



def scoreReport(questions):
    for i in questions:
        if i['score']==i["max_marks"]:
            print(i["question_text"],end=" ")
            print("Correct Answer! - Marks Awarded:",i['score'])
        else:
             print(i["question_text"],end=" ")
             print("Wrong Answer! - Penalty:",i['score'])
    return questions         


def runQuiz():
    questions=parseQuestions(loadData("questions.txt") )
    
    dict=startQuiz(questions)
    g=scoreReport(dict)
    total=0
    for i in g:
        total=total+i['score']
    print("Total Score:", total)  

runQuiz()