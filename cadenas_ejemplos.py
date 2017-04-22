s = 'Monty Python'
print (s[2]) ## n 
print (s[-2] )## o 
print (s[:6] + s[6:8] + s[8:]) ## Monty Python


##operador%
print  ("%d tigres comen %.1f porción de %s en un %s" % (3, 0.5, 'trigo', 'trigal'))

##Unicode
ustring = u'Hola en chino \u4F60  \u597D ' # ñ \xf1'

## (ustring from above contains a unicode string)
s = ustring.encode('utf-8')
print (s) #equivalente de unicode en UTF8
t = s.decode('utf-8', "strict")         ## Convert bytes back to a unicode string

print(t)                     ## It's the same as the original, yay!

##len
print(len('La vida es mucho mejor con Python.'))
print("La vida es mucho mejor con Pyhon.".find("Python"))
print('Mejor con Python'.replace('Python', 'Jython'))
