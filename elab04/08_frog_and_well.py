depth = int(input("What is the well's depth? "))
jump = int(input("Enter the height the frog can jump up: "))
slip = int(input("Enter the height the frog slips down: "))
now = 0

if jump == slip and jump != depth:
    print("The frog is always stuck in the well.")
else:
    day = 1
    while now + jump < depth:
        now += jump
        print(f"On day {day} the frog leaps to the depth of {depth-now} meters.")
        now -= slip
        print(f"At night he slips down to the depth of {depth-now} meters.")
        day += 1
    print(f"The frog can escape the well on day {day}.")
        
