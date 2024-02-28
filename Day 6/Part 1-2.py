# theedoo originale version (this one does not works)
tt1 = 66
button1 = 0
time1 = tt1-button1
x1 = 0
for button1 in range(tt1):
    distance1 = time1 * button1
    if distance1 > 1041:
        x1 = x1 + 1
# -----------------------------------------------
# dooe fix version (this one works)
tt = 66
x = 0
for button in range(tt):
    time = tt - button
    distance = time * button
    if distance > 1041:
        x = x + 1
