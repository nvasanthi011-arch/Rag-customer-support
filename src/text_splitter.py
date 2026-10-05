from loader import load_document
def split_text(text, chunk_size=300, overlap=20):
    """
    Splits the input text into chunks of specified size with optional overlap.

    Args:
        text (str): The input text to be split.
        chunk_size (int): The maximum size of each chunk. Default is 1000 characters.
        overlap (int): The number of overlapping characters between chunks. Default is 200 characters.

    Returns:
        list: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)    
        start  = end - overlap 
    return chunks 

if __name__ == "__main__":
    document = load_document("data/troubleshooting.txt")
    chunks = split_text(document)
    print ("total chunks:", len(chunks))