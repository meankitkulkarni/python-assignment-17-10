inventory ={"pen":10, "Notebook":5}
same_inventory = inventory
copied_inventory=inventory.copy()
same_inventory["pen"]+=2
print("inventory:",inventory)
print("same_inventory:",same_inventory)
print("copied_inventory:",copied_inventory)