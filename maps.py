from tkinter import *
import tkintermapview

root = Tk()
root.title('Codemy.com - Tkinter MapView')

root.geometry("800x600")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
# Set Coordinates
#map_widget.set_position(54.8766873, -1.4282809) 

# Set Address
marker_1=map_widget.set_address("52 Arundel Road, Sunderland, United Kingdom",marker=True)
print(marker_1.position,marker_1.text)
marker_1.set_text("52 Arundel Road, Sunderland, United Kingdom")

# Set A Zoom Level
map_widget.set_zoom(15)


map_widget.pack()



root.mainloop()