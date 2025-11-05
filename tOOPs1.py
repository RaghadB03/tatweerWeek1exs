class Item():
    def __init__(self,itemId, name,  price, category, vendor, exD,quantity=0,):
        self.itemId = itemId
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.vendor = vendor
        self.exDate = exD
    
    def purchase(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            total_cost = amount * self.price
            return total_cost
        else:
            return "Insufficient stock"
    
    def restock(self, amount):
        self.quantity += amount
        return self.quantity
    
    def is_expired(self, current_date):
        return current_date > self.exDate
    
    
    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        return self.price
    
    def __str__(self):
        return f"Item ID: {self.itemId}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Category: {self.category}, Vendor: {self.vendor}, Expiration Date: {self.exDate}"
    

class clothItem(Item):
    def __init__(self, itemId, name, quantity, price, category, vendor, exD, size, material):
        super().__init__(itemId, name, quantity, price, category, vendor, exD)
        self.size = size
        self.material = material
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Size: {self.size}, Material: {self.material}"