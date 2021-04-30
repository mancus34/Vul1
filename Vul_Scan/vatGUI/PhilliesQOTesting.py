import tkinter as tk #gui
import requests
import tkinter.font as tkFont #custom fonts
from tkinter import *
from tkmagicgrid import *
import io
import csv

#canvas dimensions
HEIGHT = 600
WIDTH = 900

#root (welcome page)
root = tk.Tk()
root.minsize(WIDTH,HEIGHT)

#custom fonts
font1 = tkFont.Font(family="Segoe UI Light",size=16) #bold and large
root.font=font1
font2 = tkFont.Font(family="Segoe UI Light",size=24)
root.font2 = font2

#create canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#title and icon 
root.title("VAT")
#root.iconbitmap("philliesicon.ico")

#background image
bg_image = tk.PhotoImage(file='bg.gif')
root.bg_image = bg_image
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

#frame that holds the labels and buttons 
frame1 = tk.Frame(root, bg = "white",  borderwidth=2, relief="groove")
frame1.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.4)

#labels
label = tk.Label(frame1, text="vulnerability assessment tool", bg="white",font="font2")
label.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)


'''welcome page: BEGIN button event'''

#begin button event (go to main page)
def beginClick():

    #canvas dimensions
    HEIGHT = 600
    WIDTH = 900

    average = '$16,000,000'

    #main
    main = tk.Toplevel()
    main.minsize(WIDTH,HEIGHT)
    
    #custom font
    font1 = tkFont.Font(family="Segoe UI Light",size=16)
    main.font = font1

    #create canvas
    canvas = tk.Canvas(main, height=HEIGHT, width=WIDTH)
    canvas.pack()

    #title and icon 
    main.title("Phillies Qualifying Offer: One Year Contract")
    #main.iconbitmap("philliesicon.ico")

    #cite- image not getting garbage collected anymore
    #https://stackoverflow.com/questions/26479728/tkinter-canvas-image-not-displaying
    #background image
    background_image = tk.PhotoImage(file='bg.gif')
    main.image = background_image
    background_label = tk.Label(main, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    #button events (change to redirecting to different page (phase 2))
    #accept button event 
    def runClick():
        
        #new page
        accept_win = tk.Toplevel()
        accept_win.minsize(WIDTH,HEIGHT)
        accept_win.title("Acceptance Page")
        #accept_win.iconbitmap("philliesicon.ico")
        img = tk.PhotoImage(file='bg.gif') #not showing up for some reason
        accept_win.img = img
        background_label = tk.Label(accept_win, image=img)
        background_label.place(relwidth=1, relheight=1)

        # Create a MagicGrid widget
        grid = MagicGrid(accept_win)
        grid.pack(side="top", expand=1, fill="both")

        # Display the contents of some CSV file
        # (note this is not a particularly efficient viewer)
        with io.open("results.csv", "r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            parsed_rows = 0
            for row in reader:
                if parsed_rows == 0:
                    # Display the first row as a header
                    grid.add_header(*row)
                else:
                    grid.add_row(*row)
                parsed_rows += 1



        #exit both windows
        #cite: https://stackoverflow.com/questions/55560127/how-to-close-more-than-one-window-with-a-single-click
        def qExit():
            accept_win.destroy()
            main.destroy()
            root.destroy()

        btn = tk.Button(f, text="exit", bg="#f4fdf4", activebackground="#b1d3b1", activeforeground="black",cursor="hand2", pady=10, padx=10, font="font1", command=qExit).place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1) 
        
        #exit both windows
        #cite: https://stackoverflow.com/questions/55560127/how-to-close-more-than-one-window-with-a-single-click
        def qExit():
            main.destroy()
            root.destroy()

        btn = tk.Button(f, text="exit",  bg="#f4fdf4", activebackground="#b1d3b1", activeforeground="black",cursor="hand2", pady=10, padx=10, font="font1", command=qExit).place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1) 

    #frame that holds the labels and buttons 
    frame1 = tk.Frame(main, bg = "white",  borderwidth=2, relief="groove")
    frame1.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.3)

    #labels
    label = tk.Label(frame1, text="Click RUN to generate vulnerability assessment", bg="white",font="font1")
    label.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)
    
    #MAIN PAGE run button
    run_btn = tk.Button(frame1, text="run", pady=10, padx=10, command=runClick, fg="black", bg="white", activebackground="grey",
                       activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
    run_btn.place(relx=0.15, rely=0.5, relwidth=0.2, relheight=0.3)
    
    #MAIN PAGE exit button
    btn = tk.Button(main, text="exit", bg="white", activebackground="grey", activeforeground="black",cursor="hand2", pady=10, padx=10, font="font1", command=root.destroy).place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1) 



'''welcome page: HELP btn event '''
    
def helpClick():
    
    #new page
    help_win = tk.Toplevel()
    help_win.minsize(WIDTH,HEIGHT)
    help_win.title("Help Page")
    #help_win.iconbitmap("philliesicon.ico")
    img = tk.PhotoImage(file='bg.gif')
    help_win.img = img
    background_label = tk.Label(help_win, image=img)
    background_label.place(relwidth=1, relheight=1)
    
    #custom font
    font1 = tkFont.Font(family="Segoe UI Light",size=16)
    help_win.font = font1
    
    #frame that holds the labels and buttons 
    f = tk.Frame(help_win, bg = "black",  borderwidth=2, relief="groove")
    f.place(relx=0.075, rely=0.1, relwidth=0.85, relheight=0.8)
    
    background_label = tk.Label(f, bg="white")
    background_label.place(relwidth=1, relheight=1)
    
    background_label = tk.Label(f, bg="white", text="how to use tool:", pady=10, padx=10, font="font1",justify="left")
    background_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    
    #back
    btn = tk.Button(f, text="back", bg="#f4fdf4", activebackground="#b1d3b1", activeforeground="black",cursor="hand2", pady=10, padx=10, font="font1", command=help_win.destroy).place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1) 
    
'''welcome page: buttons'''

#buttons
#begin button (go to main page)
begin_btn = tk.Button(frame1, text="begin", pady=10, padx=10, command=beginClick, fg="black", bg="#f4fdf4",
                      activebackground="#b1d3b1", activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
begin_btn.place(relx=0.15, rely=0.5, relwidth=0.3, relheight=0.3)

#help button
help_btn = tk.Button(frame1, text="help", pady=10, padx=10, command=helpClick, fg="black", bg="#f4fdf4",
                      activebackground="#b1d3b1", activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
help_btn.place(relx=0.55, rely=0.5, relwidth=0.3, relheight=0.3)
    
root.mainloop()