def minion_game(string):
    vowel = {'A','E','I','O','U'}
    kevin = 0
    stuart = 0
    
    for i in range(len(string)):
        if string[i] in vowel:
            kevin += len(string) - i
        else:
            stuart += len(string) -i

    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin < stuart:
        print("Stuart",stuart)
    else:
        print("Draw")