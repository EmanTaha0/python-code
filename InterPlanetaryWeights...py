# --------------------------------------------------------------
# Program: Inter Planetary Weights
# Course: CIT-115/115L Python
# Professor: Brian Candido
# Student: [Eman Taha]
# Description:
#   This program calculates a person's weight on various planets
#   in our solar system using each planet's surface gravity factor.
# --------------------------------------------------------------

# 1. Declare Named Constants for Surface Gravity Factors
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

# 2. Prompt the user for their name and Earth weight
sName = input("What is your name: ")
fEarthWeight = float(input("What is your weight: "))

# 3. Perform calculations for each planet
fMercuryWeight = fEarthWeight * MERCURY_GRAVITY
fVenusWeight = fEarthWeight * VENUS_GRAVITY
fMoonWeight = fEarthWeight * MOON_GRAVITY
fMarsWeight = fEarthWeight * MARS_GRAVITY
fJupiterWeight = fEarthWeight * JUPITER_GRAVITY
fSaturnWeight = fEarthWeight * SATURN_GRAVITY
fUranusWeight = fEarthWeight * URANUS_GRAVITY
fNeptuneWeight = fEarthWeight * NEPTUNE_GRAVITY
fPlutoWeight = fEarthWeight * PLUTO_GRAVITY

# 4. Display formatted output exactly like the sample
print()
print(sName+" here are your weights on our Solar System's planets:")
print("Weight on Mercury:", format (fMercuryWeight,"10.2f"))
print("Weight on Venus: ",  format (fVenusWeight,"10.2f"))
print("Weight on Our Moon:",format (fMoonWeight,"10.2f"))
print("Weight on Mars:",format (fMarsWeight,"10.2f"))
print("Weight on Jupiter:", format (fJupiterWeight,"10.2f"))
print("Weight on Saturn:",format  (fSaturnWeight,"10.2f"))
print("Weight on Uranus:", format (fUranusWeight,"10.2f"))
print("Weight on Neptune:",format (fNeptuneWeight,"10.2f"))
print("Weight on Pluto:", format  (fPlutoWeight,"10.2f"))

# 5. End of Program
