# Crochet Progress tracker
# Kayla Cromer
# 8.12.2021
# Purpose: Track progress on a crochet project in % while giving % updates when asked
# User will give information regarding
#  - name of Project
#  -how many rows/rounds in the project
project = input("What is the name of your project?")
print("Your current project is: " + project)
rows = input("How many rows/rounds does "+ project + " have?")

# Marker will track which row user is on
marker = input("Row/round completed ")
print(marker)

# progress will take in marker, will divide rows by marker and multiply by 100 to get progress percent
progress = float(marker) / float(rows) * 100
print("congrats! You are " + str(progress) + "% done. Keep up the good work.")
# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
