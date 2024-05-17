print('hello world')
if 5>2:
    print("Five is greater than two")

x = 5
y = 'hello world'
print('sayı %d' % (x))
#this is a comment
#print('hello world')
"""
uzunca yazı yazabiliyorum
satır 
satır 
hem
de

"""
int_age = 21
str_name = 'Salih Cihat Yalçın'
dbl_rate = 2.11
bool_flag = True
print('Age %d' % (int_age))
print('Name %s %d' % (str_name, int_age))
print('Rate %.2f' % (dbl_rate))
print('Flag %s' % (bool_flag))

int_age = int(input('Input your age: ')) #int koymasaydık string olarak kalıcaktı. #int() integera dönüştürmek için #float(), str()
print('Your age is ', int_age) #print('your age is %d' % (int_age))

int_grade = int(input('Input your grade: '))
print('Your grade is %d'% (int_grade))
#0 60 arası fail. 60 100 arası pass. 100den büyükse invalid.

if int_grade>=0 and int_grade<60:  #süslü parantez yok :. print boşluk bırakılarak yazılmalı
    print('Fail')
    print('Work hard!')
elif int_grade>=60 and int_grade<101:
    print('Pass')
    print('Congrats')
else:
    print('Invalid input')