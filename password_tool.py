from zxcvbn import zxcvbn

# Function to analyze password strength

def analyze_password(password):
    result = zxcvbn(password)
    print(f"Password strength score: {result['score']} (0=weak, 4=strong)")
    print(f"Suggestions: {result['feedback']['suggestions']}")
    print(f"Crack time estimate: {result['crack_times_display']}")

# Function to get user info for wordlist

def get_user_inputs():
    name = input("Enter your name: ")
    year = input("Enter a memorable year: ")
    pet = input("Enter your pet's name: ")
    return [name, year, pet]

# Function to generate variations

def generate_variations(words):
    variations = set()
    for w in words:
        variations.add(w)
        variations.add(w[::-1])  # reversed
        variations.add(w + '123')  # appending
        # Add leetspeak conversion
        leet_map = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5', 't':'7'}
        leetspeak = ''.join(leet_map.get(c, c) for c in w.lower())
        variations.add(leetspeak)
    return list(variations)

# Function to save wordlist

def save_wordlist(words):
    with open('wordlist.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
    print('Wordlist saved to wordlist.txt')

# Main execution

if __name__ == "__main__":
    pw = input("Enter a password to analyze: ")
    analyze_password(pw)
    user_words = get_user_inputs()
    variation_list = generate_variations(user_words)
    save_wordlist(variation_list)
