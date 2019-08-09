def print_formatted(number):
    # your code goes here
    width = len(format(number,'b'))
    for i in range(number):
        i += 1
        print(str(i).rjust(width),str(format(i,'o')).rjust(width),str(format(i,'X')).rjust(width),str(format(i,'b')).rjust(width))
