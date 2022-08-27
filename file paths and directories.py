
# what files do I have???
#https://youtu.be/uQ5BZht9L3A
from pathlib import Path 

# where am I?
cwd = Path.cwd()
print('\nCurrent working directoty:\n' + str(cwd))

# Get the parent directory
parent=cwd.parent

# Combine parts to creat path name
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

demo_file = Path.joinpath(cwd, 'demo_file.txt')
# Does file exist?
print('\nDoes file exist? '+ str(new_file.exists()))#returns tru or false
# Get file name
print('\nFile name: ' + demo_file.name)
# Get extention
print('\nFile suffix: ' + demo_file.suffix)
# Get the folder
print('\nFile folder name: ' + demo_file.parent.name)
#Get the size
#print(demo_file.stat().st_size)

#Directory
# Is this the directory
print('\nIs this the directory? '+ str(parent.is_dir()))#returns True or False
# Is this the file
print('\nIs this the file? '+str(parent.is_file()))

# List child directories
print('\n-------directory contents--------')
for child in parent.iterdir():
    if child.is_dir():
        print(child)



