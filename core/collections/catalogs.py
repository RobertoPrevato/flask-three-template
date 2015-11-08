
class CatalogPage:
    """
    Represents a page of paginated results.
    """
    def __init__(self, subset, page, total):
        self.subset = subset
        self.page = page
        self.total = total
