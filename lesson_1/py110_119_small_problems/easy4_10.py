# P:
# input: two arguments - inventory item ID & transaction list
# output: returns True if an ID# is present and the "movement" is "in",
#         otherwise False
# explicit:
# implicit:

# E: see below

# D:

# A:
# def transactions_for(item_id, transact_lst):
#    return [transaction for transaction in transact_lst 
#            if item_id == transaction["id"]]

# def is_inventory_positive(transact_lst):
#     if transact_lst == []:
#         return False

#     inventory_tracker = 0
    
#     for transact in transact_lst:
#         if transact["movement"] == "in":
#             inventory_tracker += transact["quantity"]
#         if transact["movement"] == "out":
#             inventory_tracker -= transact["quantity"]

#     return inventory_tracker > 0


# def is_item_available(item_id, transaction_lst):
#     selected_transacts = transactions_for(item_id, transaction_lst)
#     return is_inventory_positive(selected_transacts)

# C:
def transactions_for(item_id, transact_lst):
   return [transaction for transaction in transact_lst 
           if item_id == transaction["id"]]

def is_inventory_positive(transact_lst):
    if transact_lst == []:
        return False

    inventory_tracker = 0
    
    for transact in transact_lst:
        if transact["movement"] == "in":
            inventory_tracker += transact["quantity"]
        else:
            inventory_tracker -= transact["quantity"]

    return inventory_tracker > 0


def is_item_available(item_id, transaction_lst):
    selected_transacts = transactions_for(item_id, transaction_lst)
    return is_inventory_positive(selected_transacts)


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True 