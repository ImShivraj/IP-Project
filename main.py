#ip project 

def takeInput():
    inp = int(input("Enter your preferred option: "))
    return inp


def intro():
    intro = '''
    Welcome to the the IP projekt \n
    \t \t made by Mudra and Shivraj
    '''
    print(intro)

    mainmenu = '''
    Choose one of the options from the following [1] or [2] or [3] or [4] or [5] or [6]\n\n
    1. Data Collection\n
    2. Data Manipulation on SQL\n
    3. Data Analysis\n
    4. Data Visualization\n
    5. Data Export to CSV\n
    6. Exit\n
    '''
    print(mainmenu)


def dataCollect():
   
    collectmenu = '''
    Choose one of the options from the following [1] or [2]\n\n
    1. Data import from CSV to SQL\n
    2. Data import from CSV to DataFrame\n
    3. Return back to main menu\n
    '''
    print("Data Collection\t")
    print(collectmenu)
    collectoption = takeInput()
    if collectoption == 1:
        None # todo 
    elif collectoption == 2:
        print("Data Collection\t")  #todo 


def dataManipulate():
    
    manipulatemenu = '''
    Choose one of the options from the following [1] or [2] or [3] or [4] \n\n
    1. Insert rows \n
    2. Delete rows \n
    3. Update information \n
    4. Sort data \n
    5. Return back to main menu\n
    '''
    print("Data Manipulation on SQL\t")
    print(manipulatemenu)
    manipulateoption = takeInput()
   

def dataAnalysis():
    analysisemenu = '''
    Choose one of the options from the following [1] or [2] or [3] or [4] \n\n
    1. Display top records \n
    2. Display bottom records \n
    3. Display a particular Row \n
    4. Display a Row on basis of conditions \n
    5. Return back to main menu\n
    '''
    print("Data Analysis\t")
    print(analysisemenu)
    analyseoption = takeInput()


def dataVisual():
    visualmenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. Line Graph \n
    2. Bar Graph \n
    3. Histogram Graph \n
    4. Return back to main menu\n
    '''
    print("Data Visualization\t")
    print(visualmenu)
    visualoption = takeInput()
  

def csv():
    csvmenu = '''
    Choose one of the options from the following [1]  \n\n
    1. Transfer the changes back to csv \n
    '''
    print("Data Collection\t")
    print(csvmenu)
    csvoption = takeInput()


  


if __name__ == '__main__':

    while True:
        intro()
        # option1 = int(input("Enter your preferred option: "))
        option1 = takeInput()

        if option1 == 1: 
            dataCollect()
           

        elif option1 == 2:
            dataManipulate()
            

        elif option1 == 3: 
            dataAnalysis()
            

        elif option1 == 4:
            dataVisual()
            

        elif option1 == 5:
            csv()

        elif option1 == 6:
            break

        else:
            print("Please enter a valid option.")
