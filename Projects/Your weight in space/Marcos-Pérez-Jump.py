print("Jumping on other planets")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
MyJump = float(input("What is your jump's length (meter)?"))
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]
MyPlanet = input(f"Select a planet from the list: {planets}")


def calculateLength(planet, jump) :
    print(f"Your jump on Earth is: {jump}")


    Planet_index = planets.index(planet)
    print(f"Length in {planets[Planet_index]} is {MyJump*rel_gravity[Planet_index]}")

calculateLength(MyPlanet, MyJump)