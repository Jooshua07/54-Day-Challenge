prices = [12,25,8,15,20]
quantities2 = [2,1,3,2,1]
quantities = [1,1,1,1,1]

print("---test 1------------------")
total = 0
for i in range(len(prices)):
    product = prices[i] * quantities[i]
    print(f"item price : {prices[i]}| quantity : {quantities[i]} | amt: {product}")
    total += product 
print(total)

discount_percent = 10/100
if total > 100:
    discount_amt = total * discount_percent
    total = total - discount_amt
    print(total)

print("-----test2------------------")
total2 = 0
for i in range(len(prices)):
    product2 = prices[i] * quantities2[i]
    print(f"item price : {prices[i]}| quantity : {quantities2[i]} | amt: {product2}")
    total2 += product2 
print(total2)

if total2 > 100:
    discount_amt = total2 * discount_percent
    total2 = total2 - discount_amt
    print(total2)




