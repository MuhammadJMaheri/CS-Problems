'''outputs usable values of N(cluster size) from 1 to given input.
Using equation N = i^2 + ixj + j^2'''
import math
N = int(input("Enter a maximum for cluster size:"))
max_ij = math.floor(math.sqrt(N))
i = [list(range(max_ij + 1))]
i.reverse()
j = 0
usable_n = []
while j <= max_ij:
    for ic in i:
        calc = ic**2 + ic*j + j**2
        if calc <= N:
            usable_n.append(calc)
    j += 1
    i.pop()
usable_n.sort()
usable_n.pop(0)
print("Usable values of N are:\n", usable_n)
input("Press enter to exit ...")
