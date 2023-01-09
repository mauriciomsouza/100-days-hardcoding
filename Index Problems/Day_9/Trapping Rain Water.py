import matplotlib.pyplot as plt
import numpy as np 
import random


plt.style.use('_mpl-gallery')

def TrappingRain(height):
    if not height:
        return 0
    water_amount = [0 for k in range(len(height))]
    left, right = 0, len(height) - 1

    while left < right:
        if height[left] < height[right]:
            left_height = height[left]
            left += 1
            while left < right and height[left] < left_height:
                water_amount[left] = left_height - height[left]
                left += 1
        else:
            right_height = height[right]
            right -= 1
            while left < right and height[right] < right_height:
                water_amount[right] = right_height - height[right]
                right -= 1
    return np.array(water_amount)

    
def HeightGen():
    n = random.randint(6, 18)
    return list(np.random.randint(0,high=5, size=n))

height = HeightGen()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
#height = [4,3,4,4,4,4]
y = np.array(height)
x = 0.5+np.arange(len(height))

print(y)
print(TrappingRain(height))


#print(y)
#print(TrappingRain(height))
fig, ax = plt.subplots()

ax.bar(x, y, width = 1 ,color = 'black', edgecolor = 'white')
ax.bar(x, TrappingRain(height), width = 1 ,color = 'blue', edgecolor = 'white', bottom=y)
ax.set(xlim = (0, len(height)) , xticks = np.arange(1,len(height)) , ylim = (0, max(height) + 1), yticks = np.arange(1, max(height)) )
plt.show()