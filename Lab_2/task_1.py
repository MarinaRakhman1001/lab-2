money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mounth = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while True:
    mounth += 1
    t = salary - spend
    money_capital += t
    spend *= increase + 1

    if money_capital < -t:
        break

print("Количество месяцев, которое можно протянуть без долгов:", mounth)
