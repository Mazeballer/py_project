#Chen Zi Rong
#TP073585

# Begin-----------------------

import os
import csv
import getpass

info_list = []
info_code = []
info_description = []
position = []
iden_list = []
iden = []
txtfile = "inventory.txt"

# homepage function ----------

def admin_home():
    clear()
    print("Grocer Store Inventory System")
    print("-----------------------------")
    print()
    print("Available Option:")
    print()
    print("1 - Insert stock. ")
    print("2 - Update stock. ")   
    print("3 - Delete stock. ")
    print("4 - Stock taking. ")
    print("5 - View replenish. ")
    print("6 - Stock replenish. ")
    print("7 - Search stock. ")
    print("8 - View all stock. ")
    print("9 - Add new user. ")
    print("10 - Delete user. ")
    print("11 - Log out")
    print()
    
    while True:
        choise = input("Choose an option. ")
        if choise == "1":
            insert_stock()
            break
        elif choise == "2":
            update_stock()
            break
        elif choise == "3":
            delete_stock()
            break
        elif choise == "4":
            stock_taking()
            break
        elif choise == "5":
            view_replenish()
            break
        elif choise == "6":
            stock_replenish()
            break
        elif choise == "7":
            search_stock()
            break
        elif choise == "8":
            view_all_stock()
            break
        elif choise == "9":
            add_new_user()
            break
        elif choise == "10":
            dlt_user()
            break
        elif choise == "11":
            logout()
            break
        else :
            print("Do not have this option. (Option must be a digit)")
            continue
 
def checker_home():
    clear()
    print("Grocer Store Inventory System")
    print("-----------------------------")
    print()
    print("Available Option:")
    print()
    print("1 - Stock taking. ")
    print("2 - Search stock. ")
    print("3 - View all stock. ")
    print("4 - Log out")
    print()
    
    while True:
        choise = input("Choose an option. ")
        if choise == "1":
            stock_taking()
            break
        elif choise == "2":
            search_stock()
            break
        elif choise == "3":
            view_all_stock()
            break
        elif choise == "4":
            logout()
            break
        else :
            print("Do not have this option. (Option must be a digit)")
            continue

def purchaser():
    clear()
    print("Grocer Store Inventory System")
    print("-----------------------------\n")
    print("Available Option: \n")
    print("1 - View replenish. ")
    print("2 - Stock replenish. ")
    print("3 - View all stock. ")
    print("4 - Log out")
    print()
    
    while True:
        choise = input("Choose an option. ")
        if choise == "1":
            view_replenish()
            break
        elif choise == "2":
            stock_replenish()
            break
        elif choise == "3":
            view_all_stock()
            break
        elif choise == "4":
            logout()
            break
        else :
            print("Do not have this option. (Option must be a digit)")
            continue

# main fuction----------------

