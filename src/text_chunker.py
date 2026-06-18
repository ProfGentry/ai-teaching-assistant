def chunk_text(text, chunk_size=500, overlap=50):
    """
    Author: Jennifer Gentry
    Date: 6/18/2026
    Split text into smaller overlapping chunks.

    Args:
        text (str): Full document text.
        chunk_size (int): Number of characters per chunk.
        overlap (int): Number of characters repeated between chunks.

    Returns:
        list[str]: Text chunks.
    """

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks