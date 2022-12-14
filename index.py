# Global variables
countLine = 0
lista = []

# Text request
def listText():
    lista = input('Start your list ~> ')
    inputInFile(lista)


# Write in the list
def inputInFile(lista):
    global countLine
    countLine += 1
    saveList = open('list.sv','a')
    saveList.writelines(f'{countLine} ' + str(lista) + '\n')
    saveList.close()
    deleteInFile()

# Delete list elements
def deleteInFile():
    listElement = open('list.sv','r')
    DeleteElements = listElement.readlines()

# While to remove lines
    for Line in DeleteElements:
        global lista
        lista.append(Line)
        print(lista)
    
    removing = input('Remove some thing ~> ')
    lista.pop(int(removing))
    print(lista)
    listElement.close()
    addingAgain(lista)

# Add elements to the list
def addingAgain(lista):
    addAgain = open('list.sv', 'w')
    for line in lista:
        addAgain.writelines(line)
    addAgain.close()

listText()