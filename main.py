selection = 13


def mainMenu():
    print("1. Show all records.")
    print("2. Show one record.")
    print("3. Create new record")
    print("4. Update record")
    print("5. Delete record.")
    print("6. Exit Program.")
    selection = int(input("Enter choice: "))

    while selection != 6:

        if selection == 1:
            showAll()
        elif selection == 2:
            showOne()
        elif selection == 3:
            createNew()
        elif selection == 4:
            update()
        elif selection == 5:
            delete()
        else:
            print("Enter a valid selection")
            mainMenu()


def showAll():
    print("Showing all records")



    mainMenu()


def showOne():
    print("Showing one record")
    mainMenu()


def createNew():
    print("Creating a new record")
    mainMenu()


def update():
    print("Updating record")
    mainMenu()


def delete():
    print("Deleting record")
    mainMenu()


mainMenu()
