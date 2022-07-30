import random
import string

chars = string.ascii_letters + string.punctuation + string.digits
print("Générateur de mot de passe")

b = int(input("Choisissez le nombre de mot de passe à générer: "))
a = random.randint(11,14)

print('\nVoice votre mot de passe:')

for pwd in range(b):
    password = ''
    for c in range(a):
        password += random.choice(chars)
    print(password)

 


