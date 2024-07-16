a = {'color': 'blue', 'shape': 'square', 'volume': 40}
print(a)

b = dict(color='red', edges=4, perimeter=15)
b['perimeter'] = 30
print(b)

c = dict([(23, 34), (33, 56)])
print(c)

d = dict.fromkeys(['a', 'b'], 1)
print(d)

e = {a: a ** 2 for a in range(7)}
print(e)

person = {
    'name': {
        'last_name': 'Ivanov',
        'first_name': 'Ivan',
    },
    'address': ['c. Bila Tserkva', 'str. Heroiv 72']
}

print(person['name']['last_name'])

# person.clear ()
print(person.values())
print(person.keys())
