# P:
# input: two arguments - inventory item ID & transaction list
# output: returns list of transactions containing only transactions for the
#         specified item
# explicit:
# implicit:

# E: see below

# D:

# A:
# def transactions_for(item_id, transaction_lst):
#    return [transaction for transaction in transaction_lst 
#            if item_id == transaction["id"]]

# C:
def transactions_for(item_id, transaction_lst):
   return [transaction for transaction in transaction_lst 
           if item_id == transaction["id"]]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True          