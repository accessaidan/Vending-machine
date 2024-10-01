import time

global paid
global item_name
global cost
### Arrays needed ###
arr_coins = [1, 2, 5, 10, 20, 50, 100, 200]
arr_codes = ["wal", "dor", "wis", "twi", "cok", "pep", "har", "ski"]
arr_prices = [150, 175, 75, 65, 135, 135, 15, 25]
arr_items = [
    "Walkers",
    "Doritos",
    "Wispa",
    "Twix",
    "Coke",
    "Pepsi",
    "Haribo",
    "Skittles",
]


#################### Print selection subroutine #########################


def items_sub():
    print("The available items are:")
    print("Item    : cost : code ")
    print("walkers : 150  : Wal")
    print("Doritos : 175  : Dor ")
    print("Wispa   : 75   : Wis")
    print("Twix    : 65   : Twi")
    print("Coke    : 135  : Cok")
    print("Pepsi   : 135  : Pep")
    print("haribo  : 15   : Har")
    print("skittles: 25   : Ski")

print("")
paid = 0
item = ""
cost = 0

############################Coins subroutine ###############################


def coins_sub():
    global paid
    add_coins = 1
    while add_coins != 0:
        print(
            "Please enter the pence value of your chosen coin [Enter 0 to stop entering coins] :"
        )
        add_coins = int(input(""))
        if add_coins in arr_coins:
            paid = paid + add_coins
            print("You have paid", paid)
        elif add_coins == 0:
            print("")

        else:
            print("That is not a valid coin")
            print("Coin ejected")
            print("Please input a valid coin")
    return paid


##########################Item subroutine ########################################


def item_pick_sub():
    global item_name
    global cost
    print("Please enter the code for your desired item:")
    item = input("").lower()
    if item in arr_codes:
        print("")
        finding = "false"
        counter = 0
        while finding == "false":
            if item == arr_codes[counter]:
                finding = "true"
            else:
                counter = counter + 1

        item_name = arr_items[counter]
        cost = arr_prices[counter]
        confirm_sub()
    else:
        print("That is not a valid item")
        item_pick_sub()


########################### Confirm purchase ###########################


def confirm_sub():
    global paid
    global item_name
    global cost
    print(item_name, "will cost you", cost , "pence")
    var_confirm = input("Would you like to confirm your purchase [Y/N]").lower()
    if var_confirm == "y":
        paid_enough()
    elif var_confirm == "n":
        canc_or_new()
    else:
        print("Sorry that is not a valid input")
        confirm_sub()


######################### Cancel or new ######################


def canc_or_new():
    print("Would you like to cancel your purchase [C] or select a new item [N]")
    not_confirm = input("").lower()
    if not_confirm == "c":
        print("Okay bye")
        print("**Coins ejected**")

    elif not_confirm == "n":
        item_pick_sub()
    else:
        print("Sorry that was not a valid input")
        canc_or_new()


########################## Paid enough #############################


def paid_enough():
    global paid
    global item_name
    global cost
    if paid >= cost:
        change_needed()

    else:
        print("You havent paid enough")
        print("Would you like to change your purchase (C) or input more coins (M)")
        ch_or_more = input("").lower()
        if ch_or_more == "m":
            coins_sub()
            confirm_sub()
        elif ch_or_more == "c":
            items_sub()
            item_pick_sub()


################################# is there change ########################################


def change_needed():
    global paid
    global cost
    if paid > cost:
        change = paid - cost
        change_str = str(change)
        print("You are due" , change_str + "p change")
        print("*****Dispense" , change_str + "P*****")

    ending()


####################### Thanks for buying ##############################


def ending():
    global paid
    global item_name
    global cost
    time.sleep(3)
    ("Thank you for using the vending machine")
    print("*****Dispense", item_name + "*****")
    print("")
    print("")
    time.sleep(1)
    repeat_sub()


############################# Repeat ##############################


def repeat_sub():
    print("")
    print("")
    time.sleep(2)
    print("Would you like to use the vending machine again  [Y/N]")
    repeat = input("").lower()
    if repeat == "y":
        run_subs()
    elif repeat == "n":
        print("*****SHUTTING OFF*****")
    else:
        print("Sorry that is not a valid input")
        repeat_sub()


######################### SUB OF SUBS ##########################


def run_subs():
    items_sub()
    coins_sub()
    item_pick_sub()


################## Running Code ###########################
run_subs()