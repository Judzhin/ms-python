l = []
numCollection = [1, 23, 43, 5, ['L', 'i', 's', 't'], 7, 87]
print(numCollection)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(1)
l.append(55)
b = [24, 65]
print(f"Append two elements {l}")
l.extend(b)
l.insert(2, 33)
print(f"Insert element by index {l}")
l.append(88)
print(l)
l.remove(88)
print(f"Remove by element {l}")
l.pop(1)
print(f"Remove by index {l}")
print(f"Show index by element {l.index(24)}")
print(f"Count by element {l.count(24)}")