def insert_stock():
    clear()
    print("Insert Item into Inventory. \n")
    print("---------------------------\n")
    print("Available option.\n")
    print("1 - Insert one item. ")
    print("2 - Insert two or more items. \n")
    choise = input("Choose an option. \n")
    add_info_tolist()
    code_des_list()
    if choise == "1":
        clear()
        new_info_list = []
        while True:    
            code = input("Enter the code of the item. ")
            if len(code) == 5 and int(code) > 10000 and code not in info_code:
                break
            elif int(code) < 10000 and len(code) != 5 and code not in info_code:
                print("Code start from 10000 .(5 digit)" )
                print()
                continue
            elif code in info_code:
                print("This code have already exists, change another code. ")
                print()
                continue   
        while True:    
            description = input("Enter the description of the item. ")
            if description.lower() not in info_description:
                break
            elif description.lower() in info_description:
                print("Description have already exists, change another description. ")
        category = input("Enter the category of the item. ")
        unit = input("Enter the units of the items. ") 
        price = float(input("Enter the price of the item. "))
        prices = str("{:.2f}".format(float(price)))
        quantity = input("Enter the quantity of the item. ")
        minimum = input("Enter the minimum threshold of the item. ")
        new_info_list = [new_info_list,code,description,category,unit,prices,quantity,minimum]
        info_list.append(new_info_list)
    
    elif choise == "2":
        clear()
        new_info_list = []
        while True:
            num_item = input("How many items have to be inserted? ")
            if num_item.isdigit():
                break
            else :
                print("Input must be a digit")
        num_item = int(num_item)
        for i in range(num_item):
            while True:    
                code = input("Enter the code of the item. ")
                if len(code) == 5 and int(code) > 10000 and code not in info_code:
                    break
                elif code in info_code:
                    print("This code have already exists, change another code. \n")
                    continue
                elif int(code) < 10000 and len(code) != 5:
                    print("Code start from 10000 .(5 digit)\n" )
                    continue 
            while True:    
                description = input("Enter the description of the item. ")
                if description.lower() not in info_description:
                    break
                elif description.lower() in info_description:
                    print("Description have already exists, change another description. ")
            category = input("Enter the category of the item. ")
            unit = input("Enter the units of the items. ") 
            price = float(input("Enter the price of the item. "))
            prices = str("{:.2f}".format(float(price)))
            quantity = input("Enter the quantity of the item. ")
            minimum = input("Enter the minimum threshold of the item. ")
            print()
            new_info_list = [code,description,category,unit,prices,quantity,minimum]
            info_list.append(new_info_list)
    rewrite_info() #rewrite
    new_info_list.clear()
    list_clear()
    print("Insert successfully. ")
    go_home()
    print()

def update_stock():
    clear()
    add_info_tolist()
    code_des_list()
    print("Update Item\n")
    print("------------\n")
    while True:
        code = input("Enter the code of the item that you want to update. ")
        if code in info_code:
            break
        else:
            print("Invalid code! ")
            print("Enter another code. ")
            print()
            continue           
    for i in range(len(info_list)):
        if info_list[i][0] == code:
            pos = i
    clear()
    print("Available option for update. \n")
    print("----------------------------\n")
    print("1 - Update Code ")
    print("2 - Update Description. ")
    print("3 - Update Category. ")
    print("4 - Update Unit. ")
    print("5 - Update Price. ")
    print("6 - Update Minimum. \n")
    choice = input("Enter your option. ")
    if choice == "1":
        while True:    
            new_code = input(f'Enter the new code for {code}. ')
            if len(new_code) == 5 and int(new_code) >= 10000 and new_code not in info_code:
                break
            elif new_code.isdigit() == False :
                print("Code must be a digit. ")
            elif int(new_code) < 10000 and len(new_code) != 5 and new_code not in info_code:
                print("Code start from 10000. (5 digit)")
                print()
                continue
            elif new_code in info_code:
                print("Code already exists, change another code. ")
                print()
                continue
            else:
                print("Please enter again. ")
                continue
        info_list[pos][0] = new_code
        info_code[pos] = new_code
        rewrite_info() #rewrite
        
    elif choice == "2":
        while True:    
            new_description = input(f'Enter the new description for {code}. ')
            if new_description.lower() not in info_description:
                break
            elif new_description.lower() in info_description:
                print("Description have already exists, change another description. ")
            else:
                print("Please enter again. ")
        info_list[pos][1] = new_description
        info_description[pos] = new_description
        print()
        rewrite_info() #rewrite
        
    elif choice == "3":
        while True:
            new_category = input(f'Enter the new category for {code}. ')
            if new_category == " ":
                print("Input can't be a blank. ")
                continue
            else: 
                break
        info_list[pos][2] = new_category
        print()
        rewrite_info() #rewrite
        
    elif choice == "4":
        while True:
            new_unit = input(f'Enter the new unit for {code}. ')
            if new_unit == " ":
                print("Input can't be a blank.")
                continue
            else:
                break
        info_list[pos][3] = new_unit
        print()
        rewrite_info() # rewrite
        
    elif choice == "5":
        while True:
            new_price = float(input(f'Enter the new price for {code}. '))
            if new_price > 0 :
                try:
                    new_prices = str("{:.2f}".format(float(new_price)))
                    break
                except:
                    print("Price must be a number. ")
                    continue    
            else:
                print("The input must be a positive number. ")
                print()
                continue
        info_list[pos][4] = new_prices
        print()
        rewrite_info() #rewrite
        
    elif choice == "6":
        while True:
            new_minimum = int(input(f'Enter the new minimum for {code}. '))
            if str(new_minimum).isdigit() == True and int(new_minimum) >= 0:
                break
            else:
                print("The input must be a digit. (positive number)")
                print()
                continue
        new_minimum = str(new_minimum)
        info_list[pos][6] = new_minimum
        print()
        rewrite_info() #rewrite
    list_clear()
    print("Update successfully. \n")
    go_home()

