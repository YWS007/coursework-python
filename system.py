'''
************************************************************************************************************************
                                                Function for display
************************************************************************************************************************
'''


# Print homepage options
def homepage():
    print("\t\tWELCOME!!!")
    print()
    print("\t1.Admin")
    print("\t2.New User")
    print("\t3.User")
    print("\t4.Exit")


# Print admin options
def admin_page():
    print("\t1. Upload medicine details")
    print("\t2. View all Medicines")
    print("\t3. Update/Modify medicines information")
    print("\t4. Delete medicines information")
    print("\t5. Search medicine")
    print("\t6. View all orders from customers")
    print("\t7. Search order of customer")
    print("\t8. Exit")


# Print new user options
def new_user_page():
    print("\t1. View medicines")
    print("\t2. Register")
    print("\t3. Back")


# Print user options
def user_page():
    print("\t1. View all Medicines")
    print("\t2. Place order of medicines and do payment")
    print("\t3. View own order")
    print("\t4. view personal information")
    print("\t5. Exit")


'''
************************************************************************************************************************
                                            Function for Read Data from File
************************************************************************************************************************
'''


# Read data from read_medicine_info_file and store data to list
def read_medicine_info_file(medicine_info):
    # open medicine_info.txt for read data file
    rf = open("medicine_info.txt", "r")
    # read data by lines and save those data to recorded_medicine
    recorded_medicine = rf.readlines()
    # using for loop to store data to a list, medicine_info
    for line in recorded_medicine:
        # remove space in the beginning of string
            new_line = line.strip()
        # split data with ','
            medicine_info.append(new_line.split(","))
   # close file
    rf.close()


# Read data from read_orders_info_file and store data to list
def read_orders_info_file(order_info):
    # open order_info.txt for read data file
    rf = open("order_info.txt", "r")
    # read data by lines and save those data to recorded_order
    recorded_order = rf.readlines()
    # using for loop to store data to a list, order_info
    for line in recorded_order:
        # remove space in the beginning of string
        new_line = line.strip()
        # split data with ','
        order_info.append(new_line.split(","))
    # close file
    rf.close()


# Read data from read_users_info_file and store data to list
def read_users_info_file(users_info):
    # open users_info.txt for read data file
    rf = open("users_info.txt", "r")
    # read data by lines and save those data to recorded_user
    recorded_user = rf.readlines()
    # using for loop to store data to a list, users_info
    for line in recorded_user:
        # remove space in the beginning of string
        new_line = line.strip()
        # split data with ','
        users_info.append(new_line.split(","))
    # close file
    rf.close()


# Read data from read_wallet_file and store data to list
def read_wallet_file(wallet):
    # open wallet.txt for read data file
    rf = open("wallet.txt", "r")
    # read data by lines and save those data to recorded_user
    recorded_wallet = rf.readlines()
    # using for loop to store data to a list, wallet
    for line in recorded_wallet:
        # remove space in the beginning of string
        new_line = line.strip()
        # split data with ','
        wallet.append(new_line.split(","))
    # close file
    rf.close()


'''
************************************************************************************************************************
                                            Function for Admin Application
************************************************************************************************************************
'''

# admin login by user_id: ocean123, password: 1234
def admin_login():
    # For loop to verify user's id and password
    for i in range(3):
        # input user's id
        user_id = input('User ID：')
        # input password
        password = input('Password：')
        # If user_id is ocean123, password is 1234, it will print welcome and stop the loop.
        if user_id == 'ocean123' and password == '1234':
            print('Welcome!')
            break
        # Else, user would have 3 attempts for login. If failed, user could not try it anymore.
        else:
            if i < 2:
                n = 2 - i
                print("Key in wrongly, another", n, "try")
            else:
                print("You couldn't try it anymore!")
        i += 1


# Function for admin upload medicine
def upload_medicine():
    # Open medicine_info.txt file for append
    f = open("medicine_info.txt", "a")
    # While loop for continue upload medicine
    while True:
        # input information of medicine
        medicine_name = input('Medicine name: ')
        expired_date = input('Expired date：')
        price = float(input('Price：'))
        specification = input('Specification: ')
        manufacture = input('Manufacture: ')

        # append those informations to medicine_info.txt
        f.write('\n' + medicine_name + ',' + expired_date + ',' + str(price) + ',' + specification + ',' + manufacture)
        # ask admin whether he wants to continue upload
        answer = input("Do you want to continue upload medicine？：'y/n'")
        if answer == 'y':
            continue
        else:
            break
    # display save successfully!
    print('save successfully!')
    f.close()


