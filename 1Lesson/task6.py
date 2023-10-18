rub_to_usd = float(input("Введите курс: "))
usd_to_evro = float(input("Введите курс: "))
rub_to_evro = rub_to_usd * usd_to_evro
evro_to_rub = 1 / rub_to_evro
print(rub_to_evro)
print(round(evro_to_rub,2))