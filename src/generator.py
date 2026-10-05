from retriever import retrieve_similar_chunks


def build_prompt(query, results):
    context_parts = []

    for result in results[0]:
        if "entity" in result:
            text = result["entity"]["text"]
        else:
            text = result["text"]

        context_parts.append(text)

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a customer support assistant.

Answer the user's question using only the context provided below.

If the answer cannot be found in the context, say:
"I do not have enough information in the provided documents."

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    return prompt


if __name__ == "__main__":
    query = "the device does not turn on"

    results = retrieve_similar_chunks(query)

    prompt = build_prompt(query, results)

    print(prompt)