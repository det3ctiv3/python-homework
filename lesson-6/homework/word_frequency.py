import os
from collections import Counter
import string

# Function to create sample.txt if it doesn't exist
def create_sample_file():
    if not os.path.exists("sample.txt"):
        print("sample.txt does not exist. Please create it by typing a paragraph:")
        user_input = input("Type your paragraph here: ")
        with open("sample.txt", "w") as file:
            file.write(user_input)
        print("sample.txt has been created.")

# Function to count word frequency
def count_word_frequency():
    with open("sample.txt", "r") as file:
        text = file.read().lower()  # Convert text to lowercase
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()  # Split text into words
        word_count = Counter(words)  # Count word frequency
        return words, word_count

# Function to display and save the results
def generate_report(words, word_count):
    total_words = len(words)
    top_5_words = word_count.most_common(5)

    # Console output
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} times")

    # Save to word_count_report.txt
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write("Top 5 Words:\n")
        for word, count in top_5_words:
            report_file.write(f"{word} - {count}\n")

# Main program
def main():
    create_sample_file()
    words, word_count = count_word_frequency()
    generate_report(words, word_count)

if __name__ == "__main__":
    main()