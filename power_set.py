# Power Set Generator Application

def generate_power_set(input_set):
    """Generates the power set of a given input set."""
    power_set = [[]]  # Start with the empty set
    for element in input_set:
        # For each element, add it to all existing subsets
        new_subsets = [subset + [element] for subset in power_set]
        power_set.extend(new_subsets)
    return power_set

def display_power_set(power_set):
    """Displays the power set."""
    print("\nPower Set:")
    for subset in power_set:
        print(subset)

def main():
    print("=== Power Set Generator ===")
    user_input = input("Enter elements of the set separated by spaces: ")
    input_set = user_input.split()  # Split the input into a list

    power_set = generate_power_set(input_set)
    display_power_set(power_set)

if __name__ == "__main__":
    main()
