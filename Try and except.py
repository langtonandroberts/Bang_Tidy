


#https://youtu.be/j_q6NGOwDJo?list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT

try:
    numerator = int(input("Enter a number to devide: "))
    denominator = int(input("Enter a number to devide by: "))
    result = numerator / denominator
except ZeroDivisionError:# this catches this error.
    print("You cant devide by zero.")
except ValueError:# this catches error if not number entered.
    print("Enter only numbers please.")
except Exception:# this catches every other error.
    print("Something went wrong.")
else:
    print(result)
    
    
