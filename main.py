import math

print("Drake equation 2.0")

number_of_galaxies = float(input("How many billion galaxies are there in the universe?: ")) * 1000000000
number_of_stars = float(input("Average amount of stars per galaxy in millions?: ")) * 1000000
viable_stars = float(input("Percent of G-type stars?: ")) / 100
goldilocks_stars = float(input("What percentage of these stars are in the goldilocks zone of galaxies?: ")) / 100
average_number_of_planets = float(input("Average amount of planets per star?: "))
percent_of_rocky_planets = float(input("What percent of planets are rocky?: ")) / 100
#average_number_of_moons_per_gas_giant = float(input("Average number of moons per gas giant?: "))
#viable_sized_moons = float(input("What percent of moons are large enough to have a magnetic field?: "))
#percent_of_ggm_in_goldilocks_zone_of_gg = float(input("Percent of gas giant moons in goldilocks?: ")) / 100
percent_of_planets_in_goldilocks_zone = float(input("Percent of planets in goldilocks zone?: ")) / 100
percent_of_moons_planets_with_magnetic_field = float(input("Percent of planets or moons with active core?: ")) / 100
percent_of_rocky_planets_with_a_moon = float(input("What percent of rocky planets have at least 1 large moon?: ")) / 100
percent_of_planets_with_water = float(input("Percent of planets or moons with water?: ")) / 100
percent_of_planets_moons_where_life_develops = float(input("Percent of planets or moons where life develops?: ")) / 100
percent_of_planets_moons_that_have_a_mix_of_land_water = float(input("Percent of water planets or moons with land?: ")) / 100
percent_of_life_that_becomes_intelligent = float(input("Percent of life that becomes intelligent?: ")) / 100
percent_of_intelligent_life_that_creates_technology = float(input("Percent of intelligent life that develops technology?: ")) / 100
average_lifespan_of_civilizations = float(input("Average number of years a technologically advanced society survives?: "))

number_of_viable_solar_systems = number_of_galaxies * number_of_stars * viable_stars * goldilocks_stars
number_of_viable_planets = number_of_viable_solar_systems * average_number_of_planets * percent_of_rocky_planets * \
                           percent_of_rocky_planets_with_a_moon
#number_of_viable_moons = number_of_viable_solar_systems * average_number_of_moons_per_gas_giant * \
#                         percent_of_ggm_in_goldilocks_zone_of_gg * viable_sized_moons
probability_of_life = number_of_viable_planets * percent_of_planets_in_goldilocks_zone * \
                       percent_of_moons_planets_with_magnetic_field * percent_of_planets_with_water * \
                       percent_of_planets_moons_that_have_a_mix_of_land_water * \
                       percent_of_planets_moons_where_life_develops * percent_of_life_that_becomes_intelligent * \
                       percent_of_intelligent_life_that_creates_technology * average_lifespan_of_civilizations

print(f"The number of civilizations capable of communication in the universe is: {probability_of_life} or {probability_of_life/number_of_galaxies} per galaxy")

