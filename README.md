# Coin API Project

A small Python terminal app for tracking a crypto portfolio. Users register or log in, view their holdings, buy and sell coins, and see live prices from the [CoinGecko API](https://www.coingecko.com/en/api). A FastAPI version is in progress (`api.py`).

## Features

- User registration and login
- Portfolio view
- Buy and sell coins
- Live coin dashboard with prices in USD, a price trend, and the min and max prices seen
- Data saved to local JSON files

## Project structure

```
Project Coin_Api/
├── main.py         # Terminal app entry point (menu loop)
├── api.py          # FastAPI app (work in progress)
├── app/
│   ├── user.py     # User class
│   └── utils.py    # Menus, buy/sell logic, price fetching, DB read/write
├── DB_user.json    # Users and portfolios
└── DB_coin.json    # Last, min, and max price per coin
```

## Setup

Requires Python 3.13+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]" requests truststore
```

## Run

```bash
cd "Project Coin_Api"
python main.py        # terminal app
fastapi dev api.py    # API dev server at http://127.0.0.1:8000
```
