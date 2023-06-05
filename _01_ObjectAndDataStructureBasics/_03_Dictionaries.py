# {'key1':'value1','key2':'value2'}
# Dictionaries:  Objects retrieved by key name. Unordered and can not be sorted.

# Lists:  Objects retrieved by location. Ordered Sequence can be indexed or sliced.

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict["key1"])
prices_phone = {"apple": 1000, "samsung": 800, "motorola": 400}
print(prices_phone["apple"])
d = {"k1": 1000, "k2": [1, 2, 3], "k3": {'insideKey': 100}}
var1 = d["k2"][2]
var2 = d["k3"]["insideKey"]
print(var1)
print(var2)
print(d.keys())
print(d.values())
print(d.items())
