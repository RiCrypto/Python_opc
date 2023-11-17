from opcua import Client
import traceback
import os
import time
import sys
import subprocess



# Define the OPC UA server URL
url = "opc.tcp://10.1.45.7:62541"

# Define the path to the TAG (change it to your specific TAG path)
tag_path = "ns=2;s=[default]/Osprey_B1/Oven_B1"


def run_in_new_console(script_path):
    if sys.platform.startswith('win'):
        subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(['x-terminal-emulator', '-e', 'python', script_path])

def run_osp_b1():
  import Osprey_B1_sqlite_sql_B as osp_b1
  return() 

# Create an OPC UA client and connect to the server
client = Client(url)
try:
    client.connect()

    # Get the object representing the TAG
    tag_node = client.get_node(tag_path)

    # Monitor the value changes of the TAG
    
    old_value = None
    while True:
        try:
            new_value = tag_node.get_value()
            if new_value != old_value:
                print(f"TAG value changed: {new_value}")
                if new_value in [True, 1]:
                    print("Executing Osprey_B1...")
                    # Execute the batch file here
                    run_osp_b1()             
                    time.sleep(5) # wait 5 seconds
            old_value = new_value
         
        except Exception as e:
            print(f"Error reading tag value: {e}")
            traceback.print_exc()
        time.sleep(10) # wait 10 seconds  
finally:
    # Disconnect the client when done
    client.disconnect()
