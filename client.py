from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint




import socket			 

s = socket.socket()		 

port = 12345				

s.connect(('127.0.0.1', port)) 

welcome=str(s.recv(1024))

print (welcome[2:-1])

def candi():

        
    

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'checkbox',
            'message': 'Select toppings',
            'name': 'toppings',
            'choices': [
                
                Separator('= Your chose ='),
                {
                    'name': 'To Vote',
                    'checked': True
                },
                {
                    'name': 'Show Result'
                    
                },
                
                
            ],
            'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style=style)
    answer=answers['toppings']
    print(answer)
    return 1 if answer==['To Vote'] else 2


def candidate_vote():

        
    

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'checkbox',
            'message': 'Select toppings',
            'name': 'toppings',
            'choices': [
                
                Separator('= Candidate ='),
                {
                    'name': 'Candidate-1',
                    'checked': True
                },
                {
                    'name': 'Candidate-2'
                    
                },
                
                
            ],
            'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style=style)
    answer=answers['toppings']
    print(answer)
    return 1 if answer==['Candidate-1'] else 2




def name1():

        
    

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'What\'s your first name'
        }
    ]

    name = prompt(questions, style=style)
    name=name['first_name']
    
    return name



def password1():

        
    

    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#7CFC00 bold',
        Token.Selected: '#7CFC00',  # default
        Token.Pointer: '#7CFC00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#00FF00 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'input',
            'name': 'password',
            'message': 'Password'
        }
    ]

    password = prompt(questions, style=style)
    password=password['password']
    
    return password



name=name1()
password=password1()
e=name+"#"+password

s.send(bytes(e,"utf-8 "))

AmIAuth=s.recv(1024)
AmIAuth=str(AmIAuth)[2:-1]


while(AmIAuth!="Login"):
    print("Try again")
        
    # name=input("name  :  ")
    # password=input("password  :  ")
    # e=name+"#"+password
    name=name1()
    password=password1()
    e=name+"#"+password
    s.send(bytes(e,"utf-8 "))

    AmIAuth=s.recv(1024)
    AmIAuth=str(AmIAuth)[2:-1]



print("Login")

option=candi()
print(option)

s.send(bytes(str(option),"utf-8 "))

if(option==1):


    

    
    chose=candidate_vote()
    chose=str(chose)

    s.send(bytes(chose,"utf-8 "))


    vote=str(s.recv(1024))
    print(vote[2:-1])


else:
    s.send(bytes('result',"utf-8 "))

    result=str(s.recv(1024))
    result=result[2:-1]
    first,second=result.split("#")
    print(first,second)





