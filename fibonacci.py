def fibo(x):
    if not isinstance(x,int):
        return None
    if x<=0:
        return None
    if x==1:
        return [0]
    fibo_list=[0,1]
    a=0
    b=1
    for i in range (x-2):
        c=a+b
        a=b
        b=c
        fibo_list.append(c)
    return fibo_list
    