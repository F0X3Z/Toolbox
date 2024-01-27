import hashlib

def hash_string(text, hash_algorithm):
    hash_func = hashlib.new(hash_algorithm)
    hash_func.update(text.encode('utf-8'))
    return hash_func.hexdigest()

def dehash(hash_value, wordlist):
    hash_algorithms = {
        32: 'md5',
        40: 'sha1'
        # Add more lengths and corresponding algorithms if needed
    }

    hash_length = len(hash_value)

    if hash_length not in hash_algorithms:
        raise ValueError("Unsupported hash length, unknown hash")

    hash_algorithm = hash_algorithms[hash_length]

    with open(wordlist, 'r') as f:
        for word in f:
            hashed_word = hash_string(word.strip(), hash_algorithm)
            if hashed_word == hash_value:
                return f"Found: {word.strip()}"

    return "Exhausted: Hash not found in wordlist"

if __name__ == "__main__":
    # Example usage
    hash_to_crack = input("Enter the hash to crack: ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    result = dehash(hash_to_crack, wordlist_file)
    print(result)
