# Function to print a pyramid of stars
def draw_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)   # Create leading spaces
        stars = "*" * (2 * i - 1)   # Create stars for the row
        print(spaces + stars)

# Set the number of rows for the pyramid
rows = int(input("Enter the number of rows: "))
draw_pyramid(rows)
