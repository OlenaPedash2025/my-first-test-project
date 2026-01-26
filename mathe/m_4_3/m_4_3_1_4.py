'''Programmier-Aufgabe (Python/Shell): Analysiert eine einfache Log-Datei, zählt die Häufigkeit verschiedener Fehlermeldungen (z.B. "ERROR", "WARNING", "INFO") und gebt eine Zusammenfassung aus.'''


from collections import Counter

file_path = "tools/log.txt"
try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines: list[str] = f.readlines()
    log_levels = [line.split()[2] for line in lines if len(line.split()) > 2]
    line_counts = Counter(log_levels)
    print("Häufigkeit:")
    for level, count in line_counts.items():
        print(f"{level}: {count}")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")



'''Code Review
from collections import Counter
from pathlib import Path

def count_log_levels(file_path: str):
    # Используем Path для удобной работы с путями
    path = Path(file_path)
    
    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        return

    counter = Counter()

    try:
        # Открываем файл. Контекстный менеджер 'with' закроет его автоматически
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                # Проверяем, что в строке достаточно данных (минимум дата, время, уровень)
                if len(parts) >= 3:
                    level = parts[2]
                    counter[level] += 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Вывод результата
    print("Häufigkeit:")
    # .most_common() сортирует результат от большего к меньшему
    for level, count in counter.most_common():
        print(f"{level:<8}: {count}")

if __name__ == "__main__":
    count_log_levels("tools/log.txt")

'''

