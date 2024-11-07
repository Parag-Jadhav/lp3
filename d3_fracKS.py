class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
    
    #cal value-weight ratio (per kilo profit)
    def value_to_weight_ratio(self):
        return self.value/self.weight
    
def fractional_knapsack(items, capacity):

    #sorting the items list in descending order
    items.sort(key=lambda x: x.value_to_weight_ratio(), reverse = True)

    total_value = 0.0 #total capacity of knapsack - m float since fractional

    for item in items:
        
        #if the item value is less than whole capacity take whole value
        if capacity>item.weight:
            capacity = capacity - item.weight
            total_value = total_value + item.value
        else: #if weight is greater than capacity we take fractions of the items weights
            fraction = capacity/item.weight
            total_value = total_value + item.value*fraction
            break #knapsack is full 
    return total_value

#usecase
items = [Item(60,10),Item(100,20),Item(120,30)]      
capacity = 50
max_profit = fractional_knapsack(items, capacity)
print("Total max profit= ", max_profit)     

#Time Complexity:𝑂(𝑛log⁡𝑛) sorting
#Space Complexity:O(n) input
