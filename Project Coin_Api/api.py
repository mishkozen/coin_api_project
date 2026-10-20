from fastapi import FastAPI, HTTPException

app = FastAPI()
@app.get("/price/{coin}")
def get_price(coin: str) -> dict:
    if coin.lower() not in {"bitcoin","ethereum","solana"}:
        raise HTTPException(status_code = 404,detail = "Coin not found")
    return {"coin": coin}