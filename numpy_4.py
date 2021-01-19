import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

array_ans = np.greater(english_score, math_score)                    #1.有多少學生英文成績比數學成績高?  
total=0
for a in array_ans:
    if a == True:
        total+=1
        
print(total,"人")                                     


array_ans1 = np.greater(chinese_score, math_score)                      #2.是否全班同學最高分都是國文?
array_ans2 = np.greater(chinese_score, english_score)

ans = np.logical_and(array_ans1, array_ans2)
total=0
for a in ans:
    if a == True:
        total+=1

print(total,"人")