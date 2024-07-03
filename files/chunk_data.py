# chunk_data.py
import sys
import json

def chunk_data(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python chunk_data.py <file_path> <chunk_size>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    chunk_size = int(sys.argv[2])

    with open(file_path, 'r') as file:
        data = file.read()
    
    chunks = chunk_data(data, chunk_size)
    chunks_json = json.dumps(chunks, indent=4)
    
    with open('chunked_data.json', 'w') as out_file:
        out_file.write(chunks_json)
    
    print("Data chunked and saved to chunked_data.json")