# Function for admin view medicine
def view_medicine():
    # declare info as list
    info = []
    # call read_medicine_info_file function
    read_medicine_info_file(info)
    # For loop for display the information
    for x in info:
        print("Medicine name: ", x[0], '\t', "Expired Date: ", x[1], '\t', "Price: ", x[2], '\t',
              "Specification: ", x[3], '\t', "Manufacture: ", x[4])


# Function for admin Update/modify medicine
def modify_medicine():
    # Declare info as a list
    info = []
    # call read_medicine_info_file function
    read_medicine_info_file(info)
    # While loop for continue modifying medicine
    while True:
        # Input modify_medicine
        modify_medicine = input("Which medicine do you want to modify? ")
        # For loop for search the specific medicine and modify the information
        for item in info:
            # If the medicine name in the info list is the same with the modify_medicine
            if item[0] == modify_medicine:
                # Display the information of medicine
                print("Medicine name: ", item[0], '\t', "Expired Date: ", item[1], '\t', "Price: ", item[2], '\t',
                      "Specification: ", item[3], '\t', "Manufacture: ", item[4])
                # Confirmation of the medicine
                confirm = input("Is this the medicine that you want to modify? y/n  ")
                # If confirmed, input the new information
                if confirm == 'y':
                    print("Please enter the new information for this medicine: ")
                    item[0] = input('Medicine name: ')
                    item[1] = input('Expired date：')
                    item[2] = float(input('Price：'))
                    item[3] = input('Specification: ')
                    item[4] = input('Manufacture: ')
                    print("Modify successful!")
                else:
                    break
        # Ask admin wthether he wants to continue modifying
        answer = input("Do you want to continue modify medicine？：'y/n'")
        if answer == 'y':
            continue
        else:
            break
    # open medicine_info.txt to write
    wf = open("medicine_info.txt", "w")
    # for loop for save the information in info to the medicine_info.txt
    for item in info:
        wf.write(item[0] + ',' + item[1] + ',' + str(item[2]) + ',' + item[3] + ',' + item[4] + '\n')
    # Close file
    wf.close()


# Function for admin to delete medicine
def delete_medicine():
    # Declare info as a list
    info = []
    # call read_medicine_info_file function
    read_medicine_info_file(info)
    # While loop for continue deleting medicine
    while True:
        # Input delete_medicine
        delete_medicine = input("Which medicine do you want to delete? ")
        # Declare i
        i = 0
        #  For loop for delete medicine
        for item in info:
            # If the medicine name in the info list is the same with the delete_medicine
            if item[0] == delete_medicine:
                # Display medicine information
                print("Medicine name: ", item[0], '\t', "Expired Date: ", item[1], '\t', "Price: ", item[2], '\t',
                      "Specification: ", item[3], '\t', "Manufacture: ", item[4])
                # Ask admin to confirm the medicine
                confirm = input("Is this the medicine that you want to delete? y/n  ")
                # If confirmed, delete
                if confirm == 'y':
                    info.pop(i)
                    print("Delete successful!")
                else:
                    break
            else:
                i = i + 1
        # Ask admin wheter he wants to continue
        answer = input("Do you want to continue delete？：'y/n'")
        if answer == 'y':
            continue
        else:
            break
    # open medicine_info.txt to write
    wf = open("medicine_info.txt", "w")
    # for loop for save the information in info to the medicine_info.txt
    for item in info:
        wf.write(item[0] + ',' + item[1] + ',' + str(item[2]) + ',' + item[3] + ',' + item[4] + '\n')
    # Close file
    wf.close()


# Function for admin to search medicine
def search_medicine():
    # Declare
    info = []
    medicine_name = []
    # call read_medicine_info_file function
    read_medicine_info_file(info)
    # While loop for continue searching medicine
    while True:
        # Input search_medicine
        search_medicine = input("Please input medicine name that you want to search: ")
        #  For loop for search medicine
        for item in info:
            # Append medicine name in info to a new list called medicine_name
            medicine_name.append(item[0])
            # If the medicine name if the same with search_medicine
            if item[0] == search_medicine:
                # Display
                print("Medicine name: ", item[0], '\t', "Expired Date: ", item[1], '\t',
                      "Price: ", item[2], '\t', "Specification: ", item[3], '\t', "Manufacture: ", item[4])
        # If search_medicine not in medicine_name, display "no this medicine"
        if search_medicine not in medicine_name:
            print("no this medicine")
        # Ask admin whether he wants to continue searching
        answer = input("Do you want to continue search？：'y/n'")
        if answer == 'y':
            continue
        else:
            break


