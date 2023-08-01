from serial import Serial                                     # add Serial library for serial communication
import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.

Arduino_Serial = Serial('com5',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
 
while 1:
    incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
    print(incoming_data)                            # print the incoming Serial data
        
    if 'left' in incoming_data:                # if incoming data is 'previous'
        pyautogui.press("capslock")
        print("caps lock pressed\n")

    if 'right' in incoming_data:
        pyautogui.press("tab")
        print("tab pressed\n")

    # if 'down' in incoming_data:
    #     pyautogui.scroll(-100)
        
    # if 'up' in incoming_data:
    #     pyautogui.scroll(100)