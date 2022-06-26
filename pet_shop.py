# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, amount):
    current_money = get_total_cash(shop)
    new_total_cash = amount + current_money
    shop["admin"]["total_cash"] = new_total_cash
    return None


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, pets_gone):
    current_number = get_pets_sold(shop)
    new_pets_number = pets_gone + current_number
    shop["admin"]["pets_sold"] = new_pets_number
    return None


def get_stock_count(shop):
    return len(shop["pets"])


# TypeError: string indices must be integers
def get_pets_by_breed(shop, breed_name):
    pets_per_breed = 0
    for breed_type in shop:
        if breed_type["pets"]["breed"] == breed_name:
            pets_per_breed += 1
        else:
            pets_per_breed += 0
    return pets_per_breed


# TypeError: string indices must be integers
def find_pet_by_name(shop, pet_name):
    found_pet = None
    for pet_item in shop:
        if pet_item["pets"]["name"] == pet_name:
            found_pet = pet_item
            return found_pet
        else:
            return found_pet


# TypeError: string indices must be integers
def remove_pet_by_name(shop, pet_name):
    shop["pets"]["name"].remove(pet_name)


# TypeError: string indices must be integers
def add_pet_to_stock(shop, pet_name):
    shop["pets"]["name"].append(pet_name)


def get_customer_cash(cust_info):
    return cust_info["cash"]


# TypeError: list indices must be integers or slices, not str
def remove_customer_cash(cust_info, rem_cash):
    for amount in cust_info["cash"]:
        amount -= rem_cash
    return amount


def get_customer_pet_count(cust_info):
    return cust_info["pets"]    


def add_pet_to_customer(cust_info, pet_info):
    cust_new_pets = 0
    if pet_info == True and cust_info["pets"] == None:
        cust_new_pets += 1
        cust_info["pets"].append(cust_new_pets)
    elif pet_info == True and cust_info["pets"] == True:
        cust_info["pets"] =+ 1