# Function for admin view order
def view_order():
    # Declare
    order_info = []
    # call read_orders_info_file function
    read_orders_info_file(order_info)
    # Flor loop for display information in the order_info
    for x in order_info:
        print("User ID: ", x[0], '\t', "Medicine name: ", x[1], '\t', "Price: ", "{:.2f}".format(float(x[2])), '\t',
              "Quantity: ", x[3], '\t', "Amount: ", "{:.2f}".format(float(x[4])))


# Function for admin search order
def search_order():
    # Declare
    order_info = []
    user_id = []
    # call read_orders_info_file function
    read_orders_info_file(order_info)
    # While loop for admin to continue search order
    while True:
        # Input search_user_id
        search_user_id = input("Please input user ID that you want to search: ")
        # For loop for search order
        for item in order_info:
            # Append user id
            user_id.append(item[0])
            # If user id is the same with the search_user_id, display information
            if item[0] == search_user_id:
                print("User ID: ", item[0], '\t', "Medicine name: ", item[1], '\t', "Price: ",
                      "{:.2f}".format(float(item[2])), '\t', "Quantity: ", item[3], '\t', "Amount: ",
                      "{:.2f}".format(float(item[4])))
        # If search_user_id not in user_id, display "No this user ID."
        if search_user_id not in user_id:
            print("No this user ID.")
        # Ask admin whether he wants to continue
        answer = input("Do you want to continue search？：'y/n' ")
        if answer == 'y':
            continue
        else:
            break


'''
************************************************************************************************************************
                                            Function for New User Application
************************************************************************************************************************
'''


# Function for new customer register
def user_register():
    # Declare
    users = []
    # call read_users_info_file function
    read_users_info_file(users)
    # Input information
    print("Please input your information.")
    name = input("Name: ")
    gender = input("Gender (f/m): ")
    date_of_birth = input("Date of birth (dd/mm/yy): ")
    contact_no = input('Contact Number：')
    address = input("Address: ")
    email = input("Email : ")

    id = []
    # for loop for append user id in users to id
    for item in users:
        id.append(item[6])
    # While loop for checking whether the new user id had been used
    while True:
        user_id = input('User Id: ')
        if user_id in id:
            print("This user ID is already used. Please input other ID.")
            continue
        else:
            break
    # While loop for password verification
    while True:
        # Input password
        password = input('Password (between 6 to 10 characters): ')
        # If the length of password is not in between 6 and 10 need to rewrite password
        if len(password) >= 6 and len(password) <= 10:
            # While loop for verify the rewrite password is the same with the password
            while True:
                rewrite_password = input('Rewrite password: ')
                if rewrite_password == password:
                    print("Registered Successful!")
                    break
                else:
                    print("Password does not match! Please try again.")
            break
        else:
            print("Invalid password.")
    # Open the users_info.txt for append
    f = open("users_info.txt", "a")
    # write the information to file
    f.write('\n' + name + ',' + gender + ',' + date_of_birth + ',' + str(contact_no) +
            ',' + address + ',' + email + ',' + user_id + ',' + password)
    # Close file
    f.close()

    # Declare e-wallet balance for nre register customer
    wallet_balance = 0.00
    # Open the wallet.txt for append
    f = open("wallet.txt", "a")
    # write the information to file
    f.write('\n' + user_id + ',' + str(wallet_balance))
    # Close file
    f.close()


'''
************************************************************************************************************************
                                            Function for User Application
************************************************************************************************************************
'''


# Function for user to login
def user_login():
    # Declare
    global user_id
    users = []
    # call read_users_info_file function
    read_users_info_file(users)
    id = []
    # Save the user id in users to id
    for item in users:
        id.append(item[6])
    psw = []
    # Save the password in users to psw
    for item in users:
        psw.append(item[7])

    # For loop for verify the user id and password that inputing by user
    for i in range(3):
        # Input
        user_id = input('User ID：')
        password = input('Password：')
        # If the information is correct, display 'Welcome"
        if user_id in id and password in psw:
            print('Welcome!')
            break
        # Else, user would have 3 attemps for login. If they fail, the system will return to users interface
        else:
            if i < 2:
                n = 2 - i
                print("Key in wrongly, another", n, "try")
            else:
                print("You couldn't try it anymore!")
        i += 1
    # return user_id


