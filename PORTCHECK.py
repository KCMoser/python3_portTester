import time                                             # For pausing results and light timers
import socket                                           # For socket/port testing
import logging
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')   #Set up timestamp and logfile name
#import RPi.GPIO as GPIO                                 # Import Raspberry Pi GPIO library
#GPIO.setmode(GPIO.BCM)                                  # Set naming convention for pins
#GPIO.setwarnings(False)                                 # Ignore warning messages

# Import IP address
#ipFile = open("/home/pi/Desktop/ipAddress.txt","r")     # RPi file convention
ipFile = open("ipAddress.txt","r")                      # To open PC file
global ipAddress                                        # Make ipAddress globally accessible
ipAddress = ipFile.readline()                           # Reads IP address from line 1 of file

# Import port numbers
global portList                                         # Make portList globally accessible
#portList = open("/home/pi/Desktop/portList.txt").read().splitlines()# Imports, no EOL chars
portList = open("portList.txt").read().splitlines()     # To open PC file

#ipAddr=ipAddress           *Remove if no errors @ runtime*
print(ipAddress+" is IP address being tested"+"\n")     # For Testing
logging.info("IP address being tested is "+ipAddress)   # Log IP address being tested           **
print("Port numbers read in for testing:")              # For Testing
print(portList)                                         # For Testing
logging.info("Ports being tested")                      # Log ports being tested                **
logging.info(portList)                                 # Log ports being tested
print                                                   # For Testing
for portNum in portList:                                # Start iterating through ports
    print(portNum+" is port being tested")              # For Testing
    #GPIO.setup(23,GPIO.OUT)                             # Activate pin 23 for use.
    #GPIO.output(23,GPIO.HIGH)                           # Turn white light on
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
    sock.settimeout(5)                                  # Reduce timeout to 5 seconds
    time.sleep(3)                                       # Pause program so white light doesn't just blink between tests
    result = sock.connect_ex((ipAddress, int(portNum))) #
    if result == 0:
        #GPIO.output(23,GPIO.LOW)                        # Turn white light off
        print ("Port "+portNum+" is open")              # For Testing
        #GPIO.setup(18,GPIO.OUT)                         # Activate pin 18 for use.
        #GPIO.output(18,GPIO.HIGH)                       # Turn green light on
        time.sleep(3)                                   # Pause for 3 seconds
        #GPIO.output(18,GPIO.LOW)                        # Turn green light off
    else:
        #GPIO.output(23,GPIO.LOW)                        # Turn white light off
        print ("Port "+portNum+" not open")             # For Testing
        #GPIO.setup(25,GPIO.OUT)                         # Activate pin 25 for use.
        #GPIO.output(25,GPIO.HIGH)                       # Turn red light on
        time.sleep(3)                                   # Pause for 3 seconds
        #GPIO.output(25,GPIO.LOW)                        # Turn red light off
#GPIO.cleanup()                                          # Reset GPIO resources
ipFile.close()                                          # Close file
