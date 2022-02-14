a = input("Ievadiet skolēnu vidējas atzīmes(noapaļotas, ar vienu atstarpi): ")
a = "Extract 10 , 9 , 8 from this string"
s = [int(s) for s in str.split(a) if s.isdigit()]
print(s)
a = "Extract 7 , 6 , 5 , 4 from this string"
b = [int(b) for b in str.split(a) if b.isdigit()]
print(b)
a = "Extract 3 , 2 , 1 from this string"
c = [int(c) for c in str.split(a) if c.isdigit()]
print(c)
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Teicamnieku skaits: ", get_number_of_elements(s))
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Mācās vidēji skaits: ", get_number_of_elements(b))
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Nesekmīgu skaits: ", get_number_of_elements(c))
