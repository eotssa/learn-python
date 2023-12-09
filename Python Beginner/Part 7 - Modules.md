# **Debugging Methods in Python**

## **Recap of Debugging Methods**
- **Visualization tools** and **debugging print outs** are common methods.
- **Visual Studio Code built-in debugger** is an effective tool. Problems with file location are covered in the previous section.

## **Introduction to Breakpoint Command**
- Python version 3.7 introduced the **breakpoint() command** for debugging.
- The command halts the program execution at the point where it is inserted.
- An **interactive console** opens upon halting, enabling the user to experiment with the code.

## **Use Cases and Instructions**
- The command is useful in identifying the cause of an error in a particular line.
- Execution can be resumed using the command **continue**, or **c**, in the debugging console.
- Other commands for the console can be found through the **help** command.
- The **exit** command concludes the program execution.
- Users must remember to remove **breakpoint** commands after debugging.

# **Python Modules**

## **Introduction to Modules**
- Python's language definition includes useful functions, but more complex programs often require additional functionalities provided by the **Python standard library**.
- The standard library consists of **modules**, each containing functions and classes around different themes.
- The **import** command allows the use of a given module's contents in the current program.

## **Using the Math Module**
- The **math module** provides functions for mathematical operations.
- Functions in a module are referred to by prefixing them with the module name (e.g., math.sqrt).

## **Importing Specific Module Sections**
- Select parts of a module can be imported using the **from** command, which eliminates the need for prefixing.
- The **star notation** imports all contents of a module.
- The star notation can be handy in testing and small projects but may also pose problems.

## **Programming Exercises**
- An exercise on calculating the **hypotenuse** of a triangle using the **math module**.
- Another exercise on separating different character types using the **string module**.
- A third exercise on creating fractions using the **fractions module**.

## **Understanding Module Contents**
- Python documentation provides detailed resources on each module.
- The **dir function** lists all names defined by a module.
- The names can represent classes, constant values, or functions.