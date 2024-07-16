l = [34, 'sd', 56, 34.34]
print(l[0])
print(l[-1])  # start from end

i = 0
while i < 4:
    print(l[i])
    i += 1

# item[START:STOP:STEP]
print(l[:])
print(l[1:])
print(l[:3])
print(l[::2])
print(l[-2::-2])
