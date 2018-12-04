word = "hallå"
key = 14
letters = []
crypt = []

meny = int(input("1. Kryptera \n 2. Decryptera \n 3. Ändra fras för krytpering \n 4. Ändra krypterings nyckel. \n 5. Avsluta \n"))

while meny != 5:
    if meny = 1:
        word = input("Skriv in ord eller fras: ")
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)

    if meny = 2: 
        for l in letters:
            crypt.append(chr(l))
        print(crypt)