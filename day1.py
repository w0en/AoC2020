
input_text = open("input1.txt", "r")
inputs = []
for line in input_text:
    inputs.append(int(line))
input_text.close()
print(inputs)
for i in range(len(inputs)):
    for j in range(i, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            print(str(inputs[i]) + " * " + str(inputs[j]) + " = " + str(inputs[i] * inputs[j]))
            break