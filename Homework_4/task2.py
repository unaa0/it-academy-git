def country_gen(n):

    for val in range(n):
        first_country = input("Введите страну и города: ")
        first_country = first_country.strip().split()
        country, *cities = first_country

        yield country, cities


def find_country(countries_list, given_city):

    found_country = []

    for city in range(given_city):
        cities_to_compare = input("Введите название города: ")
        cities_to_compare = cities_to_compare.strip()

        for country, cities in countries_list:
            if cities_to_compare in cities:
                found_country.append(country)
                break

    return found_country


num_countries = int(input("Количество стран: "))
list_of_countries = (list(country_gen(num_countries)))

num_of_cities = int(input("Количество городов: "))
final_result = find_country(list_of_countries, num_of_cities)

for correct_country in final_result:
    print(correct_country)