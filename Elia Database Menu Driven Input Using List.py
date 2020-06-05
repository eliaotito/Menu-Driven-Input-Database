#list database Project
#A Small Project for Adding & Display & Remove Data


name = []
address = []
phone =[]
education=[]
religion=[]

while True:
    print('\n 1.Adding Data\n 2.Display Data\n 3.Deleting Data\n 4. Exit the Program')
    choice= int(input('Please enter your choice as above menu:  '))
    if choice==1:
            nam= input('Please enter your name:  ')
            name.append(nam)
            addr = input('Please enter your Address:   ')
            address.append(addr)
            phon= input('Please enter your phone number:   ')
            phone.append(phon)
            edu = input('Please enter your Education Level:  ')
            education.append(edu)
            rel = input('Please enter your religion :    ')
            religion.append(rel)

        
    elif choice ==2:
        print('---------Please enter your Name to be displayed-----------------')
        nam = input('Please enter your name:   ')
        if nam in name:
            print('--------------Your Name will be displayed shortly---------------------')
            check_name = name.index(nam)
            print('Name is:  ',  name[check_name])
            print('Address is: ', address[check_name])
            print('Your Education level is: ' ,education[check_name])
            print('Your Religion is:', religion[check_name])
            print('Your Phone Number is: ', phone[check_name])
            print()


        else:
            print('-----------Sorry your name was not available-----------------')

    elif choice ==3:
       print('---------------You want to Delete your Data--------------------')
       nam = input('Please enter your name:   ')
       if nam in  name:
           check_name = name.index(nam)
           name.pop(check_name)
           address.pop(check_name)
           education.pop(check_name)
           religion.pop(check_name)
       else:
           print('------------------Sorry your Data WAS Not found so it could not be deleted-------')

    elif choice==4:
          print('--------------BYE BYE -------------------')
          break

       

    
