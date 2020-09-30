def city_country(city, country, population=''):

    if population:
        formatted_city=f"{city}, {country} -population {population}"
    else:
        formatted_city=f"{city}, {country}"
    return formatted_city.title()

