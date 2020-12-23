n = 100
mean = 500
std = 80
interval = 0.95
z = 1.96
print(round(mean - (std / (n**0.5))* z, 2))
print(round(mean + (std / (n**0.5))* z, 2))
