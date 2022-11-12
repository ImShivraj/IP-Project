# ip project
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sql 

df = pd.read_csv(r"data.csv", encoding='latin-1', skiprows=1)
df.columns = [
    "ac_year",
    "statcd",
    "statname",
    "area_sqkm",
    "tot_population",
    "urban_population",
    "grwoth_rate",
    "sexratio",
    "sc_population",
    "st_population",
    "literacy_rate",
    "male_literacy_rate",
    "female_literacy_rate",
]



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
        df = pd.read_csv(r"data.csv", encoding='latin-1')
        print("Imported successfully!")
        # choice = input("Do you wanna print it ? ")
        print(df)

    elif collectoption == 1:

        a = sql.connect(host="localhost", user="root", password="123")
        cursor = a.cursor()
        cursor.execute("DROP DATABASE IF EXISTS IPPROJECT")
        cursor.execute("CREATE DATABASE IPPROJECT")
        cursor.execute("select database();")
        cursor.fetchone()
        cursor.execute('DROP TABLE IF EXISTS data_project;')
        cursor.execute( """CREATE TABLE data_project (ac_year varchar(100),
                                                    statcd int(10),
                                                    statname varchar(100),
                                                    area_sqkm int(10),
                                                    tot_population float,
                                                    urban_population float,
                                                    grwoth_rate float,
                                                    sexratio int(10),
                                                    sc_population float,
                                                    st_population float,
                                                    literacy_rate float,
                                                    male_literacy_rate float,
                                                    female_literacy_rate float)"""
                         )
        for i,row in df.iterrows(): 
            value = "INSERT INTO data_project VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t1=cursor.execute(value, tuple(row)) 
        a.commit()
        cursor = a.cursor()
        cursor.execute("USE IPPROJECT;")
        a.commit()
        df=pd.read_sql("Select * from data_project", a)
        display(df)

    


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
    
    if manipulateoption == 1:
            i1=input("Enter the ac_year: ")
            i2=input("Enter the statcd: ")
            i3=input("Enter the statname: ")
            i4=input("Enter the area_sqkm: ")
            i5=input("Enter the tot_population: ")
            i6=input("Enter the urban_population: ")
            i7=input("Enter the grwoth_rate: ")
            i8=input("Enter the sexratio: ")
            i9=int(input("Enter the sc_population: "))
            i10=int(input("Enter the st_population: "))
            i11=int(input("Enter the literacy_rate: "))
            i12=int(input("Enter the male_literacy_rate: "))
            i13=int(input("Enter the female_literacy_rate: "))          
            cursor=a.cursor()
            cursor.execute("Use IPPROJECT;")
            cursor.execute("""INSERT INTO data_project VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13))
            a.commit()
            print("Your Data has been successfully added !")

    elif manipulateoption == 2:
        rows = list(map(int, input("Enter the index nos. of the rows you want to delete {Ex: 2 3 4 5}: ").split()))
        print(rows)
        df.drop(rows, axis=0, inplace=True)
        cursor=a.cursor()
        cursor.execute("Use IPPROJECT;")
        for i,row in df.iterrows(): 
            value = "INSERT INTO data_project VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t1=cursor.execute(value, tuple(row)) 
        a.commit()
        print("Rows have been deleted!")


    elif manipulateoption == 3:
        inp1 = int(input("Enter the index no. of the row: "))
        inp2 = int(input("Enter the index no. of the column: "))
        change = input("Enter the change: ")
        df.iloc[inp1, inp2+1] = change
        print(df , inplace=True)
        cursor=a.cursor()
        cursor.execute("Use IPPROJECT;")
        for i,row in df.iterrows(): 
            value = "INSERT INTO data_project VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t1=cursor.execute(value, tuple(row)) 
        a.commit()
        print("Your csv data has been modified successfully !")
        
    elif manipulateoption == 4:
        sort_by = input("Enter the name of the column you want to sort by:" )
        which_sort = input("Sort by [A]Ascending or [D]Descending:" )
        if which_sort.capitalize() == A:
            df.sort_values(by=sort_by , ascending=True)
            print(df)
        elif which_sort.capitalise() == D:
            df.sort_values(by=sort_by,ascending=False)
            print(df)
            
    elif manipulateoption == 5:
        None
            

    


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
        df_top = df.head(inp)
        print(df_top)
    elif analyseoption == 2:
        inp = int(input("Enter the number of rows you want: "))
        df_bottom = df.tail(inp)
        print(df_bottom)

    elif analyseoption == 3:
        inp = int(input("Enter the particular row number of the row you want to display: "))
        part_row = df.iloc[inp, :]
        print(part_row)

    elif analyseoption == 4:
        conditions = '''
    Choose one of the options from the following [1] or [2] or [3] or [4] \n\n
    1. Select rows on basis of index no. \n
    2. Select rows on the basis of statcd \n
    3. Select rows on the basis of statname \n
    4. Select rows on the basis of ac-year \n
    '''
        print(conditions)
        condition_inp = takeInput()
        if condition_inp == 1:
            inp1 = int(input("Please enter the starting index no.: "))
            inp2 = int(input("Please enter the ending index no.: "))

            index_df = df.iloc[inp1:inp2 + 1, :]
            print(index_df)

        elif condition_inp == 2:
            year_df = df['statcd']
            print(year_df)

        elif condition_inp == 3:
            count_df = df['statname']
            print(count_df)

        elif condition_inp == 4:
            sport_df = df['ac-year']
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
    1. area_sqkm vs tot_population \n
    2. area_sqkm vs grwoth_rate \n
    3. sexratio vs literacy_rate \n
    
    '''
        print(linemenu)
        lineoptions = takeInput()
        if lineoptions == 1:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.plot(df["area_sqkm"], df["tot_population"])
            plt.xlabel("area_sqkm")
            plt.ylabel("tot_population")
            plt.title("area_sqkm vs tot_population")
            plt.show()

        elif lineoptions == 2:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.plot(df["area_sqkm"], df["grwoth_rate"])
            plt.xlabel("area_sqkm")
            plt.ylabel("grwoth_rate")
            plt.title("area_sqkm vs grwoth_rate")
            plt.show()

        elif lineoptions == 3:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.plot(df["sexratio"], df["literacy_rate"])
            plt.xlabel("sexratio")
            plt.ylabel("literacy_rate")
            plt.title("sexratio vs literacy_rate")
            plt.show()

    elif visualoption == 2:
        barmenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. statname vs tot_population \n
    2. area_sqkm vs grwoth_rate \n
    3. sexratio vs literacy_rate \n
    '''
        print(barmenu)
        baroptions = takeInput()
        if baroptions == 1:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.bar(df["statname"], df["tot_population"],
                    color='c', width=0.4)
            plt.xlabel("statname")
            plt.ylabel("tot_population")
            plt.title("statname vs tot_population")
            plt.show()

        elif baroptions == 2:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.bar(df["statname"], df["grwoth_rate"],
                    color='c', width=0.4)
            plt.xlabel("statname")
            plt.ylabel("grwoth_rate")
            plt.title("statname vs grwoth_rate")
            plt.show()

        elif baroptions == 3:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.bar(df["sexratio"], df["literacy_rate"],
                    color='c', width=0.4)
            plt.xlabel("sexratio")
            plt.ylabel("literacy_rate")
            plt.title("sexratio vs literacy_rate")
            plt.show()

    elif visualoption == 3:
        hismenu = '''
    Choose one of the options from the following [1] or [2] or [3] \n\n
    1. sexratio \n
    2. Medals \n
    3. grwoth_rate \n
    '''
        print(hismenu)
        hisoptions = takeInput()
        if hisoptions == 1:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.hist(df["sexratio"])
            plt.xlabel("sexratio")
            plt.ylabel("literacy_rate")
            plt.title("sexratio vs literacy_rate")
            plt.show()

        elif hisoptions == 2:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.hist(df["literacy_rate"])
            plt.xlabel("sexratio")
            plt.ylabel("literacy_rate")
            plt.title("sexratio vs literacy_rate")
            plt.show()

        elif hisoptions == 3:
            plt.figure(figsize=(10, 8))
            plt.grid(True)
            plt.hist(df["grwoth_rate"])
            plt.xlabel("sexratio")
            plt.ylabel("literacy_rate")
            plt.title("sexratio vs literacy_rate")
            plt.show()

    elif visualoption == 4:
        None

    else:
        print("Please enter a valid option!")


def csv():
    csvmenu = '''
    Your data has been exported!!
    '''
    cursor=a.cursor()
    cursor.execute("USE IPPROJECT;")
    data_read = pd.read_sql("SELECT * from data_project", a)
    df = pd.DataFrame(data_read)
    df.to_csv("Updated data.csv", index = False) 
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