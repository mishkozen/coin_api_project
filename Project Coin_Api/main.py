from app.utils import registration, login, wellcome_page, coin_dashboard,read_info_user_db,read_info_coin_db, main_page,buy_page,sell_page, update_user_db,update_coin_db,portfolio_page
from app.user import User
while True:
    data = read_info_user_db()
    data_coin = read_info_coin_db()
    while True:
        option = wellcome_page()
        match option:
            case "1":
                (received_name,
                 received_password,
                 received_address,
                 received_portfolio) = login(data)
                User_info = User(received_name,
                                 received_password,
                                 received_address,
                                 received_portfolio)

                break
            case "2":
                registration()
                break
            case "3":
                break
    if option == "2" or option == "3":
        break

    while True:
        option = main_page(User_info.get_name())
        match option:
            case "1":
                portfolio_page(User_info.get_name(),User_info.get_portfolio())
            case "2":
                data_coin = coin_dashboard(User_info.get_portfolio(),data_coin)
            case "3":
                current_portfolio = buy_page(User_info.get_portfolio())
                User_info.set_portfolio(current_portfolio)
            case "4":
                current_portfolio = sell_page(User_info.get_portfolio())
                User_info.set_portfolio(current_portfolio)
            case "5":
                break
    update_user_db(data,User_info.get_address(),User_info.get_portfolio())
    update_coin_db(data_coin)
    break
