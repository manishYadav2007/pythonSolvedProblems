
def  get_trades(list_of_customers):
    total_trades = 5 / 100 * len(list_of_customers)
    count_each_customer = {}
    for i in list_of_customers:
        if i in count_each_customer:
            count_each_customer[i] += 1
        else:
            count_each_customer[i] = 1 
    
    active_customers = []
    
    for customer, count in count_each_customer.items():
        if count >= total_trades:
            active_customers.append(customer)
    
    active_customers.sort()
    
    return active_customers




list_of_customers = input("Enter the customers: ").split()


result = get_trades(list_of_customers)
print(result)