from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    """
    Create embeddings for a list of texts using the SentenceTransformer model.

    Args:
        texts (list of str): List of texts to create embeddings for.

    Returns:
        list: A list of embedding vectors.
    """
    embeddings = model.encode(texts)
    return embeddings   

if __name__ == "__main__":
    text = "the device doesnot turn on."
    embeddings = create_embeddings([text])      

    print ("original text ")
    print (text)
    print ("\nembeddings :")
    print (embeddings)

    print ("\nEmbedding dimension:")
    print (len(embeddings[0]))  # Print the dimension of the embedding vector