print("Welcome to the ASCII Art Creator!")
print("""Choose a roof type:
1. Triangle
2. Flat
3. Rounded""")
roof = input()
if not roof[0] in ['1', '2', '3']:
    print("Invalid choice for roof type. Defaulting to triangle roof.")
    roof = 1
    
print("""Choose a window type:
1. Square
2. Round
3. Closed""")
wind = input()
if not wind[0] in ['1', '2', '3']:
    print("Invalid choice for window type. Defaulting to square window.")
    wind = 1
    
print("""Choose a door type:
1. Wooden
2. Glass
3. Double""")
door = input()
if not door[0] in ['1', '2', '3']:
    print("Invalid choice for door type. Defaulting to wooden door.")
    door = 1
    
roofs = [
"""
         /\\
        /  \\
       /    \\
      /      \\
     /________\\""",
"""

     __________""",
"""
       ______
      (      )
     (________)"""
    ]

winds = [
"""
     |        |
     |  [  ]  |""",
"""
     |        |
     |  (  )  |""",
"""
     |        |
     |  [XX]  |"""]

doors = [
"""
     |   __   |
     |  |  |  |
     |__|__|__|""",
"""
     |        |
     |  [  ]  |
     |__[__]__|""",
"""
     |        |
     | [ ][ ] |
     |_[_][_]_|"""]

print(roofs[int(roof[0]) - 1],end="")
print(winds[int(wind[0]) - 1],end="")
print(doors[int(door[0]) - 1],end="")