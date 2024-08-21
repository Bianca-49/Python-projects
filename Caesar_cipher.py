import string
alphabet_upper_list = list(string.ascii_uppercase)
user=True
while user:
    op=''
    while op.upper()!='DECODE' and op.upper()!='ENCODE':
        op = input(f'Do you want to decode or encode? (type decode or encode)\n')
        if op.upper()!='DECODE' and op.upper()!='ENCODE':
            print("I don't understand. Please type decode or encode!\n")
        else:
            break
    key= 0
    while key not in range(1,26):
        key=input(f'Type the key! (A number between 1 and 25)\n')
        if int(key) not in range(1,26):
            print('Please type a valid number!\n')
        else:
            break
    secv='123'
    while secv.isalpha()==False:
        secv=input(f'Please insert the phrase you want to {op}. The phrase must contain only letters.\n')
        if secv.isalpha()==False:
            print('Please type only letters\n')
        else:
            secv=secv.upper()
            break
    res=''
    key=int(key)
    if op.upper()=='ENCODE':
        for i in secv:
            if alphabet_upper_list.index(i)+key>25:
                res=res+alphabet_upper_list[(alphabet_upper_list.index(i)+key)%25-1]
            else:
                res=res+alphabet_upper_list[(alphabet_upper_list.index(i)+key)]
    if op.upper()=='DECODE':
        for i in secv:
            if alphabet_upper_list.index(i)-key<0:
                res=res+alphabet_upper_list[25+alphabet_upper_list.index(i)-key+1]
            else:
                res=res+alphabet_upper_list[alphabet_upper_list.index(i)-key]    
    print(f'Your {op.lower()}d phrase is {res}.')  

    val=''
    while val.upper()!='Y' and val.upper()!='N':
        val=input('Do you want to insert another phrase? (Y/N)')
        if val.upper()!='Y' and val.upper()!='N':
            print('Please type Y or N!')
        elif val.upper()=='N':
            user=False
            break
        else:
            break
