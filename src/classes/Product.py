id = 0

class Product:
    def __init__(self, name, description, category, brand):
        global id
        id += 1
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand


fregona = Product(
    name="Fregona",
     description="Fregona con microfibras",
      category="limpieza", brand="Mileda"
      )

print(fregona.name)