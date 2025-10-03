list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
k=set(list)
print(k)
k.add(12)
k.add(12)
print(k)


dict={
    "model":"1st model",
    "year":2021,
    "age":25
}
print(type(dict))
print(dict['model'])
dict['city']='Hyderabad'
print(dict)

def mom (a,b):
    return a+b
    
a=10
b=20
c=mom(a,b)
print(c)
d=mom(5,6)
print(d)
e=mom(a,b)
print(e)
f=mom(5,6)
print(f)
