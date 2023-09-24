def generateParenthesis(n):
    slot=n*2
    def generate(m=['']):
        if len(m[0])==slot:return m
        L=[]
        for i in m:
            L.append(i+')')
            L.append(i+'(')
        return generate(L)
    return generate()


def isValid(L):
    op=0
    for i in L:
        if i=='(':
            op+=1
        else:
            if op==0:
                return False
            else:
                op-=1
    return op==0
    
def ans(L1):
    ans=[]
    for i in L1:
        if isValid(i):
            ans.append(i)
    return ans
L1=generateParenthesis(3)
print(ans(L1))

#cach2

def a(n):
    ans=[]
    def genrate1(s='',op=0,cl=0):
        if op>cl:return
        if op<cl:return
        if op==cl==n:
            ans.append(s)
        genrate1(s + '(',op+1,cl)
        genrate1(s + ')',op,cl+1)
    genrate1()
    return ans
    
print(a(3))


def j(n):
    l=[]
    def k(m=3):
        for i in range(n,m):
            l.append(i)
    k()
    return l

print(j(1))



    










