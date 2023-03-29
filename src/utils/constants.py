'''
docstring -> Informacion auxiliar para el IDE
'''

## Tipos de datos
 
 
#Strings :

MERCADONA = "MERCADONA"
CONSUM = "CONSUM"
CARREFOUR = "CARREFOUR"
LIDL = "LIDL"


# Numbers :

DEFAULT_QUANTITY_TO_ALERT = 1


# Booleans :

IS_LOGGED_IN = True # False


# Lists :

MOCKUP_PRODUCTS_LIST = ["CEREALES", "FREGONA","PAPEL HIGIENICO"]

# TUPLES :

MOCKUP_COUPONS_LIST = ("COMIDA A MITAD DE PRECIO", "PRODUCTOS SIN IVA")

# SETS :

SUPERMARKETS = { MERCADONA, CONSUM, CARREFOUR, LIDL }


# OBJETCS :


# DICTIONARIES :

MOCKUP_PRODUCTS = [
    {
        "id": 1,
        "name": "Fregona",
        "description": "Fregona con microfibras",
        "category": "Limpieza",
        "brand":"Fregunix",
    },
    {
        "id": 2,
        "name": "Papel higienico",
        "description": "Papel de tres capas",
        "category": "Higiene",
        "brand":"Scotess",
    }
]


MOCKUP_PRODUCTS_STORAGE = [
    {
        "id": 1,
        "product_id": 1,
        "quantity": 2,
        "expiration_date": "n/a",
        "left_to_alert": 3
    },
    {
        "id": 2,
        "name": "Papel higienico",
        "quantity": 2,
        "expiration_date": "n/a",
        "left_to_alert": 3
    }
]

MOCK_SUPERMARKETS = [
    {
        "id":1,
        "name":MERCADONA,
    },
    {
        "id":2,
        "name":LIDL,
    },
]

MOCKUP_PRODUCTS_SUPERMARKET = [
    {
        "id":1,
        "product_id":1,
        "supermarket_id": 1,
        "stock":400,
        "price":2.99,
    },
    {
        "id":2,
        "product_id":1,
        "supermarket_id": 2,
        "stock":200,
        "price":3.99,
    }
]


## FUNCTIONS

def find_object_in_ist(target_list = None, key = None, value = None):
    '''Finds an object in a list given its desired key and value
    
    Arguments :
        - list : Target list to iterate
        - key : Key to search in the target list
        - value : Value to search in the object
    '''
    target_item = None
    if not key :
        raise Exception("Not key given")

    elif not value :
        raise Exception("Not value given")

    elif not target_list :
        raise Exception("Not target list given")

    else :
        for item in target_list :
            if item[key] == value:
                target_item = item



    return target_item

product_one = find_object_in_ist(MOCKUP_PRODUCTS,"id",1)

product_name = product_one["name"]
product_description = product_one["description"]
product_id = product_one["id"]


product_in_supermarket = find_object_in_ist(MOCKUP_PRODUCTS_SUPERMARKET,"product_id",product_id)

product_price = product_in_supermarket["price"]
supermarket_id = product_in_supermarket["supermarket_id"]

supermarket = find_object_in_ist(MOCK_SUPERMARKETS,"id",supermarket_id)
supermarket_name = supermarket["name"]


product_info = f"""
Producto : {product_name},
Descripcion : {product_description},
Price : {product_price},
Disponible en {supermarket_name}
"""

print(product_info)




## DATA CASTING:
'''
my_string = str(DEFAULT_QUANTITY_TO_ALERT)
my_number = int(MERCADONA)
my_float = float(MERCADONA)

'''