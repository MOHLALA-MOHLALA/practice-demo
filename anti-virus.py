import os
import subprocess

# function to scan a file for viruses
def scan_file(filename):
    cmd = ['clamscan', '--stdout', '--infected', filename]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if "Infected files: 1" in output:
        return True
    else:
        return False

# main program loop
while True:
    print("Virus Scanner")
    print("1. Scan a file")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        filename = input("Enter filename to scan: ")
        if os.path.isfile(filename):
            if scan_file(filename):
                print("Virus detected!")
            else:
                print("No viruses found")
        else:
            print("File not found")
    elif choice == '2':
        break
    else:
        print("Invalid choice")

