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
        


