import requests, urllib3
urllib3.disable_warnings()

while True:
    user_input = input("Enter coin names u wanna know: \n-")
    coin_names = (user_input.lower()).split()
    if not coin_names:
        print("Input can't be empty :)")
        continue
    coins = ",".join(coin_names)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd"
    response = requests.get(url, verify=False, timeout=5)
    if not response.ok:
        print("API error")
        continue
    data = response.json()
    for coin in coin_names:
        if coin not in data:
            print(f"Such coin ({coin}) doesn't exist :(")
            continue
        price = data[coin]["usd"]
        print(f"Price for {coin}: {price} usd")
    break