# Function for user to order
def order():
    # Declare
    medicine_info = []
    # call read_medicine_info_file function
    read_medicine_info_file(medicine_info)
    # Declare
    store_name = []
    # For loop append item to store_name
    for item in medicine_info:
        store_name.append(item[0])
    # Declare
    medicine_name = []
    quantity = []
    price = []
    amount = []

    # While loop for user continue ordering medicine
    while True:
        print("Please enter the medicine name and quantities for order.")
        # Input information
        medicine_name_in = input('Medicine name: ')
        quantity_in = int(input('Quantity: '))
        # For loop for search medicine information
        for item in medicine_info:
            # If the medicine found, display the information
            if item[0] == medicine_name_in:
                print("Is this the medicine that you want to order?")
                print("Medicine name: ", item[0], '\t', "Expired Date: ", item[1], '\t', "Price: ",
                      "{:.2f}".format(float(item[2])), '\t', "Specification: ", item[3], '\t', "Manufacture: ", item[4])
                # Ask user to confirm order
                confirm = input("Is this the medicine that you want to order? y/n ")
                # If confirmed, append those information to different list
                if confirm == 'y':
                    medicine_name.append(item[0])
                    price.append(item[2])
                    quantity.append(quantity_in)
                else:
                    break
        # If medicine_name_in not in store_name, display no this medicine
        if medicine_name_in not in store_name:
            print("no this medicine")

        # Ask user whether he wants to continue order
        answer = input("Do you want to continue order？：'y/n'")
        if answer == 'y':
            continue
        elif answer == 'n':
            break
        else:
            print("No this options ")
            break

    # If there is information in medicine_name
    if len(medicine_name) >= 1:
        # Call print_order function and return amount
        amount = print_order(medicine_name, price, quantity)
    # Call print_order function
    remove_order(medicine_name, price, quantity, amount)

    # Open file for append
    af = open("order_info.txt", "a")
    # For loop to pass information to txt file
    for i in range(len(medicine_name)):
        af.write(user_id + ',' + medicine_name[i] + ',' + str(price[i]) + ',' + str(quantity[i]) + ',' + str(
            amount[i]) + '\n')
    # Close file
    af.close()

    # Declare
    total_amount = 0.00
    # For loop for calculating the total_amount
    for x in amount:
        total_amount = total_amount + x
    print("Total amount is : RM ", "{:.2f}".format(total_amount))

    print("Lets make payment now. ")
    # Call payment function
    payment(total_amount)


# Function for user to print order
def print_order(medicine_name, price, quantity):
    # Declare
    amount = []
    print("Please check your order: ")
    i = 0
    # While loop for printing orders in the cart
    while i < len(medicine_name):
        item_no = i + 1
        item_amount = float(price[i]) * float(quantity[i])
        amount.append(item_amount)
        print("Item number: ", item_no, '\t', "Medicine name: ", medicine_name[i], '\t', "Price: ",
                "{:.2f}".format(float(price[i])), '\t', "Quantity: ", quantity[i], '\t', "Amount: ",
                "{:.2f}".format(float(amount[i])))
        i += 1
    return amount


# Function for user to remove order
def remove_order(medicine_name, price, quantity, amount):
    confirm = input("Do you want to remove any items? y/n ")
    if confirm == 'y':
        #  While loop for deleting orders
        while True:
            # input medicine that user want to remove from cart
            remove = int(input("Which item number would you like to remove: "))
            i = remove - 1
            # delete the orders
            medicine_name.pop(i)
            price.pop(i)
            quantity.pop(i)
            amount.pop(i)
            # Ask user whether he wants to continue removing
            con = input("Continue remove? y/n ")
            #  If the user cease to contunue, display the orders
            if con == 'n':
                print("Your order: ")
                i = 0
                while i < len(medicine_name):
                    item_no = i + 1
                    print("Item number: ", item_no, '\t', "Medicine name: ", medicine_name[i], '\t', "Price: ",
                            "{:.2f}".format(float(price[i])), '\t', "Quantity: ", quantity[i], '\t', "Amount: ",
                            "{:.2f}".format(float(amount[i])))
                    i += 1
                break
            else:
                continue


# Function for user to make payment
def payment(total):
    # Declare
    wallet_balance = 0.00
    wallet = []
    # call wallet_file function
    read_wallet_file(wallet)

    # For loop to find the wallet balance using user ID
    for item in wallet:
        if item[0] == user_id:
            wallet_balance = float(item[1])

    # While loop for making payment
    while True:
        print('Balance in your e-wallet.txt: RM ', "{:.2f}".format(wallet_balance))
        # If the balance in e-wallet is sufficient, users can make payment, and the system will display the balance of e-wallet after payment is made.
        if wallet_balance >= total:
            confirm = input("Place order now? y/n ")
            if confirm == 'y':
                wallet_balance = wallet_balance - total
                print("Paid successful!")
                print('Balance in your e-wallet.txt: RM ', "{:.2f}".format(wallet_balance))
                print("Thank you for your order!")
                break
            else:
                break
        # If the balance is insufficient, users are required to top-up
        else:
            print("Balance insufficient.")
            print("Please top-up your e-wallet.")
            top_up = float(input("Top-up value: RM "))
            if top_up >= total:
                wallet_balance = wallet_balance + top_up
                print("Top-up successful!")
            else:
                wallet_balance = wallet_balance + top_up
                print("Top-up successful!")

    # For loop to replace the latest wallet balance
    for item in wallet:
        if item[0] == user_id:
            item[1] = wallet_balance

    # Open wallet.txt to write
    wf = open("wallet.txt", "w")
    #  For loop that save value to text file
    for item in wallet:
        wf.write(item[0] + ',' + str(item[1]) + '\n')
    # Close file
    wf.close()


