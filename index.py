t_user=input('Give me your text')
count=0
for c in t_user: 
    print(c)
    match c:
        case 'a':
            count+=1
        case 'e':
            count+=1
        case 'i':
            count+=1
        case 'o':
            count+=1
        case 'u':
            count+=1
print(f'The length vowels is:{count}')
