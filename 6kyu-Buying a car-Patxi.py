def nbMonths(old_car_price, new_car_price, saving_per_month, percent_loss_by_month):
    savings = 0
    month = 1
    while old_car_price + savings < new_car_price:
        if month % 2 == 0:
            percent_loss_by_month += 0.5
        month += 1
        new_car_price -= new_car_price * percent_loss_by_month / 100
        old_car_price -= old_car_price * percent_loss_by_month / 100
        savings += saving_per_month
    return [month - 1, round(savings + old_car_price - new_car_price)]