def delete_stock():
    clear()
    print("Delete Item\n")
    print("------------\n")
    add_info_tolist()
    code_des_list()
    while True:
        while True:
            delete_item_code = str(input("Please enter the code of the item that wanted to delete. "))
            if delete_item_code not in info_code:
                print("No item with this code! ")
                print("Enter another code. ")
            else: 
                break
        if delete_item_code in info_code:
            print(f'Do you sure {delete_item_code} is the code of the item you wanted to delete ? ')
            print("1 - Yes")
            print("2 - No\n")
            choice = input("Enter your option. (1/2) ")
        if choice == "1":
            for i in range(len(info_code)):
                if info_code[i] == delete_item_code :
                    pos = i
                    break              
            info_list.remove(info_list[pos])
            break   
        elif choice == "2":
            print()
            continue
        else:
            print("Enter again. ")
    rewrite_info() #rewrite
    list_clear()
    print("Deleted successfully. \n")
    go_home()

def stock_taking():
    clear()
    print("Stock Taking \n")
    print("--------------\n")
    add_info_tolist()
    code_des_list()
    print(info_code)
    while True:    
        code = input("Please enter the code of the stock to be took. ")
        if code in info_code:
            break
        elif code not in info_code:
            print("Invalid code! ")
            continue
        else:
            print("Enter again. ")
    for i in range(len(info_list)):
        if code in info_code[i]:
            pos = i
    while True:
        while True:
            quantity_take = input("The quantity of item to be took. ")
            if quantity_take.isdigit() == True and int(quantity_take) >= 1:
                break
            else:
                print("The input must be a digit. (positive number)")
                continue
        if int(info_list[pos][5]) > int(quantity_take) :    
            info_list[pos][5] = int(info_list[pos][5]) - int(quantity_take)
            info_list[pos][5] = str(info_list[pos][5])
            break
        elif int(info_list[pos][5]) < int(quantity_take) :
            print("Stock Insufficient! ")
            continue
    rewrite_info() #rewrite
    list_clear()
    print("Took Successfully. \n")
    go_home()  

def view_replenish():
    clear()
    add_info_tolist()
    print("Check for Replenish. \n")
    print("--------------------\n")
    found = False
    for i in range(len(info_list)):
        if int(info_list[i][5]) < int(info_list[i][6]):
            found = True
            position.append(i)
    if found == True:
        for j in position:
            print(f'Code : {info_list[j][0]}, Description : {info_list[j][1]}, has to be replenished. ')   
    if found == False:
        print("No stock has to be replenished. ")
    position.clear()
    list_clear()
    print()
    go_home()

def stock_replenish():
    clear()
    print("Stock Replenish\n")
    print("----------------\n")
    add_info_tolist()
    code_des_list()
    while True:    
        code = input("Please enter the code of the stock to be replenished. \n")
        if code in info_code:
            break
        elif code not in info_code:
            print("Invalid code! ")
            continue
    for i in range(len(info_list)):
        if code in info_code[i]:
            pos = i 
    while True:
        quantity_replenish = input("The quantity of stock to be replenished. \n")
        if quantity_replenish.isdigit() == True and int(quantity_replenish) > 0:
            break
        else:
            print("The input must be a digit. (positive number)")
            continue
    info_list[pos][5] = int(info_list[pos][5]) + int(quantity_replenish)
    info_list[pos][5] = str(info_list[pos][5])
    rewrite_info() #rewrite
    list_clear()
    print("Replenished Successfully. \n")
    go_home() 

