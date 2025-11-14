def calculate_product_revenue(product_tuple):
    product_id, category, price, units_sold = product_tuple
    return price * units_sold

def find_top_revenue_product(products):
    
    revenues = [(p[0], calculate_product_revenue(p)) for p in products]

    max_revenue = max(r[1] for r in revenues)

    highest = [r[0] for r in revenues if r[1] == max_revenue]

    return sorted(highest)[0]

def get_products_in_category(products, category_name):
    result = [p[0] for p in products if p[1] == category_name]
    return sorted(result)

def get_category_sales_summary(products):
    category_totals = {}

    for pid, cat, price, sold in products:
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += sold

    return sorted([(cat, total) for cat, total in category_totals.items()])


def analyze_products(products):
    top_product = find_top_revenue_product(products)
    electronics_ids = get_products_in_category(products, "Electronics")
    summary = get_category_sales_summary(products)

    return (top_product, electronics_ids, summary)

products = []
n = int(input(f"how many products  ?: "))

for i in range(n):
    print(f"\nProduct {i+1}:")
    product_id = input(f"enter product ID:   ")
    category = input(f"enter category: ")
    price = float(input(f"enter price: "))
    sold = int(input(f"Enter units solt: "))

    products.append((product_id, category, price, sold))
    
result = analyze_products(products)

print(f"final Result :")
print(result)
