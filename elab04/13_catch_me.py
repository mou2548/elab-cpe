police = 0
criminal = 100
i = 1
while police < criminal:
    criminal += 2 ** i
    police += int(input("Input distance: "))
    print(f"Police distance: {police}")
    print(f"Criminal distance: {criminal}")
    i += 1
print("Caught him!")
