from openpyxl import load_workbook
from matplotlib import pyplot as plt

# load data
load_wb = load_workbook("earthquakes.xlsx", data_only=True)
load_ws = load_wb["Sheet1"]


def getValue(loc: str):
    return load_ws[loc].value


# analyze data
x_values = []
y_values = []
i = 1
while True:
    # depth: 깊이
    # intensity: 진도
    # magnitude: 규모
    depth = getValue(f"D{i}")
    intensity_char = getValue(f"E{i}")
    magnitude = getValue(f"C{i}")

    # roman number to int
    intensity = -1
    if intensity_char == "Ⅰ":
        intensity = 1
    elif intensity_char == "Ⅱ":
        intensity = 2
    elif intensity_char == "Ⅲ":
        intensity = 3
    elif intensity_char == "Ⅳ":
        intensity = 4
    elif intensity_char == "Ⅴ":
        intensity = 5

    if depth == None:
        break
    if depth != "-" and magnitude != "-" and intensity != -1:
        # append to x_values, y_values
        x_values.append(magnitude / depth)
        y_values.append(intensity)

    i += 1

print(len(x_values))

# show plot
plt.scatter(x_values, y_values)
# set x, y label
plt.xlabel("magnitude/depth")
plt.ylabel("intensity")
plt.title("intensity - magnitude/depth")
plt.savefig("intensity-magnitude_per_depth.png")
plt.show()
