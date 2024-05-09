# Dmitrii Gusev
from shapecalc import shapes

if __name__ == '__main__':

    circle_1 = shapes.Circle()
    circle_1.set_x(float(input("Enter the radius of the circle 1: ")))
    print(f"Circle 1 with radius {circle_1.x} has area {round(circle_1.area(), 2)}\n\n")

    circle_2 = shapes.Circle()
    circle_2.set_x(float(input("Enter the radius of the circle 2: ")))
    print(f"Circle 2 with radius {circle_2.x} has area {round(circle_2.area(), 2)}\n\n")

    rectangle = shapes.Rectangle()
    rectangle.set_x(float(input("Enter the first side of the rectangle: ")))
    rectangle.set_y(float(input("Enter the second side of the rectangle: ")))
    print(
        f"Rectangle with first side {rectangle.x} and second side {rectangle.y} "
        f"has area {round(rectangle.area(), 2)}\n\n")

    triangle = shapes.Triangle()
    triangle.set_x(float(input("Enter the base of the triangle: ")))
    triangle.set_y(float(input("Enter the height of the triangle: ")))
    print(f"Triangle with base {triangle.x} and height {triangle.y} has area {round(triangle.area(), 2)}\n\n")

    trapezoid = shapes.Trapezoid()
    trapezoid.set_x(float(input("Enter the lower base of the trapezoid: ")))
    trapezoid.set_y(float(input("Enter the higher base of the trapezoid: ")))
    trapezoid.set_z(float(input("Enter the height of the trapezoid: ")))
    print(f"Trapezoid with lower base {trapezoid.x} and lower base {trapezoid.y}"
          f" and height {trapezoid.z} has area {round(trapezoid.area(), 2)}")
