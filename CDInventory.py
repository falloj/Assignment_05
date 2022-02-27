#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Jaclynn Fallon, 2022-Feb-27, Modified File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dicTbl = [] # list of dicts to hold data
dicRow = {} # an empty dict to hold each CD data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        # File to print
        # TODO read the file line by line into in-memory dictionary
        try: # Add error handling in case the txt file doesn't exist yet
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {'ID':int(lstRow[0]), 'Album':lstRow[1], 'Artist':lstRow[2]}
                dicTbl.append(dicRow)
            objFile.close()
            print('Your CD inventory is loaded in memory now.\n')
        except:
            print('Your CD inventory is empty!  Try adding a CD to it.\n')
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        # To prevent the user from entering a duplicate ID, we select the ID for them
        if len(dicTbl) == 0:
            ID = 1
        if len(dicTbl) != 0:
            inventTbl = []
            for CD in dicTbl:
                CDlst = []
                for key, val in CD.items():
                    CDlst.append(val)
                    inventTbl.append(CDlst)
                    IDlst = []
                    for row in inventTbl:
                        IDlst.append(row[0])
                        start = 1
                        last = max(IDlst)
                        end = last + 1
                        numbers = range(start, end, 1)
                        if len(dicTbl) != last:
                            for i in numbers:
                                if i not in IDlst:
                                    ID = i
                        else:
                            ID = len(dicTbl) + 1
        print('\nThe ID number for your entry will be: ' + str(ID))
        album = input('Enter the CD\'s Title: ')
        artist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID':ID, 'Album':album, 'Artist':artist}
        # Append the new dictionary to the 2D list
        dicTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        heading = 'ID, Album, Artist'
        print('\nYour CD inventory is: \n')
        print(heading)
        for dic in dicTbl:
            stringList = []
            for key, val in dic.items():
                val = str(val) 
                val += ' | '
                stringList.append(val)
            formattedString = ''.join(stringList)
            print(formattedString)
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        ID = input('Please enter the ID of the CD you want to delete: ')
        delID = int(ID) - 1
        del dicTbl[delID]
        print('\nThat CD in now deleted from inventory.')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        stringTable = []
        for CD in dicTbl:
            CDstring = []
            for key, val in CD.items():
                val = str(val) + ','
                CDstring.append(val)
                formattedString = ''.join(CDstring)
                formattedString = formattedString[:-1]
            stringTable.append(formattedString)
            objFile = open('CDinventory.txt', 'w') # Open the text file the user input will be saved to
            for item in stringTable:
                objFile.write(item + '\n') # Write the CD inventory to the text file
            objFile.close() # Close the txt file 
        print('\nYour CD Inventory is saved to a file now!\n') # Give the user some closure 
    else:
        print('Please choose either l, a, i, d, s or x!')