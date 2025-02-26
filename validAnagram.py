from collections import Counter
a = "lost"
b = "stol"
print(Counter(a) == Counter(b))
c = "racecar"
d = "carrace"
print(Counter(c) == Counter(d))
e = "jam"
f = "jar"
print(Counter(e) == Counter(f))

# output:
# True
# True
# False
