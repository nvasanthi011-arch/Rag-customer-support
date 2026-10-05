from pymilvus import MilvusClient

from loader import load_document
from text_splitter import split_text
from embeddings import create_embeddings


DB_PATH = "milvus.db"
COLLECTION_NAME = "support_documents"

client = MilvusClient(DB_PATH)
def create_collection():
    if client.has_collection(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists.")
        return

    client.create_collection(
        COLLECTION_NAME,
        dimension=384
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully.")




def insert_documents():
    document = load_document("data/troubleshooting.txt")

    chunks = split_text(
        document,
        chunk_size=300,
        overlap=20
    )

    embeddings = create_embeddings(chunks)

    data = []

    for i, chunk in enumerate(chunks):
        record = {
            "id": i,
            "vector": embeddings[i].tolist(),
            "text": chunk
        }

        data.append(record)

    client.insert(
        collection_name=COLLECTION_NAME,
        data=data
    )

    print(
        f"{len(data)} documents inserted into "
        f"collection '{COLLECTION_NAME}' successfully."
    )


if __name__ == "__main__":
    create_collection()
    insert_documents()