def search_stock():
    clear()
    print("Search stock in Inventory. \n")
    print("--------------------------")
    print("Available options. \n")
    print("1 - Search stock by description. ")
    print("2 - Search stock by code range. ")
    print("3 - Search stock in a specific category. ")
    print("4 - Search stock in a specific price range. \n")
    add_info_tolist()
    code_des_list()
    while True:
        choice = input("Please choose an option. ")
        if choice.isdigit() == True:
            break
        else :
            print("Do not have this option. (Option must be a digit.)")
    
    if choice == "1":
        clear()
        while True:    
            item_description = input("Please enter the description of the stock. ")
            if item_description in info_description:
                break
            else :
                print("\nDescription does not exists, change another description. \n")
                continue       
        item_description_low = item_description.lower()
        search_item_bydescription(item_description_low)
        print()
        go_home()
        
    if choice == "2":
        clear()
        while True:
            item_code_min = int(input("Please enter the minimum code range of the stock. "))
            item_code_max = int(input("Please enter the maximum code range of the stock. "))
            print()
            if len(str(item_code_min)) == 5 and len(str(item_code_max)) == 5:
                break
            else:
                print("\nCodes must be a 5 digit number. \n")
                continue
        item_code = range(item_code_min,item_code_max + 1)
        codes = []
        for i in item_code:
            codes.append(str(i))
        search_item_bycode(codes)
        print()
        go_home()
    
    if choice == "3":   
        clear()
        item_category = input("Please enter the category of the stock. ")
        item_category_low = item_category.lower()
        search_item_bycategory(item_category_low)
        print()
        position.clear()
        go_home()
         
    if choice == "4":
        clear()
        while True:
            item_price_min = float(input("Please enter the minimum price range of the stock. "))
            item_price_max = float(input("Please enter the maximum price range of the stock. "))
            print()
            if str(int(item_price_min)).isdigit() == True and str(int(item_price_max)).isdigit():
                break
            else:
                print("\nPrice must be a number. \n")
                continue
        search_item_byprice(item_price_min,item_price_max)
        print()
        go_home()
        
def view_all_stock():
    clear()
    print("All stock in grocery store.\n")
    print("---------------------------\n")
    files = open(txtfile,"r")
    for lines in files:
        print(lines)
    print()
    go_home()

def add_new_user():
    clear()
    print("Add New User ")
    print("--------------\n")
    add_iden_tolist()
    new_iden = []
    while True:    
        found = False
        username = input("New username: ")
        for i in range(len(iden_list)):
            if username == iden_list[i][0]:
                found = True
        if found == False:
            break
        else:
            print("Username already exists, change another username. ")            
    password = input("New password: ")
    while True:
        identity = input("""Which identity :
(admin/inventory-checker/purchaser). """)
        if identity == "admin" or identity == "inventory-checker" or identity == "purchaser" :
            break
        else:
            print("Do not have this indendity. ")
    new_iden = [username,password,identity]
    iden_list.append(new_iden)
    rewrite_iden()
    iden_list.clear()
    print("\nAdded new user. ")
    go_home()

def dlt_user():
    clear()
    add_iden_tolist()
    print("Delete User \n")
    while True:
        found = False
        username = input("Delete username: ")
        for i in range(len(iden_list)):
            if username == iden_list[i][0]:
                pos = i
                found = True
        if found == True:
            break
        else:
            print("Username do not exists. ")
            continue
    iden_list.remove(iden_list[pos])
    rewrite_iden()
    iden_list.clear()
    print("\nDeleted user. ")
    go_home()
 
def logout():
    clear()
    iden.clear()
    list_clear()
    login()

# support function------------------

def add_info_tolist():
    with open(txtfile,"r") as inv_file :
        reader = csv.reader(inv_file)
        for lines in reader :
            info_list.append(lines)

def add_iden_tolist():
    with open("login.txt","r") as inv_file :
        reader = csv.reader(inv_file)
        for lines in reader :
            iden_list.append(lines)

def code_des_list():
    for i in range(len(info_list)):
        info_code.append(info_list[i][0])
        info_description.append(info_list[i][1])

