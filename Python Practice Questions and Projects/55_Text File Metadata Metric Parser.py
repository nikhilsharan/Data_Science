# Open the file in read-only mode
with open("input.txt", "r") as file:
    lines = file.readlines()

# Calculate metrics
line_count = len(lines)

# Count unique whitespace-separated words
unique_words = set()
for line in lines:
    unique_words.update(line.split())
word_count = len(unique_words)

# Count total characters (excluding newline characters)
character_count = sum(len(line.rstrip("\n")) for line in lines)

# Display results
print(f"Metrics Summary: {line_count} lines, {word_count} words, {character_count} characters.")