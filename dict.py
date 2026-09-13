keys=input("enter the keys: ").split()
values=list(map(int,input("enter the values").split()))
d={}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print("\ndictionary=", d)
values_list=list(d.values())
values_list.sort()
sorted_d={}
for v in values_list:
    for k in d:
        if d[k] == v and k not in sorted_d:
            sorted_d[k] = v
print("sorted list", sorted_d)
keys2=input("enter the keys: ").split()
values2=list(map(int,input("enter the values").split()))
d2={}
for i in range(len(keys2)):
    d2[keys2[i]] = values2[i]
merged = d.copy()
merged.update(d2)
print("merged dictionary", merged)
text = input("enter a text")
f={}
for ch in text:
    if ch in f:
        f[ch]+=1
    else:
        f[ch]=1
print("frequency", f)
set1=set(map(int,input("eneter the elements of set1").split()))
set2=set(map(int,input("eneter the elements of set2").split()))
print("common elements:", set1.intersection(set2))
print("unique elements", set1.symmetric_difference(set2))