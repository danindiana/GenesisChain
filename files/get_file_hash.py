# get_file_hash.py
import hashlib
import sys

def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_file_hash.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_hash = get_file_hash(file_path)
    print(f"SHA256 Hash: {file_hash}")
