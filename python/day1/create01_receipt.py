prices = [12,25,8,15,20]
quantities = [2,1,3,2,1]

x = 0
total = 0
for i in range(len(prices)):
    product = prices[x] * quantities[x]
    print(f"item price : {prices[x]}| quantity : {quantities[x]}")
    x += 1
    total += product 

print(total)
