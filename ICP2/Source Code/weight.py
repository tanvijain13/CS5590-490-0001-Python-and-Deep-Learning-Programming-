N= int(input("Enter number of students"))
wt_lbs=list()
for _ in range(N):
    # appending weight in lbs in the list
    wt_lbs.append(float(input("Enter weight in lbs")))

wt_kg=list()
'''
for x in range(N):
    wt_kg.append(wt_lbs[x]*0.454)
'''
for x in wt_lbs:
    wt_kg.append(x*0.454) #coverting lbs to kg
print(wt_kg)
