past_cities = set()
future_cities = set()

past_input = input("Введіть міста, в яких ви були за минулі 10 років (через пробіл): ")
past_cities.update(past_input.lower().split())

future_input = input("Введіть міста, куди ви хочете поїхати наступні 10 років (через пробіл): ")
future_cities.update(future_input.lower().split())

input_cities = past_cities.intersection(future_cities)

if input_cities:
    common_cities_str = ', '.join(input_cities)
    print(f"Вам, мабуть, дуже сподобалося в містах: {common_cities_str}.".title())
else:
    print("Ви відкриті до чогось нового.".title())
