def draw_square_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")  # Print asterisks without a newline
        print()  # Move to the next line after each row
        row += 1


def main():
    # Ask the user for input until a valid positive integer is provided
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    draw_square_pattern(size)


if __name__ == "__main__":
    main()
