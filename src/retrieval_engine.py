def score_chunk(query, chunk):
    """
    Score a chunk based on how many query words appear in it.
    This is a simple keyword-based retrieval method.
    """

    query_words = query.lower().split()
    chunk_lower = chunk.lower()

    score = 0

    for word in query_words:
        if word in chunk_lower:
            score += 1

    return score


def search_chunks(query, document_chunks, top_k=3):
    """
    Search all document chunks and return the top matching chunks.

    Args:
        query (str): User question or request.
        document_chunks (dict): Dictionary of filename -> list of chunks.
        top_k (int): Number of results to return.

    Returns:
        list[dict]: Top matching chunks with filename, score, and text.
    """

    results = []

    for filename, chunks in document_chunks.items():
        for index, chunk in enumerate(chunks):
            score = score_chunk(query, chunk)

            if score > 0:
                results.append(
                    {
                        "filename": filename,
                        "chunk_index": index,
                        "score": score,
                        "text": chunk
                    }
                )

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]