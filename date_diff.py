#Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
import datetime

a=str(input()).split(" ")
a_1=[]
for i in a:
    a_1.append(int(i))
b=int(input())

d1=datetime.date(a_1[0], a_1[1], a_1[2])
total=d1+datetime.timedelta(days=b)
l=[]
for j in str(total).split('-'):
    if j[0]=='0':
        l.append(j[1:])
    else:
        l.append(j)
print(" ".join(l))




















































