import random
import matplotlib.pyplot as plt
from collections import Counter


rolls_count = 30

def roll_dice(rolls_count):
    urliste = []
    for _ in range(rolls_count):
        roll = random.randint(1, 6)
        urliste.append(roll)
    return urliste

def count_frequencies(urliste):
    frequency_table = {}
    for item in urliste:
        if item in frequency_table:
            frequency_table[item] += 1
        else:
            frequency_table[item] = 1
    return frequency_table



rolls = roll_dice(rolls_count)
frequencies = count_frequencies(rolls)
print(frequencies)

plt.bar(frequencies.keys(), frequencies.values())
plt.savefig("m_4_3_1_3.png")