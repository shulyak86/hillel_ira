dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(dict)
empty_keys = [k for k, v in dict.items() if not v]
for k in empty_keys:
    del dict[k]
print(dict)
