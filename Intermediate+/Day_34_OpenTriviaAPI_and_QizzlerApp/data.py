import requests

def no_of_questions() -> int:
    amount = int(input("How many questions do you want? (1 to 50): "))
    try:
        if 1 <= amount <= 50:
            return amount
        else:
            print("Enter a valid amount!!")
            no_of_questions()
    except ValueError:
        print("Invalid input! Please input numeric value!")
        no_of_questions()

def select_id() -> int:
    categories = {
        9: "General Knowledge",
        10: "Entertainment: Books",
        11: "Entertainment: Film",
        12: "Entertainment: Music",
        13: "Entertainment: Musicals & Theatres",
        14: "Entertainment: Television",
        15: "Entertainment: Video Games",
        16: "Entertainment: Board Games",
        17: "Science & Nature",
        18: "Science: Computers",
        19: "Science: Mathematics",
        20: "Mythology",
        21: "Sports",
        22: "Geography",
        23: "History",
        24: "Politics",
        25: "Art",
        26: "Celebrities",
        27: "Animals",
        28: "Vehicles",
        29: "Entertainment: Comics",
        30: "Science: Gadgets",
        31: "Entertainment: Japanese Anime & Manga",
        32: "Entertainment: Cartoon & Animations"
    }

    print("What category do you want?")
    for key in categories:
        print(f"category id: {key} | category name: {categories[key]}")

    category_id = int(input("Choose from the above id: "))

    try:
        if 1 <= category_id <= 50:
            return category_id
        else:
            print("Enter a valid amount!!")
            select_id()
    except ValueError:
        print("Invalid input! Please input numeric value!")
        select_id()

def select_difficulty() -> str:
    diff = ['easy', 'medium', 'hard']
    print(f"The difficulty levels are: {diff[0]}. {diff[1]}, {diff[2]}")
    user_diff = input("Select one from above: ").lower()

    try:
        if user_diff in diff:
            return user_diff
        else:
            print("Choose a valid difficulty!")
    except ValueError:
        print("Invalid input! Please enter text!")
    

parameters = {"amount": no_of_questions(),
              "category": select_id(),
              "difficulty": select_difficulty(),
              "type": "boolean"}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()['results']


