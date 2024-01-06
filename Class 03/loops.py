student_data=['Hujur','Asam','Tahseen','Shoaib','Saniah','Khadija','Atlaha','Batool','Ahmed','Tahir','Faisal','Danish']
'''for ali in student_data:
    print(ali+'s')'''
'''serach_name=input('enter')
if serach_name in student_data:
    print('Maujood ha')
else:
    print('Nahi ha bhai')
'''

start_letter=input('Enter')
for name  in student_data:
    if name.startswith(start_letter):
        print(name)
    

#start_letter_name=[name for  name in student_data if name.startswith(start_letter)]
#print(start_letter_name)


'''mix_length=6
for h in student_data:
    if len(h)>mix_length:
        print(h)'''
#longs_name=[h for h in student_data if len(h)>mix_length]
#print(h)
#print(longs_name)





