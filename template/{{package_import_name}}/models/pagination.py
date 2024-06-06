"""Pagination models."""
from pydantic import BaseModel, Field, computed_field


class Pagination(BaseModel):
    """Pagination class."""
    page: int = Field(description="Current page number (0 indexed).", examples=[0])
    size: int = Field(description="Number of objects per page.", examples=[100])
    result_count: int = Field(description="Total count of objects in filtered result set.", examples=[200])
    total_count: int = Field(description="Total count of objects before filtering.", examples=[200])

    @computed_field  # type: ignore[misc]
    @property
    def total_pages(self) -> int:
        """Total number of pages."""
        return (self.result_count + self.size - 1) // self.size

    @computed_field  # type: ignore[misc]
    @property
    def last_page(self) -> int:
        """Last page number (0 indexed)."""
        return max(0, self.total_pages - 1)
