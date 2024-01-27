'''target_value=8
current_guess=0
attempt=0
while(current_guess!=target_value):
    current_guess=eval(input("Enter the number from 1-25"))
    attempt+=1
    if current_guess<target_value:
        print("chota number dala ha bara try krien")
    elif current_guess>target_value:
        print("bara number dala ha chota try krien")
    else:
        print("Behtreen")
print(f"you have clear this test in {attempt} attempts")
        
    
'''    
number=[1,2,3,4,5,9]
index=0
sum_of_number=0
while index<len(number):
    sum_of_number+=number[index]
    index+=1
print(sum_of_number)

    
    
    
