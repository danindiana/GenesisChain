# compress_data.py
import gzip
import base64
import sys

def compress_data(data):
    compressed_data = gzip.compress(data.encode('utf-8'))
    return base64.b64encode(compressed_data).decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compress_data.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    with open(file_path, 'r') as file:
        data = file.read()
    
    compressed_data = compress_data(data)
    
    with open('compressed_data.json', 'w') as out_file:
        out_file.write(json.dumps({"compressed_data": compressed_data}, indent=4))
    
    print("Data compressed and saved to compressed_data.json")
