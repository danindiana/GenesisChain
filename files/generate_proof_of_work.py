import sys
import json
import hashlib
import time

def generate_proof_of_work(data, difficulty="00000"):
    """Generates a Hashcash proof-of-work for the given data.

    Args:
        data (str): The data to be hashed.
        difficulty (str, optional): The difficulty level (leading zeros in the hash). Defaults to "00000".

    Returns:
        dict: A dictionary containing the nonce, hash, and difficulty.
    """
    nonce = 0
    start_time = time.time()  # Track computation time

    while True:
        hash_result = hashlib.sha256((data + str(nonce)).encode()).hexdigest()
        if hash_result.startswith(difficulty):
            end_time = time.time()
            return {
                "nonce": nonce,
                "hash": hash_result,
                "difficulty": difficulty,
                "time_taken": end_time - start_time  # Include time taken
            }
        nonce += 1


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python generate_proof_of_work.py <file_path> [difficulty]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    difficulty = sys.argv[2] if len(sys.argv) == 3 else "00000"  # Allow optional difficulty

    with open(file_path, 'r') as file:
        data = file.read()

    proof_of_work = generate_proof_of_work(data, difficulty)

    with open('proof_of_work.json', 'w') as out_file:
        out_file.write(json.dumps(proof_of_work, indent=4))

    print("Proof-of-work data generated and saved to proof_of_work.json")
