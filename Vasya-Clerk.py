#Challenge is to see if the cashier will have change for all the people in line
#The "people" argument is a list of the bills that the patrons have- either a $25
#$50, or $100 bill. Can the cashier sell a ticker to each person and give the change
#if he initially has no money and sells the tickets strictly in the order people
#follow in line?
def tickets(people):
    if people[0] != 25:
        return ('NO')
    change = [people[0]]
    for i in range(1,len(people)):
        if people[i] == 25:
            change.append(people[i])
        elif people[i] == 50:
            if 25 in change:
                change.remove(25)
                change.append(50)
            else:
                return('NO')
        elif people[i] == 100:
            if change.count(25) >=3:
                change.remove(25)
                change.remove(25)
                change.remove(25)
                change.append(100)
            elif change.count(50) >= 1 and change.count(25) >=1:
                change.remove(50)
                change.remove(25)
                change.append(100)
            else:
                return('NO')
    return('YES')
