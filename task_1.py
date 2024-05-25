import pulp


model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)


x_lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
x_fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

model += x_lemonade + x_fruit_juice, "Total_Production"

model += 2 * x_lemonade + 1 * x_fruit_juice <= 100, "Water"
model += 1 * x_lemonade <= 50, "Sugar"
model += 1 * x_lemonade <= 30, "Lemon_Juice"
model += 2 * x_fruit_juice <= 40, "Fruit_Puree"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal amount of Lemonade: {pulp.value(x_lemonade)}")
print(f"Optimal amount of Fruit Juice: {pulp.value(x_fruit_juice)}")
print(f"Maximum Total Production: {pulp.value(model.objective)}")
