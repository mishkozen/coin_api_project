from fastapi import FastAPI, HTTPException
import requests, truststore
truststore.inject_into_ssl()

API_URL = "https://api.coingecko.com/api/v3/simple/price"

app = FastAPI()
@app.get("/price/{coin}")
def get_price(coin: str) -> dict:
    coin = coin.lower()
    try:
        response = requests.get(API_URL,params={"ids": coin,"vs_currencies" : "usd"}, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        raise HTTPException(status_code= 503, detail=f"Can't conect to API server \nError 503")
    if coin not in data:
        raise HTTPException(status_code = 404,detail = "Coin not found")
    return {"coin": coin, "usd":data[coin]["usd"]}