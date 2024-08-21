estimate = int(input("Estimated time : "))
weeks = estimate//8
physical, weight, fitness = 0, 0, 0
minimum = estimate*2.5
for i in range(weeks):
    print(f"Week{i+1}")
    physical += int(input("Physical therapy : "))
    weight += int(input("Weight training : "))
    fitness += int(input("Fitness training : "))

if physical >= minimum and weight >= minimum and fitness >= minimum:
    print("Buzzy has recovered in time.")
else:
    print("Buzzy has not recovered in time.")
