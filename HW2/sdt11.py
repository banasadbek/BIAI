sentence = input('enter the sentence: ')
character = input('enter the character: ')
count = -1
flag = True

for index in sentence:
    count+=1
    if flag: 
        if index == character:
            first_postion = count
            flag = False
            
print(first_postion)