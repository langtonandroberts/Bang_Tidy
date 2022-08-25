#https://youtu.be/OICqSuUvSUc
#https://youtu.be/HJpiAZDJrRY

#variables
f_name = 'Joe'
l_name = 'Roberts'
v ='Variable'

#dictionery
person ={1:'Joe',2:'Roberts',3:'Dictionery','deliver':'yes'}

#list
my_list =['Tom','Tit','List']

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#variable printing,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
print(f'My name is {f_name} {l_name}, this is a {v}')
#dictionery printing
print(f'My name is {person[1]} {person[2]}, this is a {person[3]}, {"charge dellivery" if person.get("deliver")== "yes" else"No delivery charge"}')
#list printing
print(f'My name is {my_list[0]} {my_list[1]}, this is a {my_list[2]}')#ref the index in list
#function colculation
print(f'Ten times eight is { 10*8 } ')#expression this will calculate and show the outcome.

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#spaceing the string of text,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
print(f'{"apple":>38}')#prints 38 caracters left aline.
print(f'{"bannana":<38}')#prints 38 caracters Right aline.
print(f'{"bannana":^38}')#prints 38 caracters Right aline.
print(f'{"orange":^38}')#prints 38 caracters center aline.

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#numbers,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
number = 0.9124325345
large_number = 96783.6457

positive_num = 1 #try the return with a negative number
neg_num = -1

print(f'{number:.2%}')# % multiplied by 100 and return 2 decimal places.
print(f'{number:.0%}')# % multiplied by 100 and return 0 decimal places.
print(f'£{number:.2f}')#(:.2f)gives 2 decimal places.
print(f'£{number:.3f}')
print(f'£{large_number:.2f}')
print(f'£{large_number:,.2f}')#commer seperated value.
print(f'{positive_num}... {neg_num}')
print(f'{positive_num}... {positive_num:+}')#to show a + in front of numbers.

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#printing as f string,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
invoice = f'{f_name} {l_name} would like to thank you for the £{large_number:,.2f} raised.'
print(invoice)

