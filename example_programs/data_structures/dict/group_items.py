
# group items in a dictionary
# based on cookbook 4.15

data = [
    ('Felix', 'cat'),
    ('Fido', 'dog'),
    ('Rex', 'dog'),
    ('Mynx', 'cat'),
    ('Wolfie', 'dog'),
    ]

groups = {}
for name, species in data:
    groups.setdefault(species, []).append(name)

print groups
