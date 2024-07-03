# create_dna_digital_storage_file.py
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python create_dna_digital_storage_file.py <header_path> <chunked_data_path> <compressed_data_path> <error_correction_data_path> <proof_of_work_path>")
        sys.exit(1)
    
    header_path = sys.argv[1]
    chunked_data_path = sys.argv[2]
    compressed_data_path = sys.argv[3]
    error_correction_data_path = sys.argv[4]
    proof_of_work_path = sys.argv[5]

    with open(header_path, 'r') as header_file:
        header = json.load(header_file)
    
    with open(chunked_data_path, 'r') as chunked_file:
        chunked_data = json.load(chunked_file)
    
    with open(compressed_data_path, 'r') as compressed_file:
        compressed_data = json.load(compressed_file)
    
    with open(error_correction_data_path, 'r') as error_file:
        error_correction_data = json.load(error_file)
    
    with open(proof_of_work_path, 'r') as proof_file:
        proof_of_work = json.load(proof_file)
    
    dna_digital_storage_file = {
        "header": header,
        "data": {
            "chunked_data": chunked_data
        },
        "compression": compressed_data,
        "error_correction": error_correction_data,
        "blockchain_enrollment": {
            "proof_of_work": proof_of_work
        }
    }
    
    with open('dna_digital_storage.json', 'w') as out_file:
        out_file.write(json.dumps(dna_digital_storage_file, indent=4))
    
    print("DNA digital storage file created and saved to dna_digital_storage.json")
