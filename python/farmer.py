# farmer problem

# Area details
total_land = 80
land_per_crop = total_land // 5

# overall_sales calculation
overall_sales = 0
#Tomatoes
tomatoes_cost = ((30/100*land_per_crop)*10+(70/100*land_per_crop)*12)*1000*7    #1 tonne = 1000kg ; Rs7/kg
overall_sales += tomatoes_cost
#Potatoes
potato_cost = (land_per_crop*10*1000*20)  # 10 tonnes/acre, Rs 20/kg
overall_sales += potato_cost
#Cabbage
cabbage_cost = (land_per_crop*14*1000*24)   # 14 tonnes/acre, Rs 24/kg
overall_sales += cabbage_cost
#Sunflower
sunflower_cost = (land_per_crop*0.7*1000*200)  # 0.7 tonnes/acre, Rs 200/kg
overall_sales += sunflower_cost
#Sugarcane
sugarcane_cost = (land_per_crop*45*4000)      # 45 tonnes/acre, Rs 4000/tonne
overall_sales += sugarcane_cost
print("The overall sales achieved by Mahesh from the 80 acres of land is: Rs {:.1f}".format(overall_sales))

# Months taken for conversion
tt_vegetables = 6 #6 months
tt_sunflower = 4  # 10 months
tt_sugarcane = 4  # 14 months

# Total sales from chemical-free farming at month 11
chemical_free_sales = tomatoes_cost + potato_cost + cabbage_cost + sunflower_cost

print("Sales realisation from chemical-free farming at the end of 11 months is: Rs {:.1f}".format(chemical_free_sales))