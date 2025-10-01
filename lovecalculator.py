name1=input("Enter your name: ") 
name2=input("Enter your partners name: ")
bothnames=name1+name2
print(bothnames)
small_letters=bothnames.lower()
t=small_letters.count('t')
r=small_letters.count('r')
u=small_letters.count('u')
e=small_letters.count('e')
true=t+r+u+e
l=small_letters.count('l')
o=small_letters.count('o')
v=small_letters.count('v')
e=small_letters.count('e')
love=l+o+v+e
lovescore=int(str(true)+str(love))

if lovescore < 10 or lovescore > 90:
    print("You are made for eachother")
elif lovescore<=40 or loverscore>=50:
    print("You are very lucky to have your partner")
else:
    print("You are the unique couple in the world")
