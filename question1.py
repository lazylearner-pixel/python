# person A and B are purchasing identical items at same price. person A sells the item at a profit of 20% and person B sells the item at a loss of 20%.
# if the cost price of the item is 100, find the selling price of both persons


sell_price_A = int(input("Enter the selling price by person A: "))
profit_A = int(input("Enter the profit percentage of person A: "))
profit_B = int(input("Enter the loss percentage of person B: "))

(x) = sell_price_A / (1 + profit_A / 100)

y = x + (profit_B*x)/100
print("Cost price of person A is:", x)
cost_price = x

print("selling price of person B is:", y)
