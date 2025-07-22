miles_to_metter = 1609.344
litters_to_gallon = 3.785411784


def litters_100km_to_miles_gallon(litters):
    gallon = litters / litters_to_gallon
    miles = (100 * 1000) / miles_to_metter

    return miles/gallon

def miles_gallon_to_litters_100km(miles):
    km = miles * miles_to_metter
    litters = 1 * litters_to_gallon
    return litters / km

print(litters_100km_to_miles_gallon(3.9))
print(miles_gallon_to_litters_100km(60.3))