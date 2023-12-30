import mido

# Get a list of all input port names
names = mido.get_input_names()

# Print each name
for name in names:
    print(name)