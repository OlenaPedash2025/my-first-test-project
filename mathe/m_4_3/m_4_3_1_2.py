from collections import Counter


#Aufgabe M
# 1. Original Data (Raw List / Urliste)
grades = [3, 2, 4, 5, 2, 3, 1, 2, 3, 4, 2, 3, 5, 1, 2]

# Check if the list is not empty before processing
if grades:
    # 2. Creating a Ranked List (Sorting)
    ranked_list = sorted(grades)
    print(f"Ranked List: {ranked_list}")

    # 3. Preparing data for the table
    n = len(grades)  # Total number of grades
    counts = Counter(grades)  # Absolute frequencies

    print(f"\nTotal sample size (n): {n}")
    print(f"{'Grade':<6} | {'Abs. Frequency (ni)':<20} | {'Rel. Frequency (hi)':<20}")
    print("-" * 55)

    # 4. Outputting the Frequency Table
    # We sort the keys (grades 1-5) to display the table in order
    for grade in sorted(counts.keys()):
        abs_f = counts[grade]           # Absolute frequency
        rel_f = abs_f / n               # Relative frequency (decimal)
        rel_f_percent = rel_f * 100     # Percentage
        
        print(f"{grade:<6} | {abs_f:<20} | {rel_f:.2f} ({rel_f_percent:.1f}%)")
else:
    print("The list is empty. No statistical analysis possible.")