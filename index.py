
# Global variables
lista = []

# Text request
def listText():
    lista = input('Start your list ~> ')
    if lista == 'exit':
        exit()
    elif lista == 'del':
        deleteInFile()
    else:
        inputInFile(lista)

# Write in the list
def inputInFile(lista):
    global countLine
    saveList = open('list.sv','a')
    saveList.writelines('[] ' + str(lista) + '\n')
    saveList.close()
    listText()

# Delete list elements
def deleteInFile():
    global lista
    lista.clear()
    listElement = open('list.sv','r')
    DeleteElements = listElement.readlines()

# While to remove lines
    for Line in DeleteElements:
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
        addAgain.write(line)
    addAgain.close()

while True:
    listText()
