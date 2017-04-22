name=input("Ingrese su nombre y apellido completo: ")
firstname ,lastname =[x for x in name.split(' ')]

print(">->->->->->->->->->->->->->->->->->")
print(">                                 >")
print(">    BOARDING PASS VALIDATION     >")
print(">                                 >")
print(">->->->->->->->->->->->->->->->->->")
print("")

print(" ____________________________________")
print("|                                    |")
print("|  Passenger Details:                |")
print("|    Firstname:                      |")
print("|    >  " + firstname+ (37-8- len(firstname))*" " + "|" )
print("|    Lastname:                       |")
print("|    >  " + lastname + (37-8- len(lastname))*" " + "|" )
print("|                                    |")
print("|  Flight Details:                   |")
print("|                                    |")
print("|____________________________________|")


