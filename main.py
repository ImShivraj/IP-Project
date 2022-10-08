#ip project 
import pandas as pd
import matplotlib.pyplot as plt
import sql

df = pd.read_csv('data.csv',encoding='latin-1')

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
    if collectoption == 3:
        None
    elif collectoption == 2:
        df = pd.read_csv('data.csv',encoding='latin-1')
        print(df)
        
    elif collectoption == 1:

        a = sql.connect (host = "localhost", user = "root", password = " ")
        cursor = a.cursor ()
        cursor.execute ("create database project")


    # .....  not complete d yet 

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
    # .....  not completed yet
   

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
    if analyseoption == 1:
        inp = int(input("Enter the number of rows you want: "))
        df_top= df.head(inp)
        print(df_top)
    elif analyseoption == 2:
        inp = int(input("Enter the number of rows you want: "))
        df_bottom= df.tail(inp)
        print(df_bottom)

    elif analyseoption == 3:
        inp = int(input("Enter the particular row number of the row you want to display: "))
        part_row = df.iloc[inp, :]
        print(part_row)

    elif analyseoption == 4 :
        conditions = '''
    Choose one of the options from the following [1] or [2] or [3] or [4] \n\n
    1. Select rows on basis of index no. \n
    2. Select rows on the basis of year \n
    3. Select rows on the basis of Country \n
    4. Select rows on the basis of Sport \n
    '''
        print(conditions)
        condition_inp = takeInput()
        if condition_inp == 1:
            inp1 = int(input("Please enter the starting index no.: "))
            inp2 = int(input("Please enter the ending index no.: "))

            index_df = df.iloc[inp1:inp2+1 , : ]
            print(index_df)

        elif condition_inp == 2:
            year_df = df['Year']
            print(year_df)

        elif condition_inp == 3:
            count_df = df['Country']
            print(count_df)

        elif condition_inp == 4:
            sport_df = df['Sport']
            print(sport_df)

        else:
            print("Please enter a valid option!")

    elif analyseoption == 5:
        None

    else:
        print("Please enter a valid option!")
   


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

    if visualoption == 1:
        linemenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. Year vs Country \n
    2. Year vs Medal \n
    3. Country vs Gender \n
    
    '''
        print(linemenu)
        lineoptions = takeInput()
        if lineoptions == 1:
            plt.plot(df["Year"], df["Country"])
            plt.show()

        elif lineoptions == 2:
            plt.plot(df["Year"], df["Medal"])
            plt.show()

        elif lineoptions == 3:
            plt.plot(df["Country"], df["Gender"])

    elif visualoption == 2:
        barmenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. Year vs Country \n
    2. Year vs Medal \n
    3. Country vs Gender \n
    '''
        print(barmenu)
        baroptions = takeInput()
        if baroptions ==1:
            plt.bar(df["Year"], df["Country"])
            plt.show()

        elif baroptions ==2:
            plt.bar(df["Year"], df["Medal"])
            plt.show()

        elif baroptions ==3:
            plt.bar(df["Country"], df["Gender"])
            plt.show()

    elif visualoption == 3:
        hismenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. Countries \n
    2. Medals \n
    3. Genders \n
    '''
        print(hismenu)
        hisoptions = takeInput()
        if hisoptions ==1:
            plt.hist(df["Country"])
            plt.show()

        elif hisoptions ==2:
            plt.hist(df["Medal"])
            plt.show()

        elif hisoptions ==3:
            plt.hist(df["Gender"])
            plt.show()

    elif visualoption == 4:
        None

    else:
        print("Please enter a valid option!")


def csv():
    csvmenu = '''
    Your data has been exported!!
    '''
    print(csvmenu)
    inpyes = input("Do you want to see it ? [y]/[n]")
    if inpyes.lower() == 'y':
        print(df)

    elif inpyes.lower() == 'n':
        None

    else:
        print("Please enter a valid option!")
    

  


if __name__ == '__main__':

    while True:
        intro()
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
