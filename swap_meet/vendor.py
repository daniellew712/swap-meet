class Vendor:
    
    def __init__(self, inventory = None):

        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):

        self.inventory.append(item)
        return item
    
    def remove(self, item):

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
        
    def get_by_id(self, id):

        for item in self.inventory:
            if item.id == id:
                return item
            
        return None
        
    def swap_items(self, other_vender, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vender.inventory:
            self.remove(my_item)
            other_vender.add(my_item)
            other_vender.remove(their_item)
            self.add(their_item)
            return True

        else: 
            return False
    
    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_item, their_item)

        return True
        
    def get_by_category(self, category):
        same_category = []
        
        for item in self.inventory:
            if item.get_category() == category:
                same_category.append(item)
        
        return same_category
    
    def get_best_by_category(self, category):

        same_category = self.get_by_category(category)
        if not same_category:
            return None
        
        best_condition = same_category[0].condition
        best_condition_item = same_category[0]
        
        for item in same_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_condition_item = item

        return best_condition_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if not (my_item and their_item):
            return False

        self.swap_items(other_vendor, my_item, their_item)

        return True

