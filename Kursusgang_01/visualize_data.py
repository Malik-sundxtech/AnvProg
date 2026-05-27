import numpy as np
import matplotlib.pyplot as plt
# help(plt.plot)

cigaretter_per_dag = [50, 64, 74, 12, 47, 10, 34, 14, 40, 35, 70, 49, 46, 29, 54, 14, 76, 26, 26, 67]
hospital_besoeg = [6, 6, 14, 5, 8, 5, 5, 3, 10, 5, 9, 5, 8, 4, 13, 5, 12, 8, 10, 11]

plt.plot(cigaretter_per_dag, hospital_besoeg, 'bo', label='Hospital indlæggelsers relation til cigaretter/dag') # bo, go etc. er farven
plt.xlabel("Cigaratter per dag") # Navngivning af akser
plt.ylabel("Hospital besøg")
plt.legend() # Gør at label bliver vist
plt.show() # Viser plotet