def string_alternative(Str):
    b = ""
    for i in range(len(Str)):

        if (i % 2) == 0:
            b += Str[i] # appending alternate letters
    return b

if __name__ == '__main__': # defining main function
    print(string_alternative(raw_input())) # asking for raw input
