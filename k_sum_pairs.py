

def get_pairs(list_items, target_value):
    stop_index = len(list_items) - 1 
    unique_pairs = set()
    
    for cur_index in range(stop_index):
        num_1 = list_items[cur_index]
        num_2 = target_value - num_1 
        remaining_items = list_items[cur_index + 1:]
        if num_2 in remaining_items:
            pairs = (num_1, num_2)
            sorted_tuple = tuple(sorted([pairs]))
            unique_pairs.add(sorted_tuple) 
    return unique_pairs   







list_items = list(map(int, input("Enter the list items: ").split(',')))
target_value = int(input("Enter the target sum value: "))

result = get_pairs(list_items, target_value)
# print(result)

result = sorted(result)

for each_pairs in result:
    print(each_pairs)
    
    
