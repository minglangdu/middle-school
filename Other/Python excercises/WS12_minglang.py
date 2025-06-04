# Minglang Du 6-B1
# Worksheet #12
# 5/4/2023

def arclength(rad, ang):
    import math
    circ = math.pi * rad * 2
    angle = ang / 360
    return circ * angle

print("Arc length:", arclength(5, 36))

def arcarea(rad, ang):
    import math
    circ = math.pi * rad ** 2
    angle = ang / 360
    return circ * angle

print("Arc area:", arcarea(5, 36))

def midpoint(x1, x2, y1, y2):
    sumx = x1 + x2
    sumy = y1 + y2
    x = round(sumx / 2)
    y = round(sumy / 2)
    print(f"The midpoint of ({x1}, {y1}) and ({x2}, {y2}) is ({x:.1f}, {y:.1f}).")

midpoint(2, 4, 7, 11)