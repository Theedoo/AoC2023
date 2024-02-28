import regex
i = 0
y = 0
f = open("input.txt", "r")
while i < 1000:
    w = (f.readline())
    o = regex.findall("1|2|3|4|5|6|7|8|9", w)
    r = str(o[0])
    d = str(o[len(o) - 1])
    s = str(r+d)
    l = int(s)
    y = y+l
    i += 1
print(y)
