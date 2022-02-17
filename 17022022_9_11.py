a = int(input("Ievadiet 1. skolēna vidējo atzīmi(no 10 līdz 1): "))
b = int(input("Ievadiet 2. skolēna vidējo atzīmi(no 10 līdz 1): "))
c = int(input("Ievadiet 3. skolēna vidējo atzīmi(no 10 līdz 1): "))
def atzimes():
    if a > 7:
        print("1. skolēns ir teicamncieks")
    if 7 >= a >= 4:
        print("1. skolēns mācās vidēji")
    if a < 4:
        print("1. skolēns ir nesekmīgs")
    
    if b > 7:
        print("2. skolēns ir teicamncieks")
    if 7 >= b >= 4:
        print("2. skolēns mācās vidēji")
    if b < 4:
        print("2. skolēns ir nesekmīgs")
        
    if c > 7:
        print("3. skolēns ir teicamncieks")
    if 7 >= c >= 4:
        print("3. skolēns mācās vidēji")
    if c < 4:
        print("3. skolēns ir nesekmīgs")
        
atzimes()
