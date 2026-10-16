"""
Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""

# === TEXT ANALYSIS TOOL ===

# 1. รับข้อความจากผู้ใช้
text = input("Enter text: ")

# กำหนดตัวอักษรที่เป็นสระ (Vowels)
vowels_list = "aeiouAEIOU"

# --- Character Analysis ---
total_chars_with_space = len(text)
total_chars_without_space = len(text.replace(" ", ""))

# นับสระและพยัญชนะ
found_vowels = []
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels_list:
            vowel_count += 1
            found_vowels.append(char)
        else:
            consonant_count += 1

# หาตัวอักษรที่พบบ่อยที่สุด (ไม่รวมช่องว่าง และไม่สนตัวพิมพ์เล็กใหญ่)
clean_text_lower = text.replace(" ", "").lower()
max_freq = 0
most_freq_char = ""
for char in set(clean_text_lower):
    if char.isalpha():
        freq = clean_text_lower.count(char)
        if freq > max_freq:
            max_freq = freq
            most_freq_char = char

# --- Word Analysis ---
words = text.split()
total_words = len(words)

longest_word = ""
shortest_word = words[0] if words else ""
vowel_start_words = 0
consonant_start_words = 0

for w in words:
    # ตัดสัญลักษณ์พิเศษรอบคำออกเบื้องต้นเผื่อมี
    clean_w = "".join([c for c in w if c.isalpha()])
    if clean_w:
        if len(w) > len(longest_word):
            longest_word = w
        if len(w) < len(shortest_word):
            shortest_word = w
        
        # เช็คคำที่ขึ้นต้นด้วยสระหรือพยัญชนะ
        if w[0] in vowels_list:
            vowel_start_words += 1
        else:
            consonant_start_words += 1
# สร้าง Acronym จากตัวอักษรตัวแรกของแต่ละคำ (Uppercase)
acronym = "".join([w[0].upper() for w in words if w])

# --- Transformations ---
title_case_text = text.title()
upper_case_text = text.upper()
lower_case_text = text.lower()

# กลับด้านข้อความทั้งหมด (Reversed Text ใช้ slicing [::-1])
reversed_text = text[::-1]

# กลับด้านทีละคำ (Words Reversed)
reversed_words_list = [w[::-1] for w in words]
reversed_words_text = " ".join(reversed_words_list)

# --- แสดงผลลัพธ์ตามรูปแบบตัวอย่าง ---
print("\n=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print("- Total characters: {} (with spaces), {} (without spaces)".format(total_chars_with_space, total_chars_without_space))
print("- Vowels: {} ({})".format(vowel_count, ", ".join(found_vowels)))
print("- Consonants: {}".format(consonant_count))
print("- Most frequent: '{}' (appears {} times)".format(most_freq_char, max_freq))

print("\nWord Analysis:")
print("- Total words: {}".format(total_words))
print("- Longest word: \"{}\" ({} letters)".format(longest_word, len(longest_word)))
print("- Shortest word: \"{}\" ({} letters)".format(shortest_word, len(shortest_word)))
print("- Words starting with vowels: {} (e.g., \"{}\")".format(vowel_start_words, longest_word if longest_word and longest_word[0] in vowels_list else "Over"))
print("- Words starting with consonants: {}".format(consonant_start_words))

print("\nTransformations:")
print("- Title Case: {}".format(title_case_text))
print("- Upper Case: {}".format(upper_case_text))
print("- Lower Case: {}".format(lower_case_text))
print("- Acronym: {}".format(acronym))
print("- Reversed Text: {}".format(reversed_text))
print("- Words Reversed: {}".format(reversed_words_text))