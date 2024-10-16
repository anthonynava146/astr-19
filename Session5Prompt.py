import numpy as np

def PrintTable():
    # Define the range of x between 0 and 2π, with 1000 entries
    xValues = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sin(x) values for each x
    sinValues = np.sin(xValues)
    
    # Print the header of the table
    print("x", end =" ")

    for i in range(7):
        print(" ", end =" ")

    print("sin(x)")

    for i in range(30):
        print("-", end =" ")

    print("\n")

    # Print the x and sin(x) values in an organized table format
    for x, sin_x in zip(xValues, sinValues):
        print(f"{x:1.8f}", end =" ")
        print("       ", end =" ")
        print(f"{sin_x:1.8f}")

def main():
    # Call the function to generate and print the sin table
    PrintTable()

# Run the program
if __name__ == "__main__":
    main()