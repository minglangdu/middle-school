name = "Ada"
message = "This is a long message"
age = "30"
z = 123.34567

print(f"My name is {name} and I'm {age} years old. ")
# < aligns left, > aligns right
print(f"{name:<5}{age:>10}")
# f says how many decimal places
# e is how many places in scientific notation
# g is how many places in general
print(f"{z:.2f}\n{z:.4e}\n{z:.3g}")
# truncation
print(f"{message:.10}")

# expressions can also be used

def greet(name):
    return f"Hello {name}!"

print(f"{greet(name)} You are {int(age) * 2} in dog years. ")