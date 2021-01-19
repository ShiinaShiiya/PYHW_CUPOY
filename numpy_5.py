import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
mean_eng = np.nanmean(english_score)
mean_math = np.nanmean(math_score)
mean_chin = np.nanmean(chinese_score)

max_eng = np.nanmax(english_score)
max_math = np.nanmax(math_score)
max_chin = np.nanmax(chinese_score)

min_eng = np.nanmin(english_score)
min_math = np.nanmin(math_score)
min_chin = np.nanmin(chinese_score)

std_eng = np.nanstd(english_score)
std_math = np.nanstd(math_score)
std_chin = np.nanstd(chinese_score)
"""
print(f'英文:\n    平均:{mean_eng}分\n    最大值:{max_eng}\n    最小值:{min_eng}\n    標準差:{std_eng}')
print(f'數學:\n    平均:{mean_math}分\n    最大值:{max_math}\n    最小值:{min_math}\n    標準差:{std_math}')
print(f'國文:\n    平均:{mean_chin}分\n    最大值:{max_chin}\n    最小值:{min_chin}\n    標準差:{std_chin}')
print(f'其中數學缺一筆資料可忽略?\n    可以')
"""
#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4] = 55

mean_math = np.nanmean(math_score)
max_math = np.nanmax(math_score)
min_math = np.nanmin(math_score)
std_math = np.nanstd(math_score)
"""
print(f'數學:\n    平均:{mean_math}分\n    最大值:{max_math}\n    最小值:{min_math}\n    標準差:{std_math}')
"""
#3. 用補考後資料找出與國文成績相關係數最高的學科?
cor_chin_math = np.corrcoef(chinese_score,math_score)
cor_chin_eng = np.corrcoef(chinese_score,english_score)
"""
cor_eng = np.corrcoef(english_score)
"""
print(cor_chin_math)
print(cor_chin_eng)
print("english最高")