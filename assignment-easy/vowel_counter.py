def vowel_counter(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(vowel_counter("Hello"))
print(vowel_counter("My name is Uzair"))