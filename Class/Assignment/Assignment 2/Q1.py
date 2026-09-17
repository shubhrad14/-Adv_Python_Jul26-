def count_characters(text):
    freq = {}

    # Convert string to lowercase
    text = text.lower()

    # Count only alphabetic characters
    for ch in text:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    # Return dictionary in alphabetical order
    sorted_freq = {}
    for key in sorted(freq.keys()):
        sorted_freq[key] = freq[key]

    return sorted_freq


# Example
text = "Shubhra Devlekar"
result=count_characters(text)

for key, value in result.items():
    print(f"'{key}': {value}")