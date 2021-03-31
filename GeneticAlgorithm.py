import random
import math
chromosome = ["01101", "11000", "01000", "10011"]

chromosome_length = len(chromosome)
list = []
x = []
new = []

def decimal(c):
    x = 0
    for i in range(len(c)):
        d = c.pop()
        if d == 1:
            x = x + pow(2, i)
    return x


for i in range(chromosome_length):
    for p in chromosome[i]:
        list.append(int(p))
    x.append(decimal(list))


f1 = pow(x[0], 2)
f2 = pow(x[1], 2)
f3 = pow(x[2], 2)
f4 = pow(x[3], 2)
total = f1 + f2 + f3 + f4
average = total/len(chromosome)
max = max(f1, f2, f3, f4)
print("Initial Population(Chromosome): ", chromosome)
print("X-value(Phenotype): ", x[0], x[1], x[2], x[3])
print("Fitness Score: ", f1, f2, f3, f4)
print("Total Fitness Score: ", total)
print("Average Fitness Score: ", math.ceil(average))
print("Maximum Fitness Score: ", max)

p1 = round((f1/total), 2)
p2 = round((f2/total), 2)
p3 = round((f3/total), 2)
p4 = round((f4/total), 2)
ptotal = round((total/total), 2)
pavg = round((average/total), 2)
pmax = round((max/total), 2)
print("Probability: ", p1, p2, p3, p4, ptotal, pavg, pmax)

b1 = round(random.uniform(0,p1),2)
b2 = round(random.uniform(p1,p1+p2),2)
b3 = round(random.uniform(p1+p2,p2+p3),2)
b4 = round(random.uniform((p2+p3),(p3+p4)),2)
print(b1,b2,b3,b4)
print(type(p1))
if(b1 <= p1):
    n1 = "01101"
    new.append(n1)
if(p1 >= b2 <= (p1+p2)):
    n2 = "11000"
    new.append(n2)
    if(p1 >= b3 <= (p1+p2)):
        n2 = "01000"
        new.append(n2)
if((p1+p2) >= b3 <= (p2+p3)):
    n3 = "01000"
    new.append(n3)
if((p2+p3) >= b4 <= (p3+p4)):
    n4 = "11000"
    new.append(n4)
else:
    print("message")

print(new)
