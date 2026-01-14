
def mp_neuron(inputs, weights, threshold):
    total = 0

    for x, w in zip(inputs, weights):
        total += x * w

    if total >= threshold:
        return 1
    else:
        return 0

print("Choose a Logic Gate")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. NAND")
print("5. NOR")

choice = int(input("Enter your choice: "))

if choice == 3:   
    x = int(input("Enter input (0 or 1): "))
    inputs = [x]
else:
    x1 = int(input("Enter X1 (0 or 1): "))
    x2 = int(input("Enter X2 (0 or 1): "))
    inputs = [x1, x2]


if choice == 1:       
    weights = [1, 1]
    threshold = 2

elif choice == 2:    
    weights = [1, 1]
    threshold = 1

elif choice == 3:     
    weights = [-1]
    threshold = 0

elif choice == 4:      
    weights = [-1, -1]
    threshold = -1

elif choice == 5: 
    weights = [-1, -1]
    threshold = 0

else:
    print("Invalid choice")
    exit()

output = mp_neuron(inputs, weights, threshold)
print("Output:", output)
