'''a=[1,2,3,4,5]
a[0]=2
print(a)
'''

my={
    'name':'Hasan',
    'age':22,
    'f_name':'ali',
    'education':'inter pass'
    }
#print(my['f_name'],my['education'])
my['f_name']='akbar'

my['hobby']='reading book'
del my['f_name']

#print(my.items())
'''for i in my.items():
    print(i)
'''
my_new={
    'a':1,
    'b':2
    }
merge_dictionary=my+ my_new
print(merge_dictionary)




