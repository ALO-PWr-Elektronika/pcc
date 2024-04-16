# Pearson's Correlation Coeffcient
# pip install scipy
from scipy.stats import pearsonr


# from collections import Counter
# counter = dict(Counter(input_string))


def count_letters(in_str):
    counter = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for letter in in_str:
        if letter in counter:
            counter[letter] += 1
        else:
            print(f"Letter not in counter: '{letter}'")
    return counter


def get_frequencies(counter, total_letters):
    for letter in counter:
        counter[letter] = round(float(counter[letter]) / total_letters, 2)
    return counter


input_string = "Language classification".lower()
test_string = "Language classificatiom".lower()
test_string2 = "Hello world".lower()

input_frequencies = get_frequencies(count_letters(input_string),len(input_string))
test_string_frequencies = get_frequencies(count_letters(test_string),len(test_string))
test_string2_frequencies = get_frequencies(count_letters(test_string2),len(test_string2))


r12, p_value = pearsonr(list(input_frequencies.values()), list(test_string_frequencies.values()))
r13, p_value = pearsonr(list(input_frequencies.values()), list(test_string2_frequencies.values()))

print(f"r12: {r12}")
print(f"r13: {r13}")
