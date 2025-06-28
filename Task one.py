# 1. Define variables for the prices of three items
Tomato=20
onion=50
Botato=60

#2.Define a variable for the total budget
Total_Budget=200

#3. Calculate the total cost of the items
Total_Cost=Tomato+onion+Botato

#4. Compare the total cost with the budget
if Total_Cost<=Total_Budget:
    print("you are able to buy the mentioned items")
else:
    print("you are not able to buy the mentioned items")

 # 5. Calculate the difference
difference = Total_Cost - Total_Budget

if difference >= 0:
 print("you will have",difference,"money left after shopping")
else:
 print("you need ",abs(difference),"more to afford every thing.")