import csv

from matplotlib import pyplot as plt

f = open(r"C:\Users\cdh88\Documents\programming\python\earth\japan\output.csv", "r")
rdr = csv.reader(f)

depths = []
intensities = []
magnitudes = []

depths2 = []
intensities2 = []
magnitudes2 = []
for line in rdr:
    try:
        depth = int(line[0])
        intensity_str = line[1]
        magnitude = float(line[2])

        intensity = -1
        if intensity_str == "-":
            raise ValueError
        if intensity_str.endswith("+"):
            intensity = int(intensity_str[: len(intensity_str) - 1]) + 0.5
        elif intensity_str.endswith("-"):
            intensity = int(intensity_str[: len(intensity_str) - 1]) - 0.5
        else:
            intensity = int(intensity_str)
        if depth > 70:
            depths2.append(depth)
            intensities2.append(intensity)
            magnitudes2.append(magnitude)
            raise ValueError

        depths.append(depth)
        intensities.append(intensity)
        magnitudes.append(magnitude)
        print(line)
    except:
        continue

# show plot
plt.scatter(depths, intensities)
plt.scatter(depths2, intensities2, color="red")
# set x, y label
plt.xlabel("depth")
plt.ylabel("seismic intensity")
plt.title("seismic intensity - depth (japan)")
plt.show()

f.close()
