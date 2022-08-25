#https://www.askpython.com/course/python-course-if-else-statement

#simple if statement.
from email import message
from unittest import result


def simple_if():
    value=int(input('Enter any number---> '))
    
    if (value <=5):
        print('Number is less than 5')
    

#simple if else statement.
def if_else():
    num=90
    if num>10:
        print('Number is greater than 10,','number in variable was',num)
    else:
        print('Number is less than 10')


#pass key word.
num1=100
num2=200
def pass_key_word():
    if num1 > num2:
        pass
    else:
        print('num2 is smaller')


#if statement in one line.(true or false)
value=10

def one_line():
    result=True if value == 10 else False#
    print(result)


#short form if.
Num1=40
Num2=10
#print('num1 is greater') if (Num1>Num2) else print('num2 is greater')


val1='Kelvin'
val2='Roper'

#if using operator.
def val_equal_val():
    if val1 == 'Kelvin' and val2 == 'Roper':
        print('my first name is', val1)
        print('my last name is', val2)
    else:
        print('CANDIDATE NOT FOUND')

#if inside for loop.
def in_range():
    for i in range (1,10):#range 1 to 10 not including 10.
        if i == 5:
            print('this range contains number 5')


#if statement with wile loop.
num=3
def if_while():
    while num <=10:
        print(num)
        num +=1
        if num == 5:
            #continue#this skips the print when 5 is reached.
            print('Just have reached number 5')
            
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#NESTED IF.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
num1 = 50
def nest_if():
    if num1 >10:
        print('num1 is greater than 10')
        if num1 >20:
            print('O.M.G num1 is greater than 20 aswell')
        else:
            print('But num1 is not greater than 20')
            
count=9          
#elif must come after if and before else statements.            
def if_else():
    num=count
    print(num)
    if num>10:
        print('Number is greater than 10,','number in variable was',num)
    elif num<5:
        print('number is less than 5','number in variable was',num)
    elif num==1:
        print('Spot on','number in variable was',num)
    else:
        print('Number is between 5 and 10','number in variable was',num)

if_else()

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#turnery operators....(and, or not),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
number1=2#could be enty box.get
def taxi():
    message  = 'No charge' if  number1 == 2 else 'Charge them '
    print(message)

pick_up=False
drop_off=False
up=15.50
off=16.25
both=(up+off)

#elif must come after if and before else statements.
def both_ways():
    if pick_up and drop_off:#both return True value.
        print(f"Charge is for pick-up and drop-off an extra £{both:.2f} pluss 45p per mile is needed.")
    elif drop_off:
        print(f"Drop off extra £{off:.2f}")#drop_off returns True
    elif pick_up:
        print(f'Pick up extra £{up:.2f}')#pick_up returns True
    else:
        print('Taxi is not needed')#both return False value


#elif must come after if and before else statements.
def tom():
    x = input('Enter your Name: ')
    if x == "Tim":
        print("You are great!")
    else:
        print("are well your name is not Tim")



