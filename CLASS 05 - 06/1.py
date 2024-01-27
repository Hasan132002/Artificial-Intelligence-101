features = ('machine learning', 'natural language processing', 'computer vision', 'deep learning')
data_one,data_two,data_three,data_four=features
#print(len(features))



'''b=((1,1),(1,2),(3,4))
c=dict(b)
#print(type(b))
print(b)'''
x={'a':1,'b':2,'c':3}
'''for z in x.values():
    print(z[1])'''
print(x.items())
z=list(x.items())[1]
print(z)


count=0
for key ,value in x.items():
    count+=1
    if count==2:
        second_pair=(key,value)
        break
print(second_pair)
















'''a={"a":1,"b":2,"c":3}
b={"d":1,"e":2,"f":3}
x=(1,2,3,4,5,6)
y=(6,7,8,9)
z=x+y
print(z)
c={**a,**b}
print(c)'''


