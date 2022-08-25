import sqlite3
from time import strftime
from tkinter import filedialog




def bookings():
    #,,,connect to database,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    conn=sqlite3.connect("practice.db")
    #,,,create a cursor.
    c=conn.cursor()
    #,,,create a bookings table.
    c.execute("""CREATE TABLE if not exists practice_bookings(
        booking_ref int,
        first_name text,
        last_name text,
        checkin_date integer,
        checkout_date integer,
        total_days integer,
        enclosure integer,
        collect text,
        deliver text,
        photo BLOB
        )
        """)
    #startup_data=[('','101','test first', '01/02/2022', '07/02/2022','7', '18', 'No', 'No', 'michelle_photo.jpg')]
    #c.executemany("INSERT or IGNORE INTO practice_bookings VALUES(?,?,?,?,?,?,?,?,?,?)",startup_data)
    #,,,commit the changes
    conn.commit()
    #,,,close the connection
    conn.close()

#bookings()

def upload_file():
    file=filedialog.askopenfilename()
    with open(file,'rb') as file:#read binary code.
        blob_data=file.read()

        my_data=[(None,20220311, 'Joe', 'Roberts', 20220312, 20220313, 2, 7, 'yes', 'yes',blob_data)]
        #,,,connect to database,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        conn=sqlite3.connect("practice.db")
        #,,,create a cursor.
        c=conn.cursor()
        #,,,create a bookings table.
        c.execute('INSERT INTO practice_bookings (photo) VALUES ("michelle_photo.jpg")')
        
        #,,,commit the changes
        conn.commit()
        #,,,close the connection
        conn.close()
        print('Data updated:')
    
#upload_file()    

def between_dates():
    conn=sqlite3.connect("tree_crm.db")
    c=conn.cursor()
    #,,,find bookings between ???..(you can use calendar pick box for dates).
    c.execute("SELECT * FROM kennel_bookings WHERE in_date BETWEEN '15/8/2022' and '22/8/2022' order by in_date desc")#desc
    print("Start of search.")
    returndates=c.fetchall()
    for x in returndates:
        booking_ref=(x[0])
        first_name=(x[1])
        last_name=(x[2])
        check_in=(x[8])
        check_out=(x[9])
        total_days=(x[10])
        print(f"{booking_ref} {first_name} {last_name}, check in date: {check_in} check out date: {check_out} for {total_days} days.") 
        
    conn.commit()
    conn.close()
    print(len(returndates))#gives the total of checkouts 
        
between_dates()
