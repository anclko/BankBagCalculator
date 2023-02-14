print("Welcome to the Money Bag Transport Calculator (M.B.T.C")
print("-"*55)

# setting up volume of each bag
smallBagVolume = 20
mediumBagVolume = 50
largeBagVolume = 80

# setting up amounts that each bag can contain
amountSmallBag = 10000
amountMediumBag = 30000
amountLargeBag = 60000

# Calculate the input from user
truckVolume = int(input("What is the volume of the truck? (>= 100L): "))
while truckVolume < 100:
    truckVolume = int(input("What is the volume of the truck? (>= 100L): "))

largeBagNumber = int(truckVolume/largeBagVolume)
leftoverVolume = truckVolume - (largeBagVolume*largeBagNumber)

mediumBagNumber = int(leftoverVolume/mediumBagVolume)
leftoverVolume = leftoverVolume - (mediumBagVolume*mediumBagNumber)

smallBagNumber = int(leftoverVolume/smallBagVolume)
leftoverVolume = leftoverVolume - (smallBagVolume*smallBagNumber)

# Outcome of input
print("")
print("Packing plan")
print("-"*12)
print(f"{largeBagNumber} big bags")
print(f"{mediumBagNumber} medium bags")
print(f"{smallBagNumber} small bags")
print("")

totalValue = (amountSmallBag * smallBagNumber) + (amountMediumBag * mediumBagNumber) + (amountLargeBag * largeBagNumber)

print(f"Space left : {leftoverVolume}L")
print(f"Total value: {totalValue}kr")
