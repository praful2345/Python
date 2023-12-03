set1 = {1,2,3}
set2 = {1,2,2,3}

set1.add(0)
print(set1)
set1.update({99,77,66})
print(set1)
set1.discard(99)
print(set1)
sorted_set1 = sorted(set1,reverse=True)
print(sorted_set1)
set1.clear()
print(set1)