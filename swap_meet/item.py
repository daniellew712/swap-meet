import uuid

class Item:

    def __init__(self, id = None, condition = 0.0, age = 0.0):

        if not id:
            id = uuid.uuid4().int
            
        self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        descriptions = {
            0: "Poor",
            1: "Heavily used",
            2: "Used",
            3: "Good",
            4: "Very good",
            5: "Mint condition"
        }
        return descriptions.get(self.condition, "Unknown condition")