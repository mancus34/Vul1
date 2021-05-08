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
font3 = tkFont.Font(family="Segoe UI Light",size=10)
root.font3 = font3

#create canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#title and icon 
root.title("VAT: Welcome Screen")
#root.iconbitmap("scan.ico")

#background image
bg_image = tk.PhotoImage(file='bg2.gif')
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
    main.title("VAT: Main Page")
    #main.iconbitmap("scan.ico")

    #cite- image not getting garbage collected anymore
    #https://stackoverflow.com/questions/26479728/tkinter-canvas-image-not-displaying
    #background image
    background_image = tk.PhotoImage(file='bg2.gif')
    main.image = background_image
    background_label = tk.Label(main, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    #button events
    #run button event for displaying the results 
    def scanClick():
        
        #new page
        resultTable = tk.Toplevel()
        resultTable.minsize(WIDTH,HEIGHT)
        resultTable.title("Scan Results")
        #resultTable.iconbitmap("scan.ico")
        img = tk.PhotoImage(file='bg2.gif')
        resultTable.img = img
        background_label = tk.Label(resultTable, image=img)
        background_label.place(relwidth=1, relheight=1)
        
        # Create a MagicGrid widget
        grid = MagicGrid(resultTable)
        grid.pack(side="top", expand=1, fill="both")

        # Display the contents of some CSV file
        with io.open("vul_results.csv", "r", newline="") as csv_file:
            reader = csv.reader(csv_file, delimiter = '~')
            parsed_rows = 0
            for row in reader:
                if parsed_rows == 0:
                    # Display the first row as a header
                    grid.add_header(*row)
                else:
                    grid.add_row(*row)
                parsed_rows += 1
                
    #ip device button
    def runClick():
        
        #new page
        resultTable = tk.Toplevel()
        resultTable.minsize(WIDTH,HEIGHT)
        resultTable.title("IP Results")
        #resultTable.iconbitmap("scan.ico")
        img = tk.PhotoImage(file='bg2.gif')
        resultTable.img = img
        background_label = tk.Label(resultTable, image=img)
        background_label.place(relwidth=1, relheight=1)

        # Create a MagicGrid widget
        grid = MagicGrid(resultTable)
        grid.pack(side="top", expand=1, fill="both")

        # Display the contents of some CSV file
        with io.open("ip_results.csv", "r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            parsed_rows = 0
            for row in reader:
                if parsed_rows == 0:
                    # Display the first row as a header
                    grid.add_header(*row)
                else:
                    grid.add_row(*row)
                parsed_rows += 1

    #frame that holds the labels and buttons 
    frame1 = tk.Frame(main, bg = "white",  borderwidth=2, relief="groove")
    frame1.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.3)

    #labels
    label = tk.Label(frame1, text="Click SCAN to display vulnerability assessment", bg="white",font="font1")
    label.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)
    
    #MAIN PAGE run button
    run_btn = tk.Button(frame1, text="scan", pady=10, padx=10, command=scanClick, fg="black", bg="#A5B5BD", activebackground="#3a4546",
                       activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
    run_btn.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.3)
    
    #SECOND CSV FILE
    
    #frame that holds the labels and buttons 
    frame2 = tk.Frame(main, bg = "white",  borderwidth=2, relief="groove")
    frame2.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.3)

    #labels
    label2 = tk.Label(frame2, text="Click RUN to generate ip connected devices", bg="white",font="font1")
    label2.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)
    
    #MAIN PAGE run 2 button
    run_btn = tk.Button(frame2, text="run", pady=10, padx=10, command=runClick, fg="black", bg="#A5B5BD", activebackground="#3a4546",
                       activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
    run_btn.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.3)
    


'''welcome page: HELP btn event '''
    
def helpClick():
    
    #new page
    help_win = tk.Toplevel()
    help_win.minsize(WIDTH,HEIGHT)
    help_win.title("Help Page")
    #help_win.iconbitmap("scan.ico")
    img = tk.PhotoImage(file='bg2.gif')
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
    
    background_label = tk.Label(f, bg="white", text="This tool is used to display a vulnerability assessment\nscan on your system.\nIt provides a severity rating and description of found vulnerability.\n\nHow to use tool:\nAll assessments are designed for Linux machines.\n\nIP assessment\nTo obtain a list of IP connected Devices run the ip_assess.sh script.\nYou will need super user access to run this assessment.CVE assessment\nTo obtain a list of common vulnerabilities and exposures run the vul_assess.sh script.\nYou will need to enter the IP address you want to assess.\n\nNecessary software\nPython modules\nTkintertkmagicgrid\nBeautiful Soup\nre\n\nScanning software\nNmap\nNmap vulscan script", pady=10, padx=10, font="font3",justify="left")
    background_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
    
    #back
    btn = tk.Button(f, text="back", bg="#A5B5BD", activebackground="#3a4546", activeforeground="black",cursor="hand2", pady=10, padx=10, font="font1", command=help_win.destroy).place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.1) 
    
'''welcome page: buttons'''

#buttons
#begin button (go to main page)
begin_btn = tk.Button(frame1, text="begin", pady=10, padx=10, command=beginClick, fg="black", bg="#A5B5BD",
                      activebackground="#3a4546", activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
begin_btn.place(relx=0.15, rely=0.5, relwidth=0.3, relheight=0.3)

#help button
help_btn = tk.Button(frame1, text="help", pady=10, padx=10, command=helpClick, fg="black", bg="#A5B5BD",
                      activebackground="#3a4546", activeforeground="black",cursor="hand2", font="font1", borderwidth=2)
help_btn.place(relx=0.55, rely=0.5, relwidth=0.3, relheight=0.3)
    
root.mainloop()