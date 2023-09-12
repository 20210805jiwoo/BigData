shops = [
    {'name': 'A_market', 'length': 33, 'count': 30, 'price': 13550},
    {'name': 'B_market', 'length': 35, 'count': 24, 'price': 15960},
    {'name': 'C_market', 'length': 30, 'count': 33, 'price': 11990},
]

lowest_price = float('inf') #무한대 값
cheapest = None

for shop in shops:	#shop에 현재 순회 중인 상점 정보 저장
    price_per_meter = shop['price'] / (shop['length'] * shop['count'])
    if price_per_meter < lowest_price:
        lowest_price = price_per_meter
        cheapest = shop

print(f'{cheapest["name"]}이 1m당 {lowest_price:.2f}으로 최저가이다')
