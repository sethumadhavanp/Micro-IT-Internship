# Python Calculator
    
## Description:
A python calculator that runs within the terminal. There are a variety of operations to choose from: add, subtract, multiply, divide, modulus (calculate remainder), and exponent (to work out a power of a number). 
    
Upon running the program, the user is greeted and is prompted to enter the first number. Then, a list of supported operations is displayed and the find_operation() function is called. This function will determine if the input is valid and return both the validity of the input (True / False) and the input itself. If False is returned, the value will be marked as 0 - as a placeholder. This function will repeatedly be called until the input is valid.

Next, the user is prompted for a second number, and applies the calculation to the first number.

An interesting design choice I decided to make, was the ability to continue calculating with the same number if the user chooses so. The program asks the user if they want to calculate with the same number, start with a new number, or exit the program. I find this very interesting as despite the logic being simple, it adds a whole new layer to the user experience. Should the user choose this, the output is stored and used as the new first number. The process repeats until the user opts to quit, escaping the while loop.

## Screenschot:
![Calculator](https://github.com/sethumadhavanp/Micro-IT-Internship/blob/main/Calculator-Project-main/Screenshot/Testcase1.png)