# Function for user to view own order
def view_own_order():
    # Declare
    order_info = []
    # call read_orders_info_file function
    read_orders_info_file(order_info)
    # For loop to find and display the user's order information
    for item in order_info:
        if item[0] == user_id:
            print("Medicine name: ", item[1], '\t', "Price: ", "{:.2f}".format(float(item[2])), '\t',
                  "Quantity: ", item[3], '\t', "Amount: ", "{:.2f}".format(float(item[4])))


# Function for user to view personal info
def view_personal_info():
    # Declare
    personal_info = []
    # call read_users_info_file function
    read_users_info_file(personal_info)
    # For loop to find and display the user's personal information
    for item in personal_info:
        if item[6] == user_id:
            print("Name: ", item[0], '\t', "Gender: ", item[1], '\t', "Date of birth: ", item[2], '\t',
                  "Contact Number: ", (item[3]), '\t', "Address: ", item[4], '\t', "Email: ", item[5])


'''
************************************************************************************************************************
                                                        Main
************************************************************************************************************************
'''
# While loop for all users to access diffrent functions in the Ocean Sdn Bhd website
while True:
    # Call homepage function
    homepage()
    # Input options
    opt = int(input("Please choose your option: "))
    # If choose option 1, will access to admin interface
    if opt == 1:
        print()
        print("\t\ADMIN")
        print()
        print("\t1.Log in")
        print("\t2. Back")
        opt_admin = int(input("Select option: "))
        if opt_admin == 1:
            print("Hi")
            print("Please enter your user ID and password: ")
            # Call admin_login function
            admin_login()
            print()
            # While loop for admin to access different applications after logging in
            while True:
                # Call admin_page function
                admin_page()
                admin_access = int(input("Please choose your option: "))
                if admin_access == 1:
                    # Call upload_medicine function
                    upload_medicine()
                elif admin_access == 2:
                    # Call view_medicine function
                    view_medicine()
                elif admin_access == 3:
                    # Call modify_medicine function
                    modify_medicine()
                elif admin_access == 4:
                    # Call delete_medicine function
                    delete_medicine()
                elif admin_access == 5:
                    # Call search_medicine function
                    search_medicine()
                elif admin_access == 6:
                    # Call view_order function
                    view_order()
                elif admin_access == 7:
                    # Call search_order function
                    search_order()
                elif admin_access == 8:
                    break
                else:
                    print("No this option.")
        else:
            continue

    # If choose option 2, will access to new customer interface
    elif opt == 2:
        print()
        print("\t\tNEW USER")
        print()
        # While loop for new user to access different applications
        while True:
            # Call search_order function
            new_user_page()
            opt_new_user = int(input("Please choose your option: "))
            if opt_new_user == 1:
                # Call view_medicine function
                view_medicine()
            elif opt_new_user == 2:
                # Call user_register function
                user_register()
                break
            else:
                break

   # If choose option 3, will access to customer interface
    elif opt == 3:
        print()
        print("\t\tUser")
        print()
        print("\t1.Log in")
        print("\t2. Back")
        opt_user = int(input("Select option: "))
        if opt_user == 1:
            print("Hi")
            # Call user_login function
            user_login()
            print()
            # While loop for customer to access different applications after logging in
            while True:
                # Call user_page function
                user_page()
                user_access = int(input("Please choose your option: "))
                if user_access == 1:
                    # Call view_medicine function
                    view_medicine()
                elif user_access == 2:
                    # Call order function
                    order()
                elif user_access == 3:
                    # Call view_own_order function
                    view_own_order()
                elif user_access == 4:
                    # Call view_personal_info function
                    view_personal_info()
                elif user_access == 5:
                    break
                else:
                    # Display
                    print("No this option.")
        else:
            continue
    elif opt == 4:
        # Display and exit
        print("Thank you")
        break
    else:
        print("No this option.")