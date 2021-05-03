import time                                             # For pausing results and light timers
import socket                                           # For socket/port testing
import logging
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')   #Set up timestamp and logfile name

# Import IP address
ipFile = open("ipAddress.txt","r")                      # To open PC file
global ipAddress                                        # Make ipAddress globally accessible
ipAddress = ipFile.readline()                           # Reads IP address from line 1 of file

# Import port numbers
global portList                                         # Make portList globally accessible
portList = open("portList.txt").read().splitlines()     # To open file

logging.info('Checking begins')
print(ipAddress+" is IP address being tested"+"\n")     # For Testing
logging.info("IP address being tested is "+ipAddress)   # Log IP address being tested           **
print("Port numbers read in for testing:")              # For Testing
print(portList)                                         # For Testing
logging.info("Ports being tested")                      # Log ports being tested                **
logging.info(portList)                                 # Log ports being tested
print                                                   # For Testing
for portNum in portList:                                # Start iterating through ports
    print(portNum+" is being tested")              # For Testing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
    sock.settimeout(5)                                  # Reduce timeout to 5 seconds
    time.sleep(3)                                       # Pause program so white light doesn't just blink between tests
    result = sock.connect_ex((ipAddress, int(portNum))) #
    if result == 0:
        print ("Port "+portNum+" is open")              # For Testing
        logging.info('Port ' + portNum + ' is open :)') # Log port test successful
        time.sleep(3)                                   # Pause for 3 seconds
    else:
        print ("Port "+portNum+" not open")             # For Testing
        logging.info('Port ' + portNum + ' is closed :(')   # Log port test successful
        time.sleep(3)                                   # Pause for 3 seconds
ipFile.close()                                          # Close file
