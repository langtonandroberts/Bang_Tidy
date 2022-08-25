
#use with Langton & Roberts.
import sqlite3


# select from the database table and format the results.
def sql_db():
    #,,, connect to general_settings table in database,,,,,,,,,,.
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    #,,,get info from general settings table in Database (should have only 1 row),,,,,,,
    c.execute("SELECT taxi_rate, standard_rate, luxury_rate, premium_rate FROM general_settings")
    record=c.fetchall()
    for i in record:
        taxi_rate=(i[0])
        taxi_rate=format(taxi_rate,'.2f')
        standard_rate=(i[1])
        standard_rate=format(standard_rate,'.2f')
        #standard_rate=float(standard_rate)
        luxury_rate=(i[2])
        luxury_rate=format(luxury_rate,'.2f')
        premium_rate=(i[3])
        premium_rate=format(premium_rate,'.2f')
        print("You have accessed the General Settings Table and this is the result.\n---------------------------------------------------")
        print(f"This is the Taxi Rate £{taxi_rate} one way only.")
        print(f"This is the Standard Rate £{standard_rate}.")
        print(f"This is the Luxury Rate £{luxury_rate}.")
        print(f"This is the Premium Rate £{premium_rate}.")
    #,,,commit the changes
    conn.commit()
    #,,, close the connection
    conn.close()

    sql_db()


