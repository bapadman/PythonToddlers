#!/usr/bin/python
#assertion in pu=ython same
def applyDiscount(prodPrice,discount):
	price = prodPrice * (1-(discount/100))
	assert 0 < price < prodPrice # this assert makes sure that the discounted price cannot be in negative 
	return price
#finalPrice = applyDiscount(100,50)
finalPrice = applyDiscount(100,150)
print(finalPrice)