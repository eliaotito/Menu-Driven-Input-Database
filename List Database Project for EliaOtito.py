#List Database Projects
#Menu Driven Inputs
#1. Add data
#2. Display Data
#3. Delete Data


name = []
address=[]
phone =[]
Education=[]
Religion=[]

while True:
    print('\n1.Add data \n2.Display Data \n3.Delete Data \n4.Exit')
    choice = int(input('Please enter your choice as per above Menu:  '  ))
    if choice ==1:
        print('---------- WELCOME, PLEASE ENTER YOUR DATA----------')
        nam= input('Please enter your name!   ')
        name.append(nam)
        addr = input('Please enter your address!  ')
        address.append(addr)
        phon= input('Please enter your Phone Number!   ')
        phone.append(phon)
        edu= input('Please enter your Education Level!   ')
        Education.append(edu)
        rel = input('Please enter your religion!    ')
        Religion.append(rel)
    elif choice ==2:
        
       print('--------------WELCOME,Below is your displayed Data-------------')
       nam = input('Please enter your name!:   ')
       if nam in name:
           print('---------LET CHECK YOUR DATA---------------------------')
           check_word = name.index(nam)
           print('Name is :', name[check_word])
           print('Address is:', address[check_word])
           print('Phone:', phone[check_word])
           print('Education:', Education[check_word])
           print('Religion:', Religion[check_word])
       else:
           print('------------SORRY, NO DATA is Available on  your input--------')

    elif choice==3:
        print('------- DELETE DATA----------------------')
        nam = input('Please enter your name to be deleted!::')
        if nam in name:
            print('------------WELCOME, YOU CAN DELETE DATA----------------------')
            check_word = name.index(nam)
            name.pop(check_word)
            address.pop(check_word)
            phone.pop(check_word)
            Education.pop(check_word)
            Religion.pop(check_word)
        else:
           print('-------Sorry,We cannot delete data, We didnt find the data')

    elif choice ==4:
          print('---------------BYE BYE-----------------------')
          break
            
           
