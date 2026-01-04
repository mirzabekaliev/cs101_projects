import requests

BASE_URL = "https://api.chucknorris.io/jokes"


def get_random_joke():
    try:
        response = requests.get(f"{BASE_URL}/random", timeout=10)
        response.raise_for_status()
        return response.json()["value"]
    except requests.exceptions.RequestException:
        print("Failed to fetch a random joke.")
        return None


def get_categories():
    try:
        response = requests.get(f"{BASE_URL}/categories", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Failed to load categories.")
        return []


def get_joke_by_category(category):
    try:
        response = requests.get(f"{BASE_URL}/random?category={category}", timeout=10)
        response.raise_for_status()
        return response.json()["value"]
    except requests.exceptions.RequestException:
        print("Invalid category or API error.")
        return None


def search_jokes(keyword):
    try:
        response = requests.get(f"{BASE_URL}/search?query={keyword}", timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["total"], [joke["value"] for joke in data["result"]]
    except requests.exceptions.RequestException:
        print("Search failed.")
        return 0, []


def save_to_file(content):
    with open("chuck_norris_results.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("Results saved to chuck_norris_results.txt")


def main():
    print("Welcome to Chuck Norris Joke Explorer")
    print("1. Random Joke")
    print("2. Joke by Category")
    print("3. Search Jokes by Keyword")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        joke = get_random_joke()
        if joke:
            print("\n Random Joke:")
            print(joke)
            save_to_file(joke)

    elif choice == "2":
        categories = get_categories()
        if not categories:
            return

        print("\nAvailable Categories:")
        for cat in categories:
            print(f"- {cat}")

        selected = input("Enter a category: ").lower()
        if selected not in categories:
            print(" Invalid category selected.")
            return

        joke = get_joke_by_category(selected)
        if joke:
            print(f"\n Joke from '{selected}' category:")
            print(joke)
            save_to_file(joke)

    elif choice == "3":
        keyword = input("Enter a keyword to search: ").strip()
        if not keyword:
            print(" Keyword cannot be empty.")
            return

        total, jokes = search_jokes(keyword)
        if total == 0:
            print(" No jokes found.")
            return

        print(f"\n🔍 Found {total} jokes. Showing first 3:\n")
        output = f"Search keyword: {keyword}\nTotal jokes found: {total}\n\n"

        for i, joke in enumerate(jokes[:3], start=1):
            print(f"{i}. {joke}\n")
            output += f"{i}. {joke}\n\n"

        save_to_file(output)

    else:
        print(" Invalid menu option.")


if __name__ == "__main__":
    main()
