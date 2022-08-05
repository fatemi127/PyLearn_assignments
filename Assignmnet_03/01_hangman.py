import random
words_bank = ["book","moon","tree","sadjad","python","apple","corona","cook","university","student","fatemi","mashhad"]

rword = random.choice(words_bank)

user_correct_chars = []
joon = 6
while True:
    for i  in range (len(rword)):
        if rword[i] in user_correct_chars:
            print (rword[i],end="")
        else:
            print("-", end ="")
    char = input ("\nEnter The char:\n")
    if char.isupper():
        char = char.lower() #تبدیل حروف بزرگ به حروف کوچک
    if char  in rword:
        user_correct_chars.append(char)
        a = list(set(user_correct_chars)) 
        b = list(set(rword))
        if a == b:
            print ("Excelent! You win!")
            break
        else:
            print("✅")
    else:
        joon = joon - 1
        print("❌")

    if joon == 0:
        print ("Game Over! Try again.")
        break
    