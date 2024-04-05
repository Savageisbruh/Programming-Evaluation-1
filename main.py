# ----------- QUESTION 1 ----------- 
print("""
___________      .__         
\_   _____/ ____ |__| ______ 
 |    __)_ /    \|  |/  ___/ 
 |        \   |  \  |\___ \  
/_______  /___|  /__/____  > 
        \/     \/        \/ 

""")


# -----------  QUESTION 2 ----------- 

# Ask the user for their sides of the triangle 

Sidelenthone = int(input("Enter the side lenth of the triangle: "))
Sidelenthtwo = int(input("Enter the side lenth of the triangle: "))
sidelenththree = int(input("Enter the side lenth of the triangle: "))

# Caculate S 
S = (sidelenththree + Sidelenthtwo + Sidelenthone)/2

# Caculate the area of the triangle
Area = (S*(S-sidelenththree)*(S-Sidelenthtwo)*(S-Sidelenthone))
print(round (Area,2))



# -----------  QUESTION 3 -----------

import random 

totalPercentage = 100
totalBudget = 0

# Generating random Percents 
Food = random.randint(20, 30)
Clothing = random.randint(15, 20)
Rent = random.randint(35, 45)
Entertainment = totalPercentage-(Food+Clothing+Rent)
totalBudget = int(input("Enter your budget:"))


# Calculating Total Budget 
Total = Food + Clothing + Entertainment + Rent
print("total budget is", totalBudget)

# Calculating Percentages
Foodpercent = round ((totalBudget) * (Food/Total),2)
Clothingpercent = round ((totalBudget) * (Clothing/Total),2)
Rentpercent = round ((totalBudget) * (Rent/Total),2)
Entertainmentpernect = round ((totalBudget) * (Entertainment/Total),2)


# Printing Percents
print("\nrent \t\t\t", Rent, "%\t$", Rentpercent, "\nClothing \t\t", Clothing, "%\t$", Clothingpercent, "\nFood \t\t\t", Food, "%\t$", Foodpercent, "\nEntertainment \t", Entertainment, "%\t$", Entertainmentpernect)
