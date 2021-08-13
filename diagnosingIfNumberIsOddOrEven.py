# author : Sarvin Nami
def number (num) :
    if num % 2 == 0 :
        return True
    else :
        return False
num = int(input('please enter your number here : '))
while num != 00 :
    if number(num) :
        print('your entered number is even.')
    else :
        print('your entered number is odd.')
    num = int(input('please enter your number here and if you wanna stop enter 00 : '))
    