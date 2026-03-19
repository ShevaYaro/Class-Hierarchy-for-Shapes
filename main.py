from circle import Circle
from rectangle import Rectangle
from square import Square

def main():
    # Circle parameters: x, y, radius, name
    c1 = Circle(0, 0, 4, "Circle_1")
    c2 = Circle(0, 0, 9, "Circle_2")
    
    # Rectangle parameters: length, width, name
    r1 = Rectangle(10, 20, "Rectangle_1")
    r2 = Rectangle(20, 30, "Rectangle_2")
    
    # Square parameters: side, name
    s1 = Square(10, "Square")

    # 2. Put them all in a single list
    shapes = [c1, c2, r1, r2, s1]

    # 3. Polymorphism Check!
    print("--- Polymorphism check ---")
    for shape in shapes:
        if isinstance(shape, Circle):
            print(f"{shape.name} Area = {shape.area:.5f}")
        else:
            print(f"{shape.name} Area = {shape.area}")

    print("\n--- Getter/setter check ---")
    
    # 4. Circle update check
    print(f"{c1.name} Current:  {c1.radius} {c1.area:.5f}")

    c1.radius = 8

    print(f"{c1.name} Doubled:  {c1.radius} {c1.area:.5f}")

    # 5. Rectangle update check
    print(f"{r1.name} Current:  {r1.length} {r1.width} {r1.area}")
    r1.length = 20
    r1.width = 40
    print(f"{r1.name} Doubled:  {r1.length} {r1.width} {r1.area}")

    # 6. Square update check
    print(f"{s1.name} Current:  {s1.side} {s1.area}")
    s1.side = 20
    print(f"{s1.name} Doubled:  {s1.side} {s1.area}")

if __name__ == "__main__":
    main()