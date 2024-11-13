from functools import wraps
# Function to hash the password using scrypt
def hash_password(password: str, salt: bytes):
    password_bytes = password.encode('utf-8')

    kdf = Scrypt(
        length=32,     # Length of the derived key
        salt=salt,     # Salt used in hashing
        n=32768,       # CPU/memory cost factor (2^15 recommended)
        r=8,           # Block size
        p=1,           # Parallelization factor
        backend=default_backend()
    )

    # Derive the key (hashed password)
    hashed_password = kdf.derive(password_bytes)
    return hashed_password

# Function to verify the password using scrypt
def verify_password(stored_hash, password: str, salt: bytes):
    kdf = Scrypt(
        length=32,     # Length of the derived key
        salt=salt,     # Salt (same as used for hashing)
        n=32768,       # CPU/memory cost factor
        r=8,           # Block size
        p=1,           # Parallelization factor
        backend=default_backend()
    )

    try:
        kdf.verify(password.encode('utf-8'), stored_hash)  # Verify the password
        return True
    except Exception as e:
        return False
