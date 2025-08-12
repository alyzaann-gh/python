group1 = set()
group2 = set()
self = set()

for i in range(3):
    groupwan = input("Enter brith month " + str(i+1) + ": ")
    group1.add(groupwan)
    
for j in range(3):
    grouptu = input("Enter birth month " + str(j+1) + ": ")
    group2.add(grouptu)
    
print("Group 1: " , group1)
print("Group 2: " , group2)

selfko = input("Enter your birth month: ")
self.add(selfko)

print("Union: " + str(group1 | group2))
print("Intersection: " + str(group1 & group2))
print("Difference: " + str(group1 - group2))

if(self.issubset(group1 | group2)):
    print("You have the same birth month with one of your classmates.")
else:
    print("You don't have the same birth month with one of your classmates.")