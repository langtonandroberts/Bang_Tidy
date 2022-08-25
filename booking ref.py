
# this is 1 of 6 vidioes
#https://youtu.be/KN43SilXv4E?list=PLvrGx2UE_sKQPoTKbYqksT9k-PzWGCwxx
#https://youtu.be/ovgWNOs41cU


#https://youtu.be/q5uM4VKywbA  #look at this first.
#https://youtu.be/Uh2ebFW8OYM

import csv
import random 

#you cannot save an integar to a csv file,,,you must convert to string.




with open('pet notes\\kennelbooker.csv','a',newline='') as csvfile:#shows all the content of the file.
            writer=csv.writer(csvfile)
            #print(csvfile.name)#prints name of file.
            
with open("pet notes\\kennelbooker.csv","r") as f: #(with) is a context manager,,so you do not need to close the file after you open it.
        content = f.read()# pass in a number to get that number of rows.
        print("------------this is the full list of the bookings--------------")
        print(content)#prints everything in file line by line
        print("--------------------------------------------------------")            

def copy_photo():#PHOTO'S
    with open("_.jpg","rb") as rf:#this will open a photo file and copy it.
        with open("_copy.jpg","wb") as wf:
            for line in rf:
                wf.write(line)

def searchdate():
    data=[]
    with open("pet notes\\kennelbooker.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    #print(data)#prints all data in file.
    
    lookup = input('Please enter a date in the format (YYYY-MM-DD): ')
    
    #loop through all data in column 5 assign it to a vairiable called col5
    col5 = [x[4] for x in data]
    #print is just to test all data in col5 is correct.
    print('--------------List of check in dates----------------------------------')
    print(col5)#prints all dates.
    print('--------------List of bookings for that date------------------')
    
    if lookup in col5:
        #searches through column 5 to find all instances
        #if it finds a match, the index (row) number is noted as "k"
        #data [k] prints all information on that row.
        for k in range (0, len(col5)):
            if col5[k] == lookup:
                #print("test",k)
                print(data[k])
                #results.append(k)
    else:
        print("Sorry I Have no date match!.")

def searchkennel():
    data=[]
    with open("pet notes\\kennelbooker.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    #print(data)#prints all data in file.
    
    lookup = input('Please enter a Kennel Number: ')
    lookup = lookup.lower()
    
    #loop through all data in column 4 assign it to a vairiable called col4
    col4 = [x[3] for x in data]
    print('--------------List of booked kennels----------------------------------')
    print(col4)
    print('--------------List of bookings for that kennel number------------------')
    
    if lookup in col4:
        #searches through column 4 to find all instances of the kennel number
        #if it finds a match, the index (row) number is noted as "k"
        #data [k] prints all information on that row.
        for k in range (0, len(col4)):
            if col4[k] == lookup:
                print("Kennel booked by: ", (data[k]))
                
    else:
        print("Sorry I Have no match for that Kennel Number!.")

def searchbookingref():
    data=[]
    with open("pet notes\\kennelbooker.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    #print(data)#prints all data in file.
    
    lookup = input('Please enter a ref Number: ')
    
    
    #loop through all data in column 4 assign it to a vairiable called col4
    col1 = [x[0] for x in data]
    #print is just to test all data in col4 is correct.
    print('--------------List of ref numbers----------------------------------')
    print(col1)#prints all ref numbers.
    print('--------------This is the booking for that ref------------------')
    
    if lookup in col1:
        #searches through column 4 to find all instances of the film name
        #if it finds a match, the index (row) number is noted as "k"
        #data [k] prints all information on that row.
        for k in range (0, len(col1)):
            if col1[k] == lookup:
                #print("test",k)
                print(data[k])
                #results.append(k)
    else:
        print("Sorry I Have no match for that Kennel Number!.")

def addbooking():
    bookings=[]
    data=[]#data will be the list we use to search the column where booking ref is.
    with open('pet notes\\kennelbooker.csv') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            data.append(row)
        
    booking_ref= random.randint(0,100)
    booking_ref=str(booking_ref)
    #col4=[x[3] for x in data]
    #print(col4)
    col1=[x[0] for x in data]
    #if the booking ref exists in column 1 (0) then do this.
    if booking_ref in col1:
        booking_ref=int(booking_ref)
        
        #code to make new booking ref.
        booking_ref2=random.randint(1,1000)
        new_booking_ref=booking_ref * booking_ref2
        new_booking_ref=str(new_booking_ref)
        bookings.append(new_booking_ref)

        print('The booking ref is: ',new_booking_ref)
        surname = input('Please enter your surname: ')
        forename = input('Please enter your First name: ')
        kennel = input('Please enter the Kennel Number: ').lower()
        booking_date = input('What date do you want to book from (YYYY-MM-DD): ')
        to_date = input('What date do you want to book to (YYYY-MM-DD): ')

        bookings.append(surname)
        bookings.append(forename)
        bookings.append(kennel)
        bookings.append(booking_date)
        bookings.append(to_date)
        
        print('Thank you for your booking.')

        with open('pet notes\\kennelbooker.csv','a',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(bookings)
    #if the booking ref is not in column 1 (0) continue as normal    
    else:
        print('The booking ref is: ',booking_ref)
        surname = input('Please enter your surname: ')
        forename = input('Please enter your First name: ')
        kennel = input('Please enter the Kennel Number: ').lower()
        booking_date = input('What date do you want to book from (YYYY-MM-DD): ')
        to_date = input('What date do you want to book to (YYYY-MM-DD): ')

        bookings.append(booking_ref)
        bookings.append(surname)
        bookings.append(forename)
        bookings.append(kennel)
        bookings.append(booking_date)
        bookings.append(to_date)
        
        print('Thank you for your booking.')

        with open('pet notes\\kennelbooker.csv','a',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(bookings)
    
#print('info saved to csv file.')
#Menu system
print('Welcome to this booking system!.')
print('Select an option from below to continue.')


print('Select (1) to add booking.')
print('Select (2) to search Kennal number.')
print('Select (3) to search Booking ref.')
print('Select (4) to search by Booking date.')

choice = input('Please select an option from above: ')

if choice == "1":
    addbooking()
elif choice == "2":
    searchkennel()
elif choice == "3":
    searchbookingref()
elif choice == "4":
    searchdate()    
else:
    print("Invalid entry run the program again.")



