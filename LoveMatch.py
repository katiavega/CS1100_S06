
print("*****************************")
print("*   Love Match Calculator   *")
print("*****************************")

#Retrieve User Inputs
name1=input("Ingrese el primer nombre:")
name2=input("Ingrese el segundo nombre:")
name1=name1.lower()
name2=name2.lower()

#Initialise key variables
score=0
vowels="aeiouy"
consonants="bcdfghjklmnpqrstvwxyz"
vowelsInName1=0
vowelsInName2=0

#Check if both names have the same number of characters
if len(name1)==len(name2):
  score = score + 20
  print("20 puntos por longitud de nombres")

#Check if both names start with a vowel
if (name1[0] in vowels and name2[0] in vowels):
    score = score + 10
    print("10 puntos comenzar con la misma vocal")


#Check if both names start with a consonant
if (name1[0] in consonants and name2[0] in consonants):
    score = score + 10
    print("10 puntos comenzar con la misma consonante")

#finding letters l o v e
#l
if (name1.find("l") != -1 and name2.find("l")!= -1):
    score = score + 7
    print("7 puntos la letra l")
#o
if (name1.find("o") != -1 and name2.find("o") != -1):
    score = score + 7
    print("7 puntos la letra o")
#v
if (name1.find("v")!= -1 and name2.find("v")!= -1):
    score = score + 7
    print("7 puntos la letra v")
#e
if (name1.find("e") != -1 and  name2.find("e")!= -1):
    score = score + 7
    print("7 puntos la letra e")


#Puntaje
print("Tu puntaje de amor es: " + str(score))
