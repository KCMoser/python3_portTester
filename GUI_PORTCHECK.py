import time                                             # For pausing results and light timers
import socket                                           # For socket/port testing
import logging                                          # For logging events and outputs to file
from tkinter import*                                    #GUI module import
# Set up timestamp and logfile name...
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
global resultText                               #                                                                                   **                

# Set up GUI...
def show_button_action(*args):              # Action for button press created, the *args allows enter or button click to work
    logging.info('Button pressed')          # Add a logging event to button use
    ipAddress = get_IP.get()                # Pull IP address from entry field into ipAddress variable
    print(ipAddress + " is IP address being tested"+"\n")   # For Testing
    logging.info("IP address being tested is " + ipAddress) # Log IP address being tested
    print("Port numbers read in for testing:")              # For Testing
    print(portList)                                         # For Testing
    logging.info("Ports being tested")                      # Log ports being tested
    logging.info(portList)                                  # Log ports being tested
    print                                                   # For Testing
    for portNum in portList:                                # Start iterating through ports
        print(portNum+" is port being tested")              # For Testing
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set up socket (port) testing
        sock.settimeout(5)                                  # Reduce timeout to 5 seconds
        time.sleep(3)                                       # Pause program so white light doesn't just blink between tests
        result = sock.connect_ex((ipAddress, int(portNum))) # Check port on IP address
        if result == 0:                                     # Check if open
            logging.info("Port " + portNum + " is open :)") # Log port test successful
            print ("Port "+portNum+" is open")              # For Testing
            resultText.config(text='Port ' + portNum + ' is open')
            root.update()
            time.sleep(3)                                   # Pause for 3 seconds
        else:                                               # If closed
            logging.info("Port " + portNum + " is closed :(")    # Log port test successful
            print ("Port "+portNum+" is closed")             # For Testing
            resultText.config(text='Port ' + portNum + ' is closed')
            root.update()
            time.sleep(3)                                   # Pause for 3 seconds
        
root=Tk()                                       # Build standard window object called root
logging.info('App Started')                     # Add a logging event for App Start
root.bind("<Return>", show_button_action)       # Allows for button press or pressing enter to work
root.title("Aligned Focus")                     # Assign title to title bar
root.geometry("600x400")                        # Set window dimensions
genericText=Label(root,text="Enter IP address to test below")        # Generic text for window with formatting
genericText.pack(fill=X,padx=5,pady=5)          # Makes text visible in GUI and fills space with formatting
get_IP=Entry(root)                              # Creating entry field called getIP
get_IP.pack()                                   # Makes entry field visible in GUI
buttonOne=Button(root,text='Start Check',command=show_button_action) # Button with action
buttonOne.pack(padx=5,pady=5)                   # Makes button visible in GUI
resultText=Label(root)                          # Creates a placeholder under the button as text
resultText.pack()                               # Makes placeholder visible in GUI
               
# Import port numbers...
global portList                                             # Make portList globally accessible
portList = open("portList.txt").read().splitlines()         # To open PC file

root.mainloop()                             #Launch window and start event listening
logging.info('App Stopped')                 #Add a logging event to App Stop


