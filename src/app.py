import example as example
import sys

def main():
  if (len(sys.argv) < 2):
    # first argv is the name of this script
    print("You must specify a function: python " + sys.argv[0] + " quad|add")
    sys.exit(1)
  
  if "quad" == sys.argv[1]:
    print("y = ax^2 + bx + c = " + str(example.myFunc(5,1,2,3) ))
  else:
    print("y = x + a + b + c = " + str(example.addAll(5,1,2,3) ))

if __name__ == "__main__":
  main()