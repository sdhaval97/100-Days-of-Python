# Creating a band name generator using city name and pet name

print("Welcome to the Band Name Generator!")

# Asking user for the input

city = input("What city were you born in?\n")

pet = input("What is the name of your pet?\n")

# concatenating city and pet name as the band-name
band_name = city + " " + pet

# printing the name of the band
print(band_name)