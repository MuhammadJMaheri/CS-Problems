'''longest substring problem'''
STRING = input()

l = len(STRING)
OUTPUT = ''

for i in range(l):
    ss = set()

    for j in range(i, l):
        ss.add(STRING[j])

        if (
            all(c.lower() in ss and c.upper() in ss for c in ss)
            and len(OUTPUT) < j - i + 1
        ):
            OUTPUT = STRING[i : j + 1]

print(OUTPUT)
