def print_rangoli(size):
    # your code goes here
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(size,0,-1):
        print('-'.join([j for j in alphabet[size-1:i-1:-1]]+[j for j in alphabet[i-1:size]]).center(4*(size-1)+1,'-'))
    for i in range(2,size+1):
        print('-'.join([j for j in alphabet[size-1:i-1:-1]]+[j for j in alphabet[i-1:size]]).center(4*(size-1)+1,'-'))

#3 -> 5x9 -> 2*3-1 x (2*3-1)*(4*(3-1))+1)
#5 -> 9x17 -> 2*5-1 x (2*5-1)*((4*(5-1))+1)
#10 -> 19x37 -> 2*10-1 x (2*10-1)*((4*(10-1))+1)
