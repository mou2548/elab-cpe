def compute_rectangle_area(first_side, second_side):
    return first_side * second_side

def compute_surface_area(width,length,height):
    return width * length * 2 + width * height * 2 + length * height * 2

def compute_volume(width,length,height):
    return width * length * height

width = float(input("Enter width: "))
length = float(input("Enter length: "))
height = float(input("Enter height: "))
print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(width,length,height):.3f}")
print(f"Volume = {compute_volume(width,length,height):.3f}")
print("\nAfter doubling each side,")
print(f"For [{width*2:.2f} x {length*2:.2f} x {height*2:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(width*2,length*2,height*2):.3f}")
print(f"Volume = {compute_volume(width*2,length*2,height*2):.3f}")
