import numbers
import re
from statistics import mean


def average (n):
    A=sum(numbers)/len(numbers)
    return A



def median (n):
    numbers.sort()
    y=len(numbers)
    print(y)








def variance(n):
    i=str(input("Enter type of variance(Sample):"))

    if i == "Sample":
        mean=average(numbers)
        s=[]
        for a in numbers:
            a-=mean
            a=a**2
            s.append(a)
        b=sum(s)
        v=(b/n)
        return v
    else:
        mean=average(numbers)
        s=[]
        for a in numbers:
            a-=mean
            a=a**2
            s.append(a)
        b=sum(s)
        v=(b/n)
        return v






def standard_deviation(n):
    i=str(input("Enter type of Standard Deviation(Sample):"))

    if i == "Sample":
        mean=average(numbers)
        s=[]
        for a in numbers:
            a-=mean
            a=a**2
            s.append(a)
        b=sum(s)
        v=(b/(n-1))**(0.5)
        return float(v)
    else:
        mean=average(numbers)
        s=[]
        for a in numbers:
            a-=mean
            a=a**2
            s.append(a)
        b=sum(s)
        v=(b/(n-1))**(0.5)
        return float (v)





def skew(n):
    mean=average(numbers)
    s=[]
    for a in numbers:
        a-=mean
        a=a**3
        s.append(a)
    b=sum(s)
    try:
        x=standard_deviation(numbers)
        v=(b/(n)-1)*((x)**3)
        return v
    except Exception:
        print("No skew found")