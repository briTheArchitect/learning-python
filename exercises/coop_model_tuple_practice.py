"""
Purpose: to practice tuples and understand their function and limitations.
Tuples are immutable: tuple elements cannot be added, removed, or changed.
"""


# Fixed, immutable coop dimensions (width, length, height) in feet
coop_dimensions = (12, 20, 11)
# unpacking tuple
width, length, height = coop_dimensions

# Fixed livestock population
livestock_pop = (24, 2)
# unpacking tuple
chickens, geese = livestock_pop

print(f"Width: {width}ft | Length: {length}ft | Height: {height}ft")

coop_area = width * length
coop_volume = coop_area * height

total_animals = chickens + geese

print(f"Coop Area: {coop_area} sq ft")
print(f"Coop Volume: {coop_volume} cu ft")

print(f"Total animals: {total_animals}")

# The following line of code would throw an error, due to the immutability of tuples
# del livestock_pop[1] 