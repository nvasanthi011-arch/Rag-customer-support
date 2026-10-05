from pymilvus import MilvusClient

from embeddings import create_embeddings

DB_PATH = "milvus.db"
COLLECTION_NAME = "support_documents"

client = MilvusClient(DB_PATH)


def retrieve_similar_chunks(query, top_k=3):
    question_embedding = create_embeddings([query])
    client.load_collection(COLLECTION_NAME)

    results = client.search(
        collection_name=COLLECTION_NAME,
        data=question_embedding.tolist(),
        limit=top_k
    )

    return results


if __name__ == "__main__":
    query = "the device does not turn on"

    results = retrieve_similar_chunks(query)

    print("Question:", query)
    print("\nSearch results:")

    for result in results[0]:
        print("\nID:", result["id"])
        print("Distance/Score:", result["distance"])

        if "entity" in result:
            print("Text:")
            print(result["entity"]["text"])
        else:
            print("Text:")
            print(result["text"])