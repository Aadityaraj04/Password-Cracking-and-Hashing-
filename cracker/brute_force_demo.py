
import itertools
import hashlib

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(target_hash, max_length=4):
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            attempt = ''.join(guess)
            if hash(attempt) == target_hash:
                return attempt
    return None

if __name__ == "__main__":
    original = 'abc1'
    target_hash = hash(original)
    print(f"Target Hash: {target_hash}")
    result = brute_force(target_hash)
    print("Cracked Password:", result if result else "Not found")
