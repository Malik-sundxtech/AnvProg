import matplotlib.pyplot as plt

path = "/home/Malik/Documents/Sundhedsteknologi/2. sem/Anvendt programmering/all_lectures/oop_3/files/data_1_rows.csv" # Gemmer en filtype
data = [] # Laver en tomliste, hvor data kan gemmes ind i
with open(path, "r") as f: # r = read. Default mode er read mode
    readFile = f.readline().strip() # Det er to funktioner der anvendes
    header = f.readline().strip() # Her læses titlen af filen
    
    for line in f:
        data.append(float(line.strip()))
n = 10 # KAN LAVE EN SLICE I STEDET FOR, slices er tommepladser implicit 0 og maks
# print(data[:10])

print(f"i {header=}Der er {len(data)} antal data")
print(f"De første {n} rækker")


for i, row in enumerate(data):
    if i > n:
        break # Hvorfor skal der bruges break her, man kan ikke lave en for i < n
    print(f"{i}: {row:.3f}")

plt.plot(data) # Plotter dataen
plt.show() # Viser dataen