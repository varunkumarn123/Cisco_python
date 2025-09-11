def main():
    nums = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in nums.split()]  # accepts int and float


    maximum = max(numbers)
    minimum = min(numbers)

    with open("minmax_data.txt", "w") as file:
        file.write(f"Numbers: {numbers}\n")
        file.write(f"Maximum: {maximum}\n")
        file.write(f"Minimum: {minimum}\n")

    print("\nData saved to minmax_data.txt")
    print("\nReading from file:")
    with open("minmax_data.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
