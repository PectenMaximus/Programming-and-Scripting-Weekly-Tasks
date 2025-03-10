#Author: Alec Reid
#Date:09.03.2025

def displaymenu():
    print ("what would you like to do?")
    print ("\t(a) Add a new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input ("Type one letter (a/v/q):").strip()
    return choice 
def do_add ():
    #we will fill this in later
    print ("in adding")
def do_view (): 
    #we will fill this in later
    print ("in viewing")

# main programme
choice = displaymenu ()
while (choice != 'q'):
    if choice == 'a':
        do_add() 
    elif choice !='q':
        print ("\n\nplease select either a,v or q")
        choice = displaymenu()

