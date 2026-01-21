"""
Day 01: Pagination helper
Purpose: reusable pagination logic for backend APIs
"""

def paginate(items, page=1, page_size=10):
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive integers")

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "page": page,
        "page_size": page_size,
        "total_items": len(items),
        "total_pages": (len(items) + page_size - 1) // page_size,
        "data": items[start:end]
    }


if __name__ == "__main__":
    sample = list(range(1, 51))
    print(paginate(sample, page=2, page_size=10))

