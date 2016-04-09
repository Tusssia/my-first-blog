print ("hello Django girls!")
a = 45
b = 15
if a > b:
    print('a jest większe od b')
elif b< a:
    print('b mniejsze od a')
else:
    print("a jest większe rowne b")

name = "Marta"
if name=='Ola':
    print ("działa Ola!")
elif name=='Gosia':
    print("działa Gosia!")
else:
    print ("te imiona nie działają")

print ("A teraz jedziemy z głośnością!!!!")
glos = 57;

if glos>=100:
    print("Bardzo głośno")
elif glos<100 and glos>50:
    print("Srednio glosno")
else:
    print("Cicho")

def moja_pierwsza_funkcja():
    print ("to jest moja pierwsza funkcja!!!!")

moja_pierwsza_funkcja()

name = "Ola"

def moja_druga_funkcja(name):
    if name=='Ola':
        print ("działa Ola!")
    elif name=='Gosia':
        print("działa Gosia!")
    else:
        print ("te imiona nie działają")

moja_druga_funkcja(name)

dziewczyny = ["Ola", "Marta"+"Anna"]

def hej (imie):
    print ("hej " + imie + "!")

for imie in dziewczyny:
    hej(imie)

hej(imie)

for i in range(3,15):
    if i>=13:
        print(i)
    else:
        pass

for n in range (3,18,2):
    print(n)
