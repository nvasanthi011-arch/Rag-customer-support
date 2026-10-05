from pathlib import Path

def load_document(file_path):
    path = Path(file_path)

    with path.open('r', encoding='utf-8') as file:
        content = file.read()   

    return content      

if __name__ == "__main__":
    document = load_document("data/troubleshooting.txt ")
    print("Document loaded successfully:")
    print(document)