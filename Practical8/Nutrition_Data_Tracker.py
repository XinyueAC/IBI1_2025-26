class food_item(object):
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_total_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_car += food.carbs
        total_fat += food.fat

    print("Today's Total Intake:")
    print(f"Total Calories: {total_cal:.1f} kcal")
    print(f"Total Protein: {total_pro:.1f} g")
    print(f"Total Carbohydrates: {total_car:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")

    if total_cal > 2500 or total_fat > 90:
        print("Notice: Excessive calories or fat!")

# Example usage
apple = food_item("apple", 60, 0.3, 15, 0.5)
banana = food_item("banana", 105, 1.3, 27, 0.3)
bread = food_item("bread", 80, 3, 15, 1)
food_list = [apple, banana, bread]
calculate_total_nutrition(food_list)
