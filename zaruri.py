"""
ZARURI
"""

N = int(input())  # in this line I will store the number of lines

faces = []

for i in range(N):
    elements = input().split()
    faces.append([int(num) for num in elements])

#print("Ati introdus: ")
#for elements in faces:
#    print(elements)

total_sum = N * 21
visible_sum = sum(sum(elements) for elements in faces)
unseen_sum = total_sum - visible_sum

print(unseen_sum)

