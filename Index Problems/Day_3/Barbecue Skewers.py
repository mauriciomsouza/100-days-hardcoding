import random

def Barbecue(grill):
    non_veg_count = 0
    veg_count = 0
    for skewer in grill:
        if 'x' in skewer:
            non_veg_count += 1
        else:
            veg_count += 1
    return [veg_count, non_veg_count]

#Testing with a random skewer's grill generator
"""n = random.randint(1,10)
grill = [''.join(random.choices(['-','o','x','-'], k=12)) for i in range(n)]

print(grill)
print(Barbecue(grill))"""