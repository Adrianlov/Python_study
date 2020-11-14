comand = ""
started = False
while comand != 'Quit':
    comand = input("> ").lower()
    if comand == "start":
        if started:
            print('The car is allready started')
            while True:


                print('The car hast started')
    elif comand == 'stop':
        print("The car has stoped")
    elif comand == 'help':
        print("""
        
Start - The car will start
Stop - The car will stop
Quit - End game""")

    else:
        print('I dont understand this')







