l = [3,4,2,5,1]
s = 1
for item in l:
  if item == s:
    s += 1
print(len(l) - s + 1)
