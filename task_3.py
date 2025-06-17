world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

country = 'Италия'

def check_is_champion():
    for year, country_value in world_champions.items():
        if country_value == country and year >= 2000:
            print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
            return
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')

check_is_champion()