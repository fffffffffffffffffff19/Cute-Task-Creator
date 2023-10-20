import os
import sqlite3

#
conn = sqlite3.connect('tasks.sqlite')
c = conn.cursor()
# Connect and create the database #
c.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, date TEXT)')
conn.commit()
#

class ShowAllItems: # Class to interact with the database #
    def databaseLoop(self):
        for item in dbCheck():
            print(f'{item[0]}) {item[1]} : {item[2]}')
        print('')
    
    def nothingInList(self):
        clearConsole()

        print('The list does not contain any element. 〳・﹏・〵\n')

    def mainFuncText(self):
        if not dbCheck():
            print('  ~ No Task Found! )\n')
        else:
            self.databaseLoop()

    def deleteOneText(self):
        if not dbCheck():
            self.nothingInList()
        else:
           self.databaseLoop()

def dbCheck(): # Check if the have data on database #
    c.execute('SELECT * FROM tasks')

    return c.fetchall()

def clearConsole(): # the name says it all... #
    if os.name == 'nt':
        return os.system('cls')
    else:
        return os.system('clear')

def clearChoice(): # The "C" choice, for delete all tasks #
    clearConsole()

    if not dbCheck():
        ShowAllItems().nothingInList()
    else:
        dangerWarning = input("Do you really want to do this?（>﹏<） \n ⤷ this will delete all your tasks.\n\n[Y]ep [N]op: ")

        if not dangerWarning.lower() == 'n':
            c.execute('DELETE FROM tasks')
            c.execute('DELETE FROM sqlite_sequence WHERE name="tasks"')
            
            conn.commit()
            
            clearConsole()
            print(' All tasks have been deleted. ●︿●\n')
        else:
            clearConsole()
            print(' Clear was canceled. d–(^ ‿ ^ )z\n')

def addChoice(): # The "A" choice, for add new tasks#
    clearConsole()

    itemListAdd = input('Name of the item to be added. ("cancel" to return)\n⤷ : ')

    clearConsole()

    if itemListAdd.lower() == 'cancel':
            return print(' Cancelled. (つò_óつ ︵ ┻━┻\n')

    print(' Item Added Successfully. 〳ᵔ‿‿ᵔ〵\n')

    c.execute('DELETE FROM sqlite_sequence WHERE name="tasks"')
    c.execute('INSERT INTO tasks (item, date) VALUES (?, datetime("now"))', (itemListAdd,))

    conn.commit()

def deleteOneChoice(): # The "D" choice, for delete one entry on database #
    if not dbCheck():
        ShowAllItems().nothingInList()
    else:
        clearConsole()
        ShowAllItems().deleteOneText()

        indexToDelete = input('Enter the index of the item you want to delete. ("cancel" to return)\n⤷ : ')

        clearConsole()

        if indexToDelete.lower() == 'cancel':
            return print(' Cancelled. (つò_óつ ︵ ┻━┻\n')

        c.execute(f'SELECT ID FROM tasks WHERE ID = ?', (indexToDelete,))
        selectedId = c.fetchone()

        if not selectedId:
            return print('Invalid index. Please enter a valid index.\n')

        c.execute('SELECT COUNT(*) FROM tasks')
        record_count = c.fetchone()[0]

        c.execute(f'DELETE FROM tasks WHERE ID = ?', (indexToDelete,))
        conn.commit()

        if record_count == 1:
            c.execute('DELETE FROM sqlite_sequence WHERE name="tasks"')
            conn.commit()

        c.execute('SELECT * FROM tasks WHERE ID > ?', (indexToDelete,))
        records_to_update = c.fetchall()

        for record in records_to_update:
            updated_id = record[0] - 1
            c.execute('UPDATE tasks SET ID = ? WHERE ID = ?', (updated_id, record[0]))

        conn.commit()
        print(' Item successfully deleted. ┏(ᴗ_ᴗ)┛┗(ᴗ_ᴗ )┓\n')

def mainFunct(): # the name says it all... #
    ShowAllItems().mainFuncText()

    print(" Schiavo's Task Creator ~ v1.0.0")
    choice = input('Select an option: [A]dd [D]elete [C]lear [E]xit: ')

    if choice.lower() not in ['a', 'd', 'c', 'e']:
        clearConsole()

        print('Choose a correct option')
        print('')

    if choice.lower() == 'e':
        clearConsole()
        return False
    elif choice.lower() == 'c':
        clearChoice()
    elif choice.lower() == 'a':
        addChoice()
    elif choice.lower() == 'd':
        deleteOneChoice()

clearConsole()

print(' ^ Hallo!! ¨ ฅ^•ﻌ•^ฅ\n')

while mainFunct() != False: pass # Loop until the user stop the script #

conn.close() # Close the database when the sript end #