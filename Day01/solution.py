f = open("input.txt")

number = 50
password1 = 0
password2 = 0 

for line in f:
    line = line.strip()
    instruction = int(line[1:])
    
    start_pos = number
    
    if line.startswith("L"):
        number -= instruction
    elif line.startswith("R"):
        number += instruction

    end_pos = ((number % 100) + 100) % 100
    
    if end_pos == 0:
        password1 += 1
    
    current = start_pos
    for _ in range(instruction):
        if line.startswith("L"):
            current -= 1
        else:  # R
            current += 1
        
        current = ((current % 100) + 100) % 100
        
        if current == 0:
            password2 += 1
    
    number = end_pos

print("Part 1: ", password1)
print("Part 2: ", password2)