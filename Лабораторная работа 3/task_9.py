salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

while True:
    delta = spend - salary
    if (delta > 0) and (months > 0):
        money_capital += delta
    else:
        break

    months -= 1
    spend *= 1 + increase

print(round(money_capital))
