import re
pattern = r'^(4|5|6)(\d){3}[-]?(\d){4}[-]?(\d){4}[-]?(\d){4}$'


for i in range(int(input())):
    string = input()
    v = re.match(pattern,string)
    if v == None:
        print("Invalid")
    
    else:
        v2 = re.split(r'-',v.group())
        v3 = ''.join(v2)
        res = re.search(r'(00|11|22|33|44|55|66|77|88|99)\1',v3)
        if res == None:
            print("Valid")
        else:
            print("Invalid")