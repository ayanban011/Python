t=int(input())
for i in range(1,t+1):
    pswrd=input()
    if any(all(b[0] == b[i] for i in range(len(b))) for b in [[pswrd[c], pswrd[c+1]] for c in range(len(pswrd)-1)]):
        print("hi")
            
