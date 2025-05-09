'''Engineering economics programming project'''
import copy
def func(method, i, no_periods):
    '''Calculates coefficients below'''
    if method == "P/F":
        return 1/(1+i)**no_periods
    if method == "A/P":
        return (i*(1+i)**no_periods)/((1+i)**no_periods-1)
print("## The RoR method and infinte or different periods are not added yet,",
       "OC and GI must be given for each year individually ##")
MARR = int(input("Minimum Attractive Rate of Return (MARR) = "))/100
N = int(input("Number of projects to compare (N) = "))
n = int(input("Number of periods for all projects (n) = "))
P = [0]*N
SV = [0]*N
NPW = [0]*N
NEUA = [0]*N
for p in range(N):
    GI = [[0 for i in range(n)] for j in range(N)]
    OC = [[0 for i in range(n)] for j in range(N)]
for c1 in range(0, N):
    print("Initial cost (P) for project", c1+1," = ")
    P[c1] = int(input())
    print("Sale Value (SV) for project", c1+1," = ")
    SV[c1] = int(input())
    for c2 in range(0, n):
        print("Gross Income (GI) of year", c2+1, " = ")
        GI[c1][c2] = int(input())
        print("Operational Cost (OC) of year", c2+1, " = ")
        OC[c1][c2] = int(input())
print("Select preferred method :\n     ",
        "a)NPW = enter 1\n      b)NEUA = enter 2\n      c)RoR = enter 3 (not available)")
METHOD = int(input())
if METHOD == 1: #NPW method
    for c1 in range(0, N):
        NPW[c1] = -P[c1] + SV[c1]*func("P/F", MARR, n)
        for c2 in range(0, n):
            NPW[c1] += (- OC[c1][c2]*func("P/F", MARR, c2+1)
                        + GI[c1][c2]*func("P/F", MARR, c2+1))
        print("NPW of project", c1+1, "= ", NPW[c1])
    neua = copy.deepcopy(NPW)
    neua.sort()
    greatest = neua[N-1]
    for c1 in range(0, N):
        if NPW[c1] == greatest:
            print("Project", c1+1, "is the preferrable choice.")
if METHOD == 2: #NEUA method
    for c1 in range(0, N):
        NPW[c1] = -P[c1] + SV[c1]*func("P/F", MARR, n)
        for c2 in range(0, n):
            NPW[c1] += (- OC[c1][c2]*func("P/F", MARR, c2+1)
                        + GI[c1][c2]*func("P/F", MARR, c2+1))
        NEUA[c1] = NPW[c1]*func("A/P", MARR, n)
        print("NEUA of project", c1+1, "= ", NEUA[c1])
    neua = copy.deepcopy(NEUA)
    neua.sort()
    greatest = neua[N-1]
    for c1 in range(0, N):
        if NEUA[c1] == greatest:
            print("Project", c1+1, "is the preferrable choice.")
input("Press enter to exit...")
