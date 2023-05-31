# 1.a
n = int(input("enter un nombre:"))
if n%2 == 0:
  print(n, "est un nombre pair.")
else:
  print(n, "est un nombre impaire.")

# 1.b
k = int(input("entrer un nombre:"))
if k>0:
  print(k, "est positive.")
elif k<0:
  print(k, "est negative.")
else:
  print(k, "est nul.")

# 2.a
for i in range(1, 11):
  print(i)

# 2.b
s = 0
for m in range(1, 101):
  s += m
print("la somme de 1 à 100 est:", s)

# 3.a
while True:
  user = input("Entrez des mots (ou 'stop' pour arrêter) : ")
  print("tu es écrit:", user)
  if user == "stop":
    break

# 3.b
g = 0
while True:
  h = int(input("entrer un nombre (ou un nombre négatif pour arrêter):"))
  g += h
  if h < 0:
    break
print("la somme des nombres positives est :", g)

# 4.a
for c in range(1, 11):
  print(c)
  if c%2 == 0:
    break

# 4.b
import random
nombre_aleatoire = random.randint(1, 100)
nb_coups = 0
while True:
  nombre_devine = int(input("Devinez un nombre entre 1 et 100 : "))
  nb_coups += 1
  if nombre_devine < nombre_aleatoire:
    print("Trop petit !")
  elif nombre_devine > nombre_aleatoire:
    print("Trop grand !")
  else:
    print(f"Bravo ! Vous avez gagné en {nb_coups} coups.")
    choix = input("Voulez-vous rejouer ? (o/n) : ")
    if choix == "o":
      nombre_aleatoire = random.randint(1, 100)
      nb_coups = 0
    else:
      break

# 5.a
for s in range(1, 11):
  if s == 7:
    continue
  print(s)

# 5.b
somme = 0

while True:
    nombre = int(input("Entrez un nombre positif (ou un nombre négatif pour arrêter): "))
    if nombre < 0:
        break
    somme += nombre

print("La somme des nombres positifs est :", somme)

# 7.a
def carre(nombre):
  return nombre**2
  
nombre = int(input("entrer un nombre:"))
resultat = carre(nombre)
print("le carré de", nombre, "est:", resultat)

# 7.b
def est_majeur(age):
  if age > 18:
    return True
  else:
    return False

age = int(input("entrer votre age:"))
resltat1 = est_majeur(age)
print(resltat1)

# 8.a
def somme(a, b):
  return a + b

a = int(input("entrer le nombre de a:"))
b = int(input("entrer le nombre de b:"))
#resultat3 = somme(a, b)
print("la somme de", a, "et", b, "est:", somme(a, b))

# 8.b
def maximum(ls):
    if len(ls) == 0:
        return None
    max_nombre = ls[0]
    for nombre in ls:
        if nombre > max_nombre:
            max_nombre = nombre
    return max_nombre

nombres = input("Entrez une liste de nombres séparés par des espaces : ")
liste = [int(nombre) for nombre in nombres.split()]
print("Le maximum de la liste", nombres, "est :", maximum(liste))

# 9.a
def factorielle(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat
while True:
  p = int(input("entrer un nombre (ou '0' pour arrêter):"))
  w = factorielle(p)
  print("La factorielle de", p, "est :" ,w)
  if p == 0:
    break

# 9.b
def est_palindrome(mot):
  mot_inverse = mot[::-1]
  if mot == mot_inverse:
    return True
  else:
    return False

mot = str(input("entrer un mot palindrome:"))
print(est_palindrome(mot))

# 10.a
def fonction_compteur():
    global compteur_appels
    compteur_appels += 1
    print("Nombre d'appels à la fonction :", compteur_appels)

n = int(input("Combien de fois souhaitez-vous appeler la fonction ? "))

for _ in range(n):
    fonction_compteur()
