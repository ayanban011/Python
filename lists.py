if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        ip = input().split()
        if(len(ip)==1):
            s = ip[0]
        elif(len(ip)==2):
            s = ip[0]
            val = int(ip[1])
        elif(len(ip)==3):
            s = ip[0]
            pos = int(ip[1])
            val = int(ip[2])
        #s = input()
        if(s == 'insert'):
            #pos,val = map(int,input().split())
            l.insert(pos,val)
        elif(s=='append'):
            #val = int(input())
            l.append(val)
        elif(s=='remove'):
            #val = int(input())
            l.remove(val)
        elif(s=='print'):
            print(l)
        elif(s=='sort'):
            l.sort()
        elif(s=='pop'):
            l.pop()
        elif(s=='reverse'):
            l.reverse()
