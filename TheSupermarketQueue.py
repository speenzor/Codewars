def queue_time(customers, n):
    if len(customers) == 0:
        return (0)
    elif len(customers) == 1:
        return (customers[0])
    elif n == 1:
        x = 0
        for i in range(len(customers)):
            x = x + customers[i]
        return (x)
    elif n >= len(customers):
        return max(customers)
    else:
        queues = {}
        for i in range(1,n+1):
            #Create a dictionary key for each till
            queues['till'+str(i)]=0
        for c in customers:
            min_key = min(queues, key=queues.get) #Find the till with the shortest line
            queues[min_key] += c #Next customer goes to the shortest line then updates the dictionary
        return max(queues.values())