def go_home():
    if iden[0] == "admin":
        while True:
            go_back = input("Enter b to return to homepage. ")
            if go_back.lower() == "b":
                admin_home()
                break
            else:
                continue
    elif iden[0] == "checker":
        while True:
            go_back = input("Enter b to return to homepage. ")
            if go_back.lower() == "b":
                checker_home()
                break
            else:
                continue
    elif iden[0] == "purchaser":
        while True:    
            go_back = input("Enter b to return to homepage. ")
            if go_back.lower() == "b":
                purchaser()
                break
            else:
                continue

def search_item_bydescription(item_description_low):
    found = False
    for item in info_list:
        if item[1] == item_description_low :
            found = True
            pos = info_list.index(item)
            print(f"""Code : {info_list[pos][0]}, Description : {info_list[pos][1]}, Category : {info_list[pos][2]}
Unit : {info_list[pos][3]}, Price : {info_list[pos][4]}, Quantity : {info_list[pos][5]}, Minimum : {info_list[pos][6]}""")
    info_list.clear()

    if found == False:
        print("Do not have this description. ")
    
def search_item_bycode(item_code_list):
    found = False
    for i in range(len(info_list)):
        if info_list[i][0] in item_code_list:
            found = True
            pos = i
            print(f"""Code : {info_list[pos][0]}, Description : {info_list[pos][1]}, Category : {info_list[pos][2]}
Unit : {info_list[pos][3]}, Price : {info_list[pos][4]}, Quantity : {info_list[pos][5]}, Minimum : {info_list[pos][6]}""")
            print()
    info_list.clear()        
    if found == False:    
        print("Do not have any item in this code range.")
    
def search_item_bycategory(item_category_low):
    found = False
    for i in range(len(info_list)):
        if info_list[i][2] == item_category_low :
            found = True
            position.append(i)
    for j in position:
        print(f"""Code : {info_list[j][0]}, Description : {info_list[j][1]}, Category : {info_list[j][2]}
Unit : {info_list[j][3]}, Price : {info_list[j][4]}, Quantity : {info_list[j][5]}, Minimum : {info_list[j][6]}""")
        print()
    info_list.clear()

    if found == False:
        print("Do not have this item in this category. ")

def search_item_byprice(price_min,price_max):
    found = False
    for i in range(len(info_list)):
        if float(info_list[i][4]) > float(price_min) and float(info_list[i][4]) < float(price_max):
            found = True
            pos = i
            print(f"""Code : {info_list[pos][0]}, Description : {info_list[pos][1]}, Category : {info_list[pos][2]}
Unit : {info_list[pos][3]}, Price : {info_list[pos][4]}, Quantity : {info_list[pos][5]}, Minimum : {info_list[pos][6]}""")
            print()
    info_list.clear()      
    if found == False:
        print("Do not have this item in this price range. ") 

def rewrite_info():
    files = open(txtfile,"w")
    files.write("")
    for item in info_list:    
        new_txt = ",".join(item)
        files.write(new_txt + "\n")

def rewrite_iden():
    files = open("login.txt","w")
    files.write("")
    for item in iden_list:    
        new_txt = ",".join(item)
        files.write(new_txt + "\n")
    iden_list.clear()

def list_clear():
    info_list.clear()
    info_code.clear()
    info_description.clear()

def clear():
    if os.name == "nt":  # for Windows OS
        _ = os.system("cls")
    else:
        _ = os.system("clear")


# login---------------------------

def login():
    clear()
    print("Welcome to Grocery login Site.\n")
    print("-------------------------------\n")
    add_iden_tolist()
    correct = False
    while True:    
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        for i in range(len(iden_list)):
            if username == iden_list[i][0] and password == iden_list[i][1]:
                correct = True
                pos = i
        if correct == False:
            print("\nIncorrect password or username. \nTry again. ")
            continue
        else: 
            break
    if iden_list[pos][2] == "admin":
        iden.append("admin")
        iden_list.clear()
        admin_home()
    elif iden_list[pos][2] == "inventory-checker":
        iden.append("checker")
        iden_list.clear()
        checker_home()
    else:
        iden_list.clear()
        iden.append("purchaser")
        purchaser()

login()








