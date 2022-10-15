def func2(x,y,z):
    return((-1)**(x+y+z+1))/((x**2+y**2+z**2)**(1/2))
def func3(x,y,z):
    return 1/((x**2+y**2+z**2)**(1/2))**9
def func1(n):
    return (-1)**(n+1)/n
def sumA(m):
    p1=0
    for x in range(-m,m+1):
            for y in range(-m,m+1):
                    for z in range(-m,m+1):
                            if x==0 and y==0 and z==0:
                                continue
                            elif (x**2+y**2+z**2)**(1/2)>m:
                                continue
                            else:
                                p1+=func2(x,y,z)
    return p1

def sumB(m):
    res=0
    for x in range(-m,m+1):
            for y in range(-m,m+1):
                    for z in range(-m,m+1):
                            if x==0 and y==0 and z==0:
                                continue
                            else:
                                res+=func2(x,y,z)
                                # print(x,y,z)
    return res
def sumC(m):
    res=0
    for x in range(-m,m+1):
            for y in range(-m,m+1):
                    for z in range(-m,m+1):
                            if x==0 and y==0 and z==0:
                                continue
                            else:
                                res+=func3(x,y,z)
                                # print(x,y,z)
    return res
# res=0
# for i in range(1,1000):
#     res+=func1(i)
# res1=sumA(97)
# res2=sumA(98)
# res3=sumA(99)
# print(res1)
# print(res2)
# print(res3)
# res4=sumC(100)
# print(res4)

import scipy.constants as cst
a=cst.e**2/(4*cst.pi*cst.epsilon_0)
rs=a*1.748/(9*6.629)
print(rs)