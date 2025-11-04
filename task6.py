# Task 6: Word Count Tool

from collections import Counter

def analyze_text_file(filename):
    try:
        # Step 1: Read the content of the file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Step 2: Calculate number of lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_chars = len(text)
        words = text.split()
        num_words = len(words)

        # Step 3: Word frequency analysis
        # Convert all words to lowercase and remove punctuation
        cleaned_words = [word.lower().strip('.,!?;:"()[]{}') for word in words]
        word_freq = Counter(cleaned_words)

        # Step 4: Display results
        print("\n📊 TEXT ANALYSIS REPORT 📊")
        print("-" * 40)
        print(f"📄 Lines Count     : {num_lines}")
        print(f"📝 Words Count     : {num_words}")
        print(f"🔠 Characters Count: {num_chars}")
        print("-" * 40)
        print("🔍 Top 50 Most Common Words:")
        for word, count in word_freq.most_common(50):
            print(f"{word:15} → {count} times")

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# --- Main Program ---
print("📂 Welcome to the Word Count & Analysis Tool!")
filename = input("Enter the text file name (with .txt extension): ")

analyze_text_file(filename)
