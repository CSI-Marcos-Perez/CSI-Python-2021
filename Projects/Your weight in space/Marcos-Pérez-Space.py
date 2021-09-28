planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("Calculate your weight in a different planet.")

MyWeight = int(input("What is your weight (pounds)?"))
MyPlanet = input(f"Select a planet from the list: {planets}")

def calculateWeight(planet, mass):
    print(f"\nEarth mass in pounds is: {mass}")

    W_kg = mass / 2.2046
    print(f"Mass in kg: {W_kg}")

    n_lb = 4.45

    planet_index = planets.index(planet)
    print(f"Weight in {planets[planet_index]} is {(W_kg * g_ms2[planet_index]) /n_lb} lb")

calculateWeight(MyPlanet, MyWeight)