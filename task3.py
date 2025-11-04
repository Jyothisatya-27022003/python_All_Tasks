# Task 3: Basic File Handling

def find_and_replace(filename, old_word, new_word):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        if old_word not in data:
            print(f"⚠️ The word '{old_word}' was not found in the file.")
            return
        modified_data = data.replace(old_word, new_word)
        with open(filename, 'w') as file:
            file.write(modified_data)
        print(f"✅ Successfully replaced '{old_word}' with '{new_word}' in '{filename}'.")
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied to access '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

print("📄 Welcome to the File Find-and-Replace Program!")
filename = input("Enter the file name (with .txt extension): ")
old_word = input("Enter the word to find: ")
new_word = input("Enter the word to replace it with: ")

find_and_replace(filename, old_word, new_word)
