name=['Enclosure', 'Runs', 'Kennel', 'Other'] #,enclosure.get()
name.append('Help')#,adds Help to the list #,enclosure.get()
#name[3]= 'Units'#,replaces Other with Units #,enclosure.get()



runs=[]
number_of_runs=10#'Kennel'#, runs.get()
for num in range(1,number_of_runs):#,remove 1 to start from 0.
    runs.append(num)#,+1 will start from 1 not 0.
    
#runs[0]=enclosure
print(runs + name)
print(name)