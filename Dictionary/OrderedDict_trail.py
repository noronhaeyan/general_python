from collections import OrderedDict

d = {'a': 1, 'b': 2, 'c': 3}

print("Regular dict:")
for k, v in d.items():
    print(k, v)

print("OrderedDict:")
od = OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3)])
for k, v in od.items():
    print(k, v)

# Does inserting new values to exisiting key change the order?
# Answer: NO
d['b'] = 20
print("After updating 'b' in regular dict:")
for k, v in d.items():
    print(k, v)

od['b'] = 20
print("After updating 'b' in OrderedDict:")
for k, v in od.items():
    print(k, v)

# Does popping an item and adding them change the order?
# Answer: YES

d.pop('b')
d['b'] = 30
print("After updating 'b' in regular dict:")
for k, v in d.items():
    print(k, v)

od.pop('b')
od['b'] = 30
print("After updating 'b' in OrderedDict:")
for k, v in od.items():
    print(k, v)

# deleting the first key inserted in dict
for _key, _value in d.items():
    d.pop(_key)
    break
d[_key] = _value
print("After deleting and re-adding the first key in regular dict:")
for k, v in d.items():
    print(k, v)