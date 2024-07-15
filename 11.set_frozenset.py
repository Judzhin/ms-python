a = set ("hello")
print (f"Show type a: {type(a)}")
print (f"dump a: {a}")

b = {'23': 32} # wrong
print (f"Show type b: {type(b)}")
print (f"dump b: {b}")

c = {i ** 2 for i in range(10)}
print (f"Show type c: {type(c)}")
print (f"dump c: {c}")

d = frozenset ("Qwerty")
a.add(1)
print(f"dump a: {a}")
print(f"dump b: {b}")

e = ['r', 's', 'w', 'a', 's', 'w']
print (f"dump e: {e}")
print (f"dump set e: {set(e)}")

f = {23, 34, 45.45, 66}
print (f"Show length: {len(f)}")

x = 34
print (f"Show logic: {x in f}")
y = 44
print (f"Show logic: {y in f}")

h = {44, 55, 77}
print (f"Show logic: {f.isdisjoint(h)}")
print (f"Show logic: {f == h}")
f.update(h)
print (f"dump: {f}")
