import numpy as np

a = np.arange(21)       #生成一個等差數列，首數為0，尾數為20，公差為1的數列。

print(a)

all_even = ""
for num in a:
    if num%2 == 0:
        if num == 0:
            pass
        else:
            all_even += str(num) + "  "
        
print(all_num)         #呈上題，將以上數列取出偶數。

all_Triple = ""
for num in a:
    if num%3 == 0:
        if num == 0:
            pass
        else:
            all_Triple += str(num) + "  "
            
print(all_Triple)