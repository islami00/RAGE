"""data_i=input('Enter student scores: ')
data_o=data_i.split(',')

data=[]
for score in data_o:
    score=int(score)
    data.append(score)

sum_=sum(data)
no_of_students=len(data)
average=sum_/no_of_students

print(f'Average score = {average} \n Sum of scores = {sum_} \n Number of students = {no_of_students}')

"""

import matplotlib
from matplotlib import pyplot as plt

views=[25,60,40,12,200,100,200,-220,123,-90,2,7,5,3,50,500,129,453]
day=range(len(views))

plt.bar(day,views)


plt.show()