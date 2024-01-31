#question no 1
light='pink'
if(light=='red'):
    print('stop')
elif(light=='green') :
    print('go')
elif(light=='yellow'):
    print('look the siginal')
else:
    print('light is brokren')
 #question no 2   
age=20
if(age<=19):
   print('you are ealigible for vote')#(indentation(....))
else:
   print('you are not ealigible for vote') 
#question no 3   
marks=40
if(marks >=90):
    grade='a'
elif(marks >=80 and marks <90):
    grade='b'
elif(marks >=70 and marks <80):
    grade='c' 
else:
    grade='d'
print('grade of  the student ->',grade) 
#question no 4 nesting
age=34
if(age>=18):
   if(age>=80):
        print('cannot drive')
   else:    
      print('you can drive')
else:
    print('you can not drive')
#question no 4      
num=int(input('enter the  number:'))
rem=num % 2
if(rem==0):
    print('even')
else:
    print('odd')
#question no 5    
a=int(input('enter the first number '))
b=int(input('enter the second number '))
c=int(input('enter the third number '))
if(a>=b and b>=c):
    print("enter the  first number si the greatest",a)
elif(b>=c ):
    print('the number second is largest',b)
else:
    print('the third number  is largest ',c)
     
     

              


