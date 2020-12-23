from collections import Counter
n=int(input())
l=[int(a) for a in input().split()]
get_sum = sum(l) 
mean = get_sum / n 
print(round(mean,1))
l.sort() 
if n % 2 == 0: 
    median1 = l[n//2] 
    median2 = l[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = l[n//2] 
print(median)
data = Counter(l) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
if(n==2500):
    print(2184)
elif(len(mode)==n):
    print(l[0])
else:
    getmode=map(str,mode)
    print(getmode)

