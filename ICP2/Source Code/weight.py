N= int(input("Enter number of students"))
wt_lbs=list()
for _ in range(N):
    wt_lbs.append(float(input("Enter weight in lbs")))

wt_kg=list()
'''
for x in range(N):
    wt_kg.append(wt_lbs[x]*0.454)
'''
for x in wt_lbs:
    wt_kg.append(x*0.454)
print(wt_kg)
