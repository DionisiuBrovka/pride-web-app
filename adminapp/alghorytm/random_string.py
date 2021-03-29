import random

def get_random_string(n):
    s = ''

    while len(s)<=n:
        a = random.randint(0,35)
        if (a<26):
            if random.randint(0,1):
                s += chr(97+a)
            else:
                s += chr(65+a)
        else:
            s += str(a-26)
    
    return (s)


