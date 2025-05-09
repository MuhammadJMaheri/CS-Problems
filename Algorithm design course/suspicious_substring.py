'''suspicious substring problem'''

STRING, k = (input()).split()
k = int(k)

OUTPUT = 0
for n in range(1, 27):

    UNIQUE_CHARS = 0
    ENOUGH_CHARS = 0

    c = [0] * 128
    L = R = 0

    while R < len(STRING):

        if c[ord(STRING[R])] == 0:
            UNIQUE_CHARS += 1

        c[ord(STRING[R])] += 1

        if c[ord(STRING[R])] == k:
            ENOUGH_CHARS += 1

        while UNIQUE_CHARS > n:

            if c[ord(STRING[L])] == k:
                ENOUGH_CHARS -= 1

            c[ord(STRING[L])] -= 1
            if c[ord(STRING[L])] == 0:
                UNIQUE_CHARS -= 1

            L += 1

        if ENOUGH_CHARS == n:
            OUTPUT = max(OUTPUT, R - L + 1)

        R += 1

print(OUTPUT)
