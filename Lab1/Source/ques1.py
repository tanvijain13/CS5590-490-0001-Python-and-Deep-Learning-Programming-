def subset(a, n):
    # List is declared
    l = []

    for i in range(2 ** n):
        subset = ""
        # consider each element in the set
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset += str(a[j]) + " "
        # if subset is encountered for the first time
        if subset not in l and len(subset) > 0:
            l.append(subset)
            # consider every subset
    for subset in l:
        # split the subset and print its elements
        a = subset.split(' ')
        for string in a:
            print(string, end=" ")
        print()

if __name__ == '__main__':
    a = [1, 2, 2]
    n = len(a)
    subset(a, n)
