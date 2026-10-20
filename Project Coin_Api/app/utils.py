import requests, urllib3, time, os, random, json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_DB = os.path.join(BASE_DIR, "DB_user.json")
COIN_DB = os.path.join(BASE_DIR, "DB_coin.json")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_info_user_db():
    with open(USER_DB,"r") as file:
        data = json.load(file)
    return data
def read_info_coin_db():
    with open(COIN_DB,"r") as file:
        data = json.load(file)
    return data
def registration():
    input_name = input("REGISTRATION\nEnter your name: ")
    clear_screen()
    input_password = input("REGISTRATION\nEnter your password: ")
    new_address = str(random.randint(100000,999999))
    new_portfolio = {}
    new_data = {
            "name":input_name,
            "password":input_password,
            "portfolio":new_portfolio
        }

    with open(USER_DB,"r") as file:
        data = json.load(file)
        file.close()
    data[new_address] = new_data
    with open(USER_DB,"w") as file:
        json.dump(data,file,indent=4)
        file.close()
    clear_screen()
    print("Relaunch program and login :)")

def login(data_dict):
    while True:
        input_address = input("LOGIN\nEnter your address: ")
        clear_screen()
        input_password = input("LOGIN\nEnter your password: ")
        if input_address not in data_dict:
            print("Wrong address :(")
            continue
        else:
            if data_dict[input_address]["password"] != input_password:
                print("Wrong password :(")
                continue
            else:
                received_name = data_dict[input_address]["name"]
                received_portfolio = data_dict[input_address]["portfolio"]
                return received_name, input_password, input_address, received_portfolio
def wellcome_page():
    clear_screen()
    option = input("Welcome to COINAPP\n\n1.Login\n2.Registration\n3.Exit\nChoose an option: ")
    clear_screen()
    return  option
def main_page(name):
    clear_screen()
    option = input(f"Welcome to COINAPP {name}\n"
                   f"1.Portfolio\n"
                   f"2.Coin Dashboard\n"
                   f"3.Buy Coin\n"
                   f"4.Sell Coin\n"
                   f"5.Exit\n"
                   f"Choose an option: ")
    return option
def portfolio_page(name, user_portfolio):
    clear_screen()
    if user_portfolio == {}:
        print("PORTFOLIO\n"
              "You don't have any Coins :(")
    else:
        print(f"PORTFOLIO\n"
              f"Hello {name} you have: ")
        for coin in user_portfolio:
            name = user_portfolio[coin]["name"]
            amount = user_portfolio[coin]["amount"]
            print(f"{name} : {amount}")
        input("Press enter to continue...")
def buy_page(user_portfolio):
    while True:
        clear_screen()
        coin_name = ((input("COINAPP\n"
                       "Coins you can buy: Bitcoin, Solana, Ethereum\n"
                       "Choose an coin: ")).lower()).strip()
        if coin_name == "bitcoin" or coin_name == "solana" or coin_name == "ethereum":
            break
    while True:
        clear_screen()
        try:
            amount = int(input("COINAPP\n"
                               "Enter amount: "))
            break
        except ValueError:
            print("Amount must be an number")
            continue
    if coin_name in user_portfolio:
        user_portfolio[coin_name]["amount"]+=amount
    else:
        user_portfolio[coin_name] = {
            "name": coin_name,
            "amount": amount
        }
    return user_portfolio
def sell_page(user_portfolio):
    clear_screen()
    if user_portfolio == {}:
        print("You don't have any coins :(")
        return user_portfolio
    else:
        while True:
            print("COINAPP\n"
                  "You can sell:")
            for coin in user_portfolio:
                name = user_portfolio[coin]["name"]
                amount = user_portfolio[coin]["amount"]
                print(f"{name} : {amount}")
            coin_name = ((input("Coin name: ")).lower()).strip()
            if coin_name in user_portfolio:
                clear_screen()
                break
            else:
                clear_screen()
                print(f"You don't have such coin({coin_name})")
                continue
    while True:
        try:
            amount = int(input("COINAPP\n"
                               "Enter amount: "))
        except ValueError:
            print("Amount must be an number")
            continue
        if user_portfolio[coin_name]["amount"]<amount:
            clear_screen()
            print("Not enough coins")
            continue
        elif user_portfolio[coin_name]["amount"]==amount:
            current_portfolio = {}
            for coin in user_portfolio:
                if coin != coin_name:
                    current_portfolio[coin] = user_portfolio[coin]
            user_portfolio = current_portfolio
            break
        else:
            user_portfolio[coin_name]["amount"] -= amount
            break
    return user_portfolio
def update_user_db(data_dict,address,user_portfolio):
    data_dict[address]["portfolio"] = user_portfolio
    with open(USER_DB,"w") as file:
        json.dump(data_dict,file,indent=4)
def update_coin_db(data_dict):
    with open(COIN_DB,"w") as file:
        json.dump(data_dict,file,indent=4)

def fetch_coin_price(coin_names: list[str], url: str) -> dict[str,dict[str, float]] | None:
    try: 
        response = requests.get(url,params={"ids": ",".join(coin_names),"vs_currencies": "usd" }, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        data = None
    return data
    
def price_trend(last_price: float, current_price: float) -> str:
    if last_price > current_price:
        change_price = "↓"
    elif last_price < current_price:
        change_price = "↑"
    else:
        change_price = "-"
    return change_price

def coin_dashboard(user_portfolio,data_dict):
    clear_screen()
    urllib3.disable_warnings()
    while True:
        user_input = input("Enter coin names price u wanna know: \n-")
        coin_names = (user_input.lower()).split()
        if not coin_names:
            print("Input can't be empty :)")
            continue
        url = "https://api.coingecko.com/api/v3/simple/price"
        index = 0
        while index<3:
            clear_screen()
            print("|-----COIN DASHBOARD-----|")
            api_prices = fetch_coin_price(coin_names, url)  
            if api_prices == None:
                time.sleep(15)
                index += 1
                continue
            else: 
                index = 0
            for coin in coin_names:
                if coin not in api_prices:
                    print(f"\nSuch coin ({coin}) doesn't exist :(")
                    continue
                price = api_prices[coin]["usd"]

                if coin not in data_dict:
                    price_change = "-"
                    data_dict[coin] = {
                        "last_price": price,
                        "max_price": price,
                        "min_price": price
                    }
                
                price_change = price_trend(data_dict[coin]["last_price"], price)

                if data_dict[coin]["max_price"]<price:
                    data_dict[coin]["max_price"] = price
                if data_dict[coin]["min_price"]>price:
                    data_dict[coin]["min_price"] = price
                print(f"\nPrice for {coin}: {price} usd {price_change}\n"
                      f"Last price: {data_dict[coin]["last_price"]}\n"
                      f"Max price: {data_dict[coin]["max_price"]}\n"
                      f"Min price: {data_dict[coin]["min_price"]}")
                if coin in user_portfolio:
                    print(f"You have {user_portfolio[coin]["name"]} coin in the amount {user_portfolio[coin]["amount"]}\n"
                          f"Which price is {(price*user_portfolio[coin]["amount"]):.2f} usd")
                data_dict[coin]["last_price"] = price
            time.sleep(5)
            exit_input = input("Enter 'exit' to stop the program or just enter to update data\n-")
            if exit_input == "exit":
                clear_screen()
                break
        if index >= 3:
            print("Api error :( \nTry to use dashboard later!")
        break
    return data_dict