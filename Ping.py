import os
import csv
os.system("cls") #use this for windows. change to os.system("clear") for linux

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
#You can add more colors and backgrounds to the dictionary if you like.

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

#Example printing out an ASCII file
f  = open("header.txt","r+")
ascii = "".join(f.readlines())
print(colorText(ascii)) 

# Open file for saving ping results
results_file = open("results.txt", "w")
# Empty list to store ip addresses
ip_list = []
# Outputs to results.txt file
with open("ipliste.txt") as file:
    ip_list = [line.rstrip('\n') for line in file]
for ip in ip_list :
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response :
        print ((f" \u001b[32mUP {ip} ping Successful" ))
        results_file.write(f"  UP {ip} Ping Successful" + "\n")
    else:
        print ((f"\u001b[31m DOWN {ip} ping Unsuccessful"))
        results_file.write(f"  Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()

input("\u001b[34;1mPress enter to exit ;)")
