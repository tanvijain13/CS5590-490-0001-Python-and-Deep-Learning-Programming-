str="I love playing with python"
split= str.split()
lis=[]
final_string=""

for i in split:
    if i == "python":
        i = "pythons"
    lis.append(i)


for x in lis:
        final_string += x
        final_string += " "

print(final_string)




