import time                                                 # For pausing results and light timers
import socket                                               # For socket/port testing
import sys                                                  # For logging system data
import platform                                             # For logging system data
import subprocess                                           # For pinging
import logging                                              # For logging events and outputs to file
from tkinter import*                                        # GUI module import
#import dropbox                                              # For file posting online
# Set up timestamp and logfile name...
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Set up button action...
def show_button_action(*args):                              # Action for button press created, the *args allows enter or button click to work
    logging.info('Python version is ' +sys.version[0]+sys.version[1] +sys.version[2])        # Log Python version
    logging.info('Operating system is: '+platform.system()+' '+platform.release())     # Log OS being run on
    logging.info('Checking begins')                         # Add a logging event to button use
    ipAddress = get_IP.get()                                # Pull IP address from entry field into ipAddress variable
    logging.info('IP address being tested is ' + ipAddress) # Log IP address being tested
    resultText.delete("1.0", "end")                         # Clear text box (for second run)
    pingLine.config(text='', font=(60))                     # Blank out Ping results line
    allDone.config(text='',font=(60))                       # Blank out the text field
    root.update()                                           # Screen refresh
    os_name=sys.platform                                    # Assign OS to variable
# Set parameters as function of OS for pinging
    if os_name=="win32":
        options=str('-n 1')
    else:
        options=str('-c 1')
# Pinging
    pingresult=subprocess.getoutput('ping' +' '+ ipAddress+' '+ options)
    if 'unreachable' in pingresult:
        pingLine.config(text=ipAddress+' is offline', font=(60), fg='red')
        allDone.config(text='App is closing',font=(60))
        logging.info(ipAddress+' is offline, closing app.')
        root.update()
        time.sleep(3)
        root.destroy()                                      # Testing stop options
    elif 'Request' in pingresult:
        pingLine.config(text=ipAddress+' is offline', font=(60), fg='red')
        allDone.config(text='App is closing',font=(60))
        logging.info(ipAddress+' is offline, closing app.')
        root.update()
        time.sleep(3)
        root.destroy()                                      # Testing stop options
    else:
        pingLine.config(text=ipAddress+' is Online', font=(60), fg='green')
        logging.info(ipAddress+' is Online')
        root.update()                                       # Screen refresh
# Start iterating through ports
    logging.info('Ports being tested')                      # Log ports being tested
    logging.info(portList)                                  # Log ports being tested
    for portNum in portList:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Set up socket (port) testing
        sock.settimeout(5)                                  # Reduce timeout to 5 seconds
        time.sleep(1)                                       # Pause for 1 second
        result = sock.connect_ex((ipAddress, int(portNum))) # Check port on IP address
        if result == 0:                                     # If open do this
            logging.info('Port ' + portNum + ' is open :)') # Log port test successful
            resultText.insert(END,'Port ' + portNum + ' is open\n')     # Adding output to text field and send newline 
            root.update()                                   # Screen refresh
            time.sleep(1)                                   # Pause for 1 second
        else:                                               # If closed
            logging.info('Port ' + portNum + ' is closed :(')           # Log port test successful
            resultText.insert(END,'Port ' + portNum + ' is closed\n')   # Adding output to text field and send newline
            root.update()                                   # Screen refresh
            time.sleep(1)                                   # Pause for 1 second
    allDone.config(text='Port check complete',font=(60),fg='blue')      # Insert a comment that program is done

# Set up GUI...
root=Tk()                                                   # Build standard window object called root
logging.info('App Started')                                 # Add a logging event for App Start
root.bind('<Return>', show_button_action)                   # Allows for button press or pressing enter to work
root.title('Digilab Port Tester')                           # Assign title to title bar
root.iconbitmap('digi.ico')                                 # Set icon for window
root.geometry('500x400')                                    # Set window dimensions
genericText=Label(root,text='Enter IP address to test below',font=(60)) # Generic text for window with formatting
genericText.pack(fill=X,padx=5,pady=5)                      # Makes text visible in GUI and fills space with formatting
get_IP=Entry(root)                                          # Creating entry field called getIP
get_IP.pack()                                               # Makes entry field visible in GUI
buttonOne=Button(root,text='Start Check',command=show_button_action)    # Button with action
buttonOne.pack(padx=5,pady=5)                               # Makes button visible in GUI
resultText=Text(root,height=6,width=25,font=(60))           # Create text box for output to be sent
resultText.pack()                                           # Makes placeholder visible in GUI
spacerLine=Label(root,text='')                              # Create blank line
spacerLine.pack()                       
pingLine=Label(root,text='')                                # Create line for Ping results
pingLine.pack()                                             # Make line visible in GUI
spacerLine2=Label(root,text='')                             # Blank line for space
spacerLine2.pack()
allDone=Label(root,text='',font=(60))                       # Insert a field and set as blank for noting when check completes
allDone.pack()                                              # Insert a comment that program is done
               
# Import port numbers to be tested...
global portList                                             # Make portList globally accessible
portList = open('portList.txt').read().splitlines()         # To open PC file
get_IP.focus()                                              # Makes the text entry field 'active' for input
root.mainloop()                                             #Launch window and start event listening
logging.info('App Stopped')                                 #Add a logging event to App Stop

# Post results to Dropbox
#token = open('access_token.txt','r+')                       # Open file containing access code for read/write
#access_token=token.read()                                   # Assign file contents to variable
#dbx = dropbox.Dropbox(access_token)                         # Pass access token to Dropbox
#dbx.files_delete_v2('/results.log')                         # Delete previous version uploaded
#with open("results.log", "rb") as f:                        # Start upload of file contents
#    dbx.files_upload(f.read(), '/results.log', mute = True)
