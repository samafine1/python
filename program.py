n = input("How many data points do you have?")
nint = int(n)
Yes = "Yes"
yes = "yes"
data = {       }
        
while (nint > 0):
    n1 = input("What is the x value?")
    m1 = input("What is the y value?")
    n2 = int(n1)
    m2 = int(m1)
    data[n2] = m2
    nint = nint-1

check = input("Is this data correct? Yes, or No?")
if check == Yes or yes:
    print("Good, Here is your data sorted.")
    for key in sorted(data.iterkeys()):
        print "%s: %s" % (key, data[key])
else:
    input("Which datapoint is wrong?")
    print("Cool!")
