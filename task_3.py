world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
world_champions[2022] = 'Аргентина'
country = 'Италия'

def print_world_champions(champions_dict):
   for year, champion in champions_dict.items():
      print(year, '-', champion) 


def check_is_champion(country_to_check):
    result = False 
    for year, country_value in world_champions.items():
        if country_value == country_to_check and year >= 2000:
            result = True
    return result

def print_champion_message(is_champion):
    if is_champion == True:
        print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
    else:
        print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')


print_world_champions(world_champions)

is_champion = check_is_champion(country)
print_champion_message(is_champion)