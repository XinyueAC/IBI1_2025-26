def calculate_protein_mass(sequence):
    """
    计算氨基酸序列的总质量。
    
    Args:
        sequence (str): 氨基酸序列字符串
    
    Returns:
        float: 总质量 (amu)，如果序列包含无效氨基酸则返回 None
    """
    # 1. 定义氨基酸质量字典 (Residue Mass Table)
    amino_acid_mass = {
        'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04,
        'F': 147.07, 'G': 57.02, 'H': 137.06, 'I': 113.08,
        'K': 128.09, 'L': 113.08, 'M': 131.04, 'N': 114.04,
        'P': 97.05, 'Q': 128.06, 'R': 156.10, 'S': 87.03,
        'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06
        # 注意：表中 Serine 是 s，这里统一用大写 S
    }
    
    total_mass = 0.0
    
    # 2. 遍历序列进行计算和检查
    for aa in sequence.upper(): # 转大写以防止输入小写
        if aa not in amino_acid_mass:
            print(f"Error: 氨基酸 '{aa}' 没有记录的质量或未定义。")
            return None # 遇到错误立即返回 (Return vs Print)
        total_mass += amino_acid_mass[aa]
    
    return total_mass

# 3. 文档要求的示例调用
print("=== 蛋白质质量预测示例 ===")
example_seq = "ACGT" # Alanine, Cysteine, Glycine, Threonine
mass = calculate_protein_mass(example_seq)
if mass is not None:
    print(f"序列 {example_seq} 的质量为: {mass:.2f} amu")


class food_item:
    """
    表示一种食物及其营养成分的类。
    """
    def __init__(self, name, calories, protein, carbs, fat):
        """
        初始化食物对象。
        
        Args:
            name (str): 食物名称
            calories (float): 卡路里
            protein (float): 蛋白质含量 (g)
            carbs (float): 碳水化合物含量 (g)
            fat (float): 脂肪含量 (g)
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def track_nutrition(food_list):
    """
    计算并报告24小时内摄入的营养总量。
    
    Args:
        food_list (list): food_item 对象的列表
    """
    # 1. 初始化计数器
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    # 2. 遍历食物列表累加
    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat
    
    # 3. 打印结果
    print("\n=== 24小时营养追踪报告 ===")
    print(f"总卡路里: {total_calories:.1f} kcal")
    print(f"总蛋白质: {total_protein:.1f} g")
    print(f"总碳水: {total_carbs:.1f} g")
    print(f"总脂肪: {total_fat:.1f} g")
    
    # 4. 警告逻辑 (根据文档要求)
    if total_calories > 2500:
        print("⚠ 警告: 卡路里摄入超过 2,500!")
    if total_fat > 90:
        print("⚠ 警告: 脂肪摄入超过 90g!")
    if total_calories <= 2500 and total_fat <= 90:
        print("摄入量在建议范围内。")

# 5. 文档要求的示例调用
print("\n=== 营养追踪器示例 ===")
# 创建示例食物对象 (模拟文档中的例子: 苹果)
apple = food_item("Apple", 60, 0.3, 15, 0.5)
# 再加几个食物凑成一餐
burger = food_item("Burger", 800, 30, 40, 50)
salad = food_item("Salad", 200, 10, 15, 10)

# 创建食物列表
my_meal = [apple, burger, salad]

# 调用函数
track_nutrition(my_meal)