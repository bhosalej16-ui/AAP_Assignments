class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand    :", self.brand)
        print("Model    :", self.model)
        print("Price    :", self.price)
        print("Category :", self.category())
        print("-" * 30)


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        print("\nAvailable Mobiles")
        print("=" * 30)
        for mobile in self.mobiles:
            mobile.display()


# Main Program
store = Store()

m1 = Mobile("Samsung", "Galaxy S25", 75000)
m2 = Mobile("OnePlus", "Nord CE 5", 28000)
m3 = Mobile("Redmi", "Note 14", 15000)

store.add_mobile(m1)
store.add_mobile(m2)
store.add_mobile(m3)

store.display_mobiles()