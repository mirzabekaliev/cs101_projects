def build_sales_log(sales_list):
    sales_dict = {}  #empty dictionary

    for entry in sales_list:
        parts = entry.split("|")  # dividing to 3 parts

        if len(parts) != 3:
            continue  # skipping data which has not 3 parts

        emp_id = parts[0]
        price = float(parts[2])  # converting string to float number

        if emp_id in sales_dict:
            sales_dict[emp_id] += price
        else:
            sales_dict[emp_id] = price

    return sales_dict


def find_top_performer(sales_dict):
    top_id = None
    top_amount = 0

    for emp_id, total in sales_dict.items():
        if total > top_amount:
            top_amount = total
            top_id = emp_id

    print("--------------------")
    print(f"Top Performer is {top_id} with ${top_amount:.2f}")

# example input value
sales_list = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]

sales_dict = build_sales_log(sales_list)

print("Sales Report:")
for emp_id, total in sales_dict.items():
    print(f"{emp_id}: ${total:.2f}")

find_top_performer(sales_dict)
