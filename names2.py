## import graphics module
import tkinter as tk

## Setting up a _root window_, in which everything will appear,
## e.g., like this:
root = tk.Tk() # `Tk()` is a constructor exported by `tkinter`

## Add a frame to the root window just for the fun of it:
frame = tk.Frame( root )  # the parameter is the _parent_ in which
                          # it will appear
## We must indicate how the frame must appear (using a
## _geometry manager_), otherwise it wil not appear at all:
frame.pack()

## List of names:
names = [
    "Ádám",
    "Bendegúz",
    "Csanád",
    "Dóra",
    "Márk",
    "Zsiga"
    ]

namesMarked = []

## add names buttons with the same click handler:
def handleNameClick( event ):
    event.widget.config( background = "#cdcdcd" )
    namesMarked.append( event.widget.name )
    print( namesMarked )
    
nameButtons = {}

for i in range( len( names ) ):
    button = NameButton( frame, names[i] )  # tk.Button( frame, text = names[i] )
    nameButtons[names[i]] = button
    button.grid( column=0, row=i )
    ## problem: should have a separate handler for each new button!
    button.bind( "<Button-1>", handleNameClick )

## add a button to the frame window (of course, `text` is a
## useful keyword parameter when we use a button)"
quitButton = tk.Button( frame, text="Quit" )

## You must use a geometry manager for the button to appear,
## let us use the `grid()` manager within the frame window:
## place the button into the top left corner:
quitButton.grid( row=len( names ), column=0 )

## define an event handler of the Quit button:
def quit_handler( event ):
    event.widget.quit()   # look up event's widget

## bind the handler to the widget, with event type "left click":
quitButton.bind( "<Button-1>", quit_handler )

## The end of your main procedure:
root.mainloop()                 # that's it, nothing else to do
