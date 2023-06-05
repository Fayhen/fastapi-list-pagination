from typing import List, TypedDict


class Paginator(TypedDict):
    contents: List
    current_page: int
    pages: int
    limit: int


def generate_list():
    return list(range(0, 1000))


def make_chunks(lst: List, limit=10):
    return [lst[i:i+limit] for i in range(0, len(lst), limit)]


def get_list(limit: int = 10, page: int = 1) -> Paginator:
    full_range = generate_list()
    chunks = make_chunks(full_range, limit)
    page_count = len(chunks)
    page = min(page_count, page)

    paginated = {
        "contents": chunks[page - 1],  # Account for the 0 index
        "current_page": page,
        "pages": page_count,
        "limit": limit
    }

    return paginated
