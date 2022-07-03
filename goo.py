from dataclasses import replace
from re import I


a=5
b=5
c=16
n=total_numbers=3
average=(a+b+c)/n
print(average)


sentence="i love pizza"
capitalize_string= sentence.capitalize()
print(capitalize_string)


text="I am learning python"
new_text= text.replace("I","You", 1)
print(new_text)


g="I hope you had fun today in class"
print(g.count("a"))



def check_fermat(a,b,c,n):
    if c==((a**n)+(b**n))**(1/n):
        if a>0 and b>0 and n>2 and c>0:
           print("Holy smokes Fermat was wrong!")
        else:
            print("No, that doesn't work.")
    else:
        print("No, that doesn't work.")

a=int(input("Enter Integer:"))
b=int(input("Enter Integer:"))
c=int(input("Enter Integer:"))
n=int(input("Enter power:"))

check_fermat(a,b,c,n)


