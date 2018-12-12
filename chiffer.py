word = ""
key = 12
letters = []
crypt = []
meny = 0


while meny != 6:
    try: 
        meny = int(input("\n 1. Kryptera \n 2. Decryptera \n 3. Ändra fras för krytpering \n 4. Ändra krypterings nyckel \n 5. Rensa fras och krypterad fras \n 6. Avsluta \n Välj:"))
    except:
        print("Använd siffra!")
        meny = 0
    if meny == 1:
        if word == "":
            print("Ingen fras hittades.")
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)
        for l in letters:
            crypt.append(chr(l))
        print(crypt)
    elif meny == 2:
        if word == "":
            print("Ingen fras hittades.")
        if letters == []:
            print("Kryptering tom")
        else: 
            for l in letters:
                crypt.append(chr(l -key))
        print(crypt)
    elif meny == 3:
        word = input("Skriv in ord eller fras: ")
        print("Fras ändrad.")
    elif meny == 4:
        key = int(input("Ange nyckel siffra för kryptering: "))
        print("Nyckel ändrad.")
    elif meny == 5:
        letters = []
        crypt = []
        print("Kryptering rensad.")
    else:
        print("Fel, försök igen.")