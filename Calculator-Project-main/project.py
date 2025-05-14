def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

def exponent(n1,n2):
  return n1 ** n2

def modulus(n1,n2):
  return n1 % n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  "**" : exponent,
  "%" : modulus,
}

def find_operation(operation = input("Which Operation? ")):
    for key in operations:
        if key == operation:
            return True, operation
    return False, 0 #placeholder for no operation
   
def main():
    print("Welcome To Calculator")
    n1 = float(input("First Number: "))

    print("Operations:")
    for key in operations:
        print(key)

    should_continue = True

    while should_continue:
        operation_found = False

        while not operation_found:
           operation_found, operation = find_operation()
            
        n2 = float(input("Second Number: "))
        
        function = operations[operation]
        output = function (n1,n2)
        print(f"{n1} {operation} {n2} = {output}")

        wants_continue = input(f"To continue with {output}, type Yes. To calculate with a new number, type No. Type anything else to exit\n")
        if wants_continue.lower() in ["y", "yes"]:
            n1 = output
        elif wants_continue.lower() in ["n","no"]:
            n1 = float(input("First Number: "))  
        else:
            should_continue = False

if __name__ == "__main__":
   main()