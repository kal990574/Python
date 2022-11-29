import math
point=[]
for i in range(5):
    point.append(int(input("성적을 입력하시오:")))
sum=0 #s=합
for i in point:
    sum=sum+i
average=round(sum/5)
print("점수:", point)
print("합:", sum, "평균:", average)