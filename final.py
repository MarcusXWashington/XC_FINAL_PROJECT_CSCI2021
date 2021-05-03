# Here are all of the strings, exactly as you will need them.
# What, you thought I was going to make you type all that??
SORRY = "Sorry. Try another input! :)"
START_DESC = "You were on a mission to collect data from the Mars criminal testing trials for the scientists back on Earth. On the way back, it became quiet...and everyone else on the ship seem to be missing... Can you make it home without having the same fate as your crewmates?" + '\n' "Enter Start to begin!"
WIN =("\n" + "YOU HAVE WON THE GAME! THE DATA WAS DELIVERED TO EARTH!")
HALLINPUT='Chose your next room or action:' +"\n" +""" - Hallway"""
# Here are some handy constants for recognizing your locations.
Key = "key"
ROOM_START = "Start"
Hallway = "Hall"
Storage = "Storage"
Engine = "Engine"
Admin = "Admin"
Navigation = "Navigation"
Oxygen = "Oxygen"
Electrical ="Electrical"
# And some variables
gamerunning=True
door_open = False
location = ROOM_START
won = False
have_code = False
launched= False
taser=False
elecdooropen=False
hammer= False
Impostor=True
autopilot=False
emergencymode=False
a=[]
player={
    'location': 'Engine',
    'taser':True
}
Impostor={
    'Impostorlocation':'Engine',
    'Impostor':True
}
#Used these from class example
def can_taser_Impostor(player,Impostor):
    if player['location']==Impostor['Impostorlocation']:
        if player['taser']==True:
            if Impostor['Impostor']==True:
                return True
    return False
def can_hammer_Impostor(player,Impostor):
    if player['location']==Impostor['Impostorlocation']:
        if player['hammer']==True:
            if Impostor['Impostor']==True:
                return True
    return False
def can_win_game(autopilot,Impostor):
    if autopilot==True:
        if Impostor==False:
            return True
    return False
#end of class example
# Start by printing the first room description.
print(START_DESC)

