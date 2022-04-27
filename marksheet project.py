
'''def ask():
    a=input("enter the student name:")
    b=int(input("\nenter your Roll Number:"))
    c=int(input("\nenter your DOB(DD/MM/YY):"))
    d=input("\nenter medium:")
    e=input("\nenter college name:")
    f=input("\nenter place:")


ask()'''



def marks():
    while True:
        m= int(input("\nEnter the obtained in mathamatics(3):"))
        
        if m<=80:
            print(m)
            break
        else:
            print("\nplease enter the correct marks")

    while True:
        m1=int(input("Enter the marks obtained in Mathmatics3[PRACTICAL]:"))

        if m1<=20:
            print(m1)
            break
        else:
            print("\nplese enter the correct marks:")

    while True:
        n=int(input("\nEnter the marks obtained in NAS:"))

        if n<=80:
            print(n)
            break
        else:
            print("\nenter enter the corect marks")

    while True:
        n1=int(input("\nEnter the marks obatined in NAS[PRACTICAL]:"))

        if n1<=20:
            print(n1)
            break
        else:
            print("\nPlease enter the correct marks")

    while True:

        em=int(input("\nEnter the marks obtained in EMI:"))

        if em<=80:
            print(em)
            break
        else:
            print("\nPlease enter the corect marks")
        
    while True:
        em1=int(input("\nenter the marks obtained in EMI[PRACTICAL]:"))

        if em1<=20:
            print(em1)
            break
        else:
            print("\nenter the correct marks")

    while True:
        e=int(input("\nEnter the marks obtained in EDC:"))

        if e<=80:
            print(e)
            break
        else:
            print("\please enter the correct marks")

    while True:
        e1=int(input("\nEnter the marks obtained in EDC[PRACTICAL]:"))

        if e1<=20:
            print(e1)
            break
        else:
            print("\n please enter the correct marks")

    while True:
        o=int(input("\nEnter the marks obtained in OOPD'S:"))

        if o<=80:
            print(o)
            break
        else:
            print("\nplease enter the correct marks")
        
    while True:
        o1=int(input("\nEnter the marks obtained in OOPDS'S[PRACTICAL]:"))

        if o1<=20:
            print(o1)
            break
        else:
            print("\nplease enter the correct marks")


marks()

def call():
    r1 = m+m1
    r2 = n+n1
    r3 = e+e1
    r4 = em+em1
    r5 = op+op1
    total=r1+r2+r3+r4+r5
    per=float(total/5)
#for result
    if(per<35):
        z='F'
    elif (per>35):
        z="P"
    else:
        z='-'
#for grading
    if(per<=85):
        grade='A'
    elif(per>75 and per<85):
        grade='B'
    elif(per>=55 and per<75):
        grade='C'
    elif(per>=40 and per<55):
        grade='D'
    else:
        grade='E'

#for marks, pass or not
    if(r1<40):
        print('#')
    elif(r1>40):
        print(' ')
    else:
        print(' ')

    if(r2<40):
        print('#')
    elif(r2>40):
         print(' ')
    else:
        print(' ')

    if(r3<40):
        print('#')
    elif(r3<40):
        print(' ')
    else:
        print(' ')

    if(r4<40):
        print('#')
    elif(r4>40):
        print(' ')
    else:
        print(' ')

    if(r5<40):
        print('#')
    elif(r5>40):
        print(' ')
    else:
        print(' ')
#####################################
    if(p=='#'):
        print('F')
    elif(q=='#'):
        print('F')
    elif(s=='#'):
        print('F')
    elif(t=='F'):
        print('F')
    elif(v=='#'):
        print('F')
    else:
        print('P')

call()










    































