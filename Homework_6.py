import random


class Quest:
    def __init__(self, title, cost, category):
        self.title = title
        self.cost = cost
        self.category = category

    def __repr__(self):
        return f"Quest({self.title}, {self.cost} coins, {self.category})"

    def __str__(self):
        return f"{self.title} (Cost: {self.cost} coins)"

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost


class QuestCategory:
    def __init__(self, category_name, quest_list):
        self.category_name = category_name
        self.quest_list = quest_list

    def __len__(self):
        return len(self.quest_list)

    def __str__(self):
        return f"In '{self.category_name}' category, there are {len(self.quest_list)} quests."

    def __iter__(self):
        return iter(self.quest_list)

    def __getitem__(self, quest_num):
        return self.quest_list[quest_num]

    @staticmethod
    def get_random_quest(all_categories, available_quests):
        available_categories = [
            category
            for category in all_categories
            if any(quest in available_quests for quest in category.quest_list)
        ]
        if not available_categories:
            return None, "No available quests in any category."

        random_category = random.choice(available_categories)
        available_quests_in_category = [
            quest for quest in random_category.quest_list if quest in available_quests
        ]
        random_quest = random.choice(available_quests_in_category)
        return (
            random_quest,
            f"Quest: '{random_quest.title}' (Cost: {random_quest.cost} coins) from '{random_category.category_name}' category.",
        )


class QuestRoom:
    def __init__(self, available_quests, completed_quests, coin_handler):
        self.available_quests = available_quests
        self.completed_quests = completed_quests
        self.coin_handler = coin_handler
        self.total_coins_spent = 0

    def initial_choice(self, categories):
        while True:
            user_choice = (
                input("\nChoose a quest or get one randomly? (Choose/Random): ")
                .strip()
                .lower()
            )
            if user_choice == "random":
                random_quest, quest_message = QuestCategory.get_random_quest(
                    categories, self.available_quests
                )
                if not random_quest:
                    print(quest_message)
                    continue
                print(quest_message)
                self.attempt_quest(random_quest)
                return random_quest
            elif user_choice == "choose":
                chosen_quest = self.choose_quest(categories)
                self.attempt_quest(chosen_quest)
                return chosen_quest
            else:
                print("Invalid input! Enter 'Choose' or 'Random'.")

    def choose_quest(self, categories):
        while True:
            try:
                print("\nAvailable Categories:")
                for i, category in enumerate(categories, start=1):
                    print(f"{i}. {category.category_name}")

                category_choice = int(input("Select a category number: "))
                chosen_category = categories[category_choice - 1]

                available_quests = [
                    quest for quest in chosen_category if quest in self.available_quests
                ]
                if not available_quests:
                    print(
                        f"No quests available in '{chosen_category.category_name}'. Choose another category."
                    )
                    continue

                print(f"\nQuests in '{chosen_category.category_name}':")
                for i, quest in enumerate(available_quests, start=1):
                    print(f"{i}. {quest}")

                quest_choice = int(input("Select a quest number: "))
                return available_quests[quest_choice - 1]
            except (IndexError, ValueError):
                print("Invalid input! Try again.")

    def attempt_quest(self, quest):
        if self.coin_handler.balance >= quest.cost:
            self.coin_handler.deduct_coins(quest.cost)
            self.completed_quests.append(quest)
            self.available_quests.remove(quest)
            self.total_coins_spent += quest.cost
            print(
                f"\nQuest '{quest.title}' completed successfully! Remaining coins: {self.coin_handler.balance}."
            )
        else:
            missing_coins = quest.cost - self.coin_handler.balance
            print(f"Not enough coins! {missing_coins} more needed for '{quest.title}'.")
            if input("Add coins to continue? (Y/N): ").strip().upper() == "Y":
                self.coin_handler.add_coins()
                self.attempt_quest(quest)
            else:
                print(f"Quest '{quest.title}' failed. Missing coins: {missing_coins}.")

    def show_progress(self):
        if self.completed_quests:
            cheapest_quest = min(self.completed_quests)
            most_expensive_quest = max(self.completed_quests)
            return (
                f"Completed quests: {[quest.title for quest in self.completed_quests]}.\n"
                f"Cheapest: {cheapest_quest}. \nMost expensive: {most_expensive_quest}.\n"
                f"Remaining coins: {self.coin_handler.balance}."
            )
        return f"No quests completed yet. Coins left: {self.coin_handler.balance}."

    def confirm_continue(self):
        if not self.available_quests:
            print("All quests completed! Thank you for playing!")
            return False
        while True:
            continue_flag = input("\nDo another quest? (Y/N): ").strip().upper()
            if continue_flag == "Y":
                return True
            elif continue_flag == "N":
                print("Game Over!")
                print(
                    f"Completed quests: {[quest.title for quest in self.completed_quests]}"
                )
                print(f"Total coins spent: {self.total_coins_spent}.")
                return False
            else:
                print("Invalid input! Enter 'Y' or 'N'.")

    def start_game(self, categories):
        print("Welcome to the Random Quest Generator!\n")
        while True:
            self.initial_choice(categories)
            print(self.show_progress())
            if not self.confirm_continue():
                break


class CoinHandler:
    def __init__(self, balance):
        self.balance = balance

    def add_coins(self):
        while True:
            try:
                amount = int(input("How many coins to add? (0 to cancel): "))
                if amount > 0:
                    self.balance += amount
                    print(f"Added {amount} coins. New balance: {self.balance}.")
                    break
                elif amount == 0:
                    print("No coins added.")
                    break
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Invalid input! Enter a number.")

    def deduct_coins(self, cost):
        self.balance -= cost


# Setup and Start Game
adventure_quests = [
    Quest("Explore a park", 2, "Adventure"),
    Quest("Go to a new cafe", 1, "Adventure"),
    Quest("Travel to a new country", 4, "Adventure"),
]

fitness_quests = [
    Quest("Workout for an hour", 3, "Fitness"),
    Quest("Do as many push-ups as you can", 4, "Fitness"),
    Quest("Go for a 30-minute walk", 2, "Fitness"),
    Quest("Swim in the pool", 2, "Fitness"),
]

skill_quests = [
    Quest("Cook a new dish", 3, "Skill"),
    Quest("Start learning a new language", 5, "Skill"),
    Quest("Learn something new online", 3, "Skill"),
    Quest("Practice Python", 4, "Skill"),
    Quest("Read a book about Django", 5, "Skill"),
]

categories = [
    QuestCategory("Adventure", adventure_quests),
    QuestCategory("Fitness", fitness_quests),
    QuestCategory("Skill", skill_quests),
]

coin_handler = CoinHandler(balance=10)
quest_room = QuestRoom(
    available_quests=adventure_quests + fitness_quests + skill_quests,
    completed_quests=[],
    coin_handler=coin_handler,
)

quest_room.start_game(categories)