# Now we loop until the user finds the treasure!
while not won and gamerunning==True:
    command = input("> ")

    if command == "quit":
        break # This breaks the loop and ends the game.

    if location == ROOM_START:
        if command == "Start":
            if location == ROOM_START:
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[218:293])
                print(HALLINPUT)
                print(' - Look around')
        elif command == "Hallway":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[46:193])
            print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
            print (' - Admin' + '\n' + ' - Engine' )
            print(' - Electrical')
            location= Hallway
        elif command=="Look around":
            print("The Impostor finds you wandering around and decides to go for the kill. I guess curiousity did actually kill the cat!")
            gamerunning=False
        else:
            print(SORRY)
            
    elif location == Hallway:
        if command == "Start":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[218:293])
            print(HALLINPUT)
            location = ROOM_START
        elif command == "Storage":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[805:922])
            print('Chose your next room or action:' +"\n" +""" - Oxyen""")
            print(' - Navigation' +"\n" +""" - Hallway""")
            print(" - Grab gear")
            location = Storage
        elif command == "Admin":
            if have_code==True:
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[465:590])
                print (HALLINPUT)
                print(" - Activate Emergency Mode")
                location= Admin
                
            elif have_code==False:
                print("You need the access code to enter! (You have returned to the hallway)")
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[46:193])
                print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
                print (' - Admin' + '\n' + ' - Engine' )
                print(' - Electrical')
                location= Hallway
                
        elif command =="Engine":
            if taser==True and have_code==True:
                location=Engine
                if can_taser_Impostor(player,Impostor):
                    with open('Room_descriptions','r') as Roomhandle:
                        Descoroom=Roomhandle.read()
                    print (Descoroom[317:433])
                    print("The Impostor jumped out of the vents and attacks you!")
                    command=input("Chose the taser or hammer to protect yourself!: ")
                    if command =="taser":
                        print('You taser the Impostor and launch them away in the escape pod into space! \n - Hallway')
                        Impostor=False
                        launched=True
                    
                    elif command=="hammer":
                        print("You grab the hammer and swing. It hits them in the head and they become unconcious. You drag them on to the escape pod, and send them back to the Mars colony! \n - Hallway")
                        Impostor=False
                        launched=True
                #print (HALLINPUT)
            elif taser==False and have_code==False:
                print("The impostor catches you unprepared and ejects you into space. Game Over!")
                gamerunning=False
            elif taser==True and have_code==False:
                print("The Impostor jumps out to attack you but you taser them and push them into the escpae pod. \n Oh no! You dont have the code to eject the pod!")
                gamerunning=False
            elif taser==False and have_code==True:
                print("The impostor catches you unprepared and ejects you into space. Game Over!")
                gamerunning=False
            
                
        elif command =="Electrical":
            if elecdooropen==True:
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[622:777])
                print (HALLINPUT)
                location= Electrical
            elif elecdooropen==False and hammer==True:
                print('You use the hammer to break the door open!')
                elecdooropen=True
                with open('Room_descriptions','r') as Roomhandle:
                        Descoroom=Roomhandle.read()
                print ("You turn the lights on!")
                location= Electrical
                print("Enter: \n - Hallway")
            elif elecdooropen==False and hammer==False:
                print("This door is jammed, find a way to open it. You have been returned to the Hallway")
                print("\n")
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[46:193])
                print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
                print (' - Admin' + '\n' + ' - Engine' )
                print(' - Electrical')
                location= Hallway
                
        else:
            print(SORRY)
            
    elif location == Storage:
        if command =="Hallway":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[46:193])
            print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
            print (' - Admin' + '\n' + ' - Engine' )
            print(' - Electrical')
            location= Hallway
        elif command == "Oxygen":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[1024:1100])
            print ('Chose your next room or action:' +"\n" +""" - Storage""")
            print(" - Get code")
            location= Oxygen
        elif command =="Navigation":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[950:997])
            print ('Chose your next room or enter a action:' +"\n"  +' - Storage')
            print(" - Autopilot" +'\n'+ ' - Night Travel')
            location= Navigation
            if command=="Autopilot":
                print("Come back here to fix")
        elif command=='Grab gear':
            print("You have picked up a hammer and a taser. These may be useful. Chose the next room!" +'\n'+ ' - Oxygen \n - Navigation \n - Hallway')
            taser=True
            hammer=True
        else:
            print(SORRY)
            
    elif location == Oxygen:
            if command == "Storage":
                with open('Room_descriptions','r') as Roomhandle:
                    Descoroom=Roomhandle.read()
                print (Descoroom[805:922])
                print ('Chose your next room:' +"\n" +""" - Oxygen""" +'\n' +' - Navigation')
                print(" - Hallway")
                location= Storage

            elif command == "Get code":
                print("Solve this Question!" +'\n' "6 X 4 ÷ 12 + 72 ÷ 8 - 9")
                while command == "Get code" and have_code ==False:
                    problem_solve=input("Answer: ")
                    if problem_solve == "2":
                        a.append(problem_solve)
                        #print (a[0])
                        print("The code is 5699 <-----Dont forget this!")
                        have_code= True
                        location=Storage
                        print("(You have been returned to Storage)")
                        #print("\n")
                        with open('Room_descriptions','r') as Roomhandle:
                            Descoroom=Roomhandle.read()
                        print (Descoroom[805:922])
                        print ('Chose your next room:' +"\n" +""" - Oxygen""" +'\n' +' - Navigation')
                        print(" - Hallway")
                    else:
                        print("Try again, Maybe use a calculator")
                    
                
    elif location == Engine:
        if command == "Hallway":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[46:193])
            print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
            print (' - Admin' + '\n' + ' - Engine' )
            print(' - Electrical')
            location= Hallway
        else:
            print(SORRY)
            
    elif location == Admin:
        if command == "Hallway":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[46:193])
            print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
            print (' - Admin' + '\n' + ' - Engine' )
            print(' - Electrical')
            location= Hallway
        elif command =="Activate Emergency Mode" and have_code==True:
            command=input("Enter the code here: ")
            if command=="5699":
                emergencymode=True
                print("You have triggered the Emergency Mode. Please engage Navigation systems! \n - Hallway")
            else:
                print(SORRY)
        elif command=="Activate Emergency Mode" and have_code==False:
            print("Please retrieve the access code to activate Emergency Mode.")
        else:
            print(SORRY)
            
    elif location ==Electrical:
        if command == "Hallway":
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[46:193])
            print ('Chose your next room:' +"\n" +""" - Start""" +'\n' +' - Storage')
            print (' - Admin' + '\n' + ' - Engine' )
            print(' - Electrical')
            location= Hallway
        elif command =="Open door" and hammer==True:
            print("You have gained access to the Electrical room, the lights are on!")
            location=Electrical 
            elecdooropen=True
        elif command =="Open door" and hammer==False:
            print("The door is still jammed. Get something to help open it")
        else:
            print(SORRY)
            
    elif location == Navigation:
        if command == "Storage":
            location=Storage
            with open('Room_descriptions','r') as Roomhandle:
                Descoroom=Roomhandle.read()
            print (Descoroom[805:922])
            print ('Chose your next room:' +"\n" +""" - Oxygen""" +'\n' +' - Navigation')
            print(" - Hallway")
        elif command =="Autopilot" and emergencymode==True:
                command=input("What year were you born?: 1977 1971 2004 2008  ")
                if command=="2008":
                    if launched==True:
                        print('Hello Capt. Taylor, Welcome aboard! Emergency Autopilot has been engaged and the destination has been set to Earth.')
                        print(WIN)
                        autpilot=True
                        gamerunning=False
                    elif launched==False:
                        print("There is a stranger on board captain. We can not return with them on the ship! Go back to storage and then go find them")
                elif command=="2004":
                    if launched==True:
                        print("Hello Capt. Leia, Welcome aboard! Emergency Autopilot has been engaged and the destination has been set to Earth.")
                        print(WIN)
                        autpilot=True
                        gamerunning=False
                    elif launched==False:
                        print("There is a stranger on board captain. We can not return with them on the ship! Go back to storage and then go find them")
                elif command=="1977":
                    if launched==True:
                        print("Hello Capt. Momma, Welcome aboard! Emergency Autopilot has been engaged and the destination has been set to Earth.")
                        print(WIN)
                        autpilot=True
                        gamerunning=False
                    elif launched==False:
                        print("There is a stranger on board captain. We can not return with them on the ship! Go back to storage and then go find them")
                elif command=="1971":
                    if launched==True:
                        print("Hello Capt. Father, Welcome aboard! Emergency Autopilot has been engaged and the destination has been set to Earth.")
                        print(WIN)
                        autpilot=True
                        gamerunning=False
                    elif launched==False:
                        print("There is a stranger on board captain. We can not return with them on the ship! Go back to storage and then go find them")
        else:
            print("Make sure there is only crewmates on board and emergency mode is activated!")
            
    else:
        print(SORRY)
