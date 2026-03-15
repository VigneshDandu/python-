text = "Vignesh is learning Python"

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("String:", text)
print("Vowel count:", count)