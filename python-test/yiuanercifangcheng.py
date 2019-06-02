# twoci fangcheng
import math
def main():
    print("This program find the real solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
#    discRoot = math.sqrt(delta)
    if a == 0:
          root = (-c) /  b
          print("\nThe solution is yiyuan question anwser is :", root)
    elif delta > 0:
          discRoot = math.sqrt(delta)
          root1 = (-b + discRoot) / (2 * a)
          root2 = (-b - discRoot) / (2 * a)
          print("\nThe solutions are: ", root1, root2)
    elif delta == 0:
          discRoot = math.sqrt(delta)
          root = (-b) / (2 * a)
          print("\nThe solution only one is: ", root)
    else:
          print("Not the solution a quadratic.")
main()
