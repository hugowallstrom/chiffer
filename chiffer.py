word = ""
key = 53
letters = []
crypt = []
meny = 0


while meny != 5:
    try: 
        meny = int(input("\n 1. Kryptera \n 2. Decryptera \n 3. Ändra fras för krytpering \n 4. Ändra krypterings nyckel. \n 5. Avsluta \n Välj:"))
    except:
        print("använd siffra!")
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
        letters = []
        crypt = []
    
    elif meny == 2:
        if word == "":
            print("Ingen fras hittades.")
        else:
            for letter in word:
                letters.append(ord(letter) + key) 
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
        break
    else:
        print("Fel siffra, försök igen.")