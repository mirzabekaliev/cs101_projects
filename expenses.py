def calculate_total(filename):
    total_spent = 0.0
    item_count = 0

    with open(filename, "r") as file:
        for line in file:
            try:
                amount = float(line.strip())
                total_spent += amount
                item_count += 1
            except ValueError:
                print("Skipping invalid line")

    print("---------------------")
    print(f"Total Items: {item_count}")
    print(f"Total Spent: ${total_spent:.2f}")


calculate_total("expenses.txt")
