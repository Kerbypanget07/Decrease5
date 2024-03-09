def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    smaller = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr[1:] if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(smaller) + [pivot] + equal + quick_sort(greater)

def main():
    user_choice = input("Enter 'L' for letters or 'N' for numbers: ").upper()
    
    if user_choice == 'L':
        user_input = input("Enter the list of characters: ").upper().replace(" ", "")
        sorted_chars = quick_sort(list(user_input))
        sorted_str = ''.join(sorted_chars)
        print("Sorted List:", sorted_str)
    elif user_choice == 'N':
        input_option = input("Enter 'S' if the numbers are separated by spaces or 'W' if they are without spaces: ").upper()
        if input_option == 'S':
            user_input = input("Enter the list of numbers separated by spaces: ")
            numbers = [int(x) for x in user_input.split()]
        elif input_option == 'W':
            user_input = input("Enter the list of numbers without spaces: ")
            numbers = [int(x) for x in user_input]
        else:
            print("Invalid input option. Please enter 'S' or 'W'.")
            return
        sorted_numbers = quick_sort(numbers)
        print("Sorted Numbers:", sorted_numbers)
    else:
        print("Invalid choice. Please enter 'L' for letters or 'N' for numbers.")

if __name__ == "__main__":
    main()
