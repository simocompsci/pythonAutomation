def smolov_jr_program(weight, height, max_bench):
    print("\n===== SMOLOV JR BENCH PROGRAM (3 WEEKS) =====\n")

    # Percentages
    base_days = [
        ("Day 1 (6x6)", 0.70),
        ("Day 2 (7x5)", 0.75),
        ("Day 3 (8x4)", 0.80),
        ("Day 4 (10x3)", 0.85)
    ]

    # Weekly increments (you can adjust)
    weekly_increase = [0, 2.5, 5]  # kg added each week

    for week in range(1, 4):
        print(f"--- WEEK {week} ---")

        for day, percent in base_days:
            base_weight = max_bench * percent
            adjusted_weight = base_weight + weekly_increase[week - 1]

            print(f"{day}: {round(adjusted_weight, 1)} kg "
                  f"({int(percent*100)}% of max + {weekly_increase[week - 1]} kg)")

        print()

    print("============================================")
    print(f"Weight: {weight} kg | Height: {height} cm | Max Bench: {max_bench} kg")
    print("Rest well, eat enough, and don't skip warm-ups!\n")


# ---- USER INPUT ----
try:
    weight = float(input("Enter your body weight (kg): "))
    height = float(input("Enter your height (cm): "))
    max_bench = float(input("Enter your max bench press (kg): "))

    smolov_jr_program(weight, height, max_bench)

except ValueError:
    print("Please enter valid numbers.")