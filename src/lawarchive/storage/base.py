"""Abstract base class for storage backends."""

from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from lawarchive.models import Section, SearchResult, TitleInfo


class StorageBackend(ABC):
    """Abstract storage backend interface."""

    @abstractmethod
    def store_section(self, section: Section) -> None:
        """Store a section in the database."""
        pass

    @abstractmethod
    def get_section(
        self,
        title: int,
        section: str,
        subsection: Optional[str] = None,
        as_of: Optional[date] = None,
    ) -> Optional[Section]:
        """Retrieve a section by citation."""
        pass

    @abstractmethod
    def search(
        self,
        query: str,
        title: Optional[int] = None,
        limit: int = 20,
    ) -> list[SearchResult]:
        """Full-text search across sections."""
        pass

    @abstractmethod
    def list_titles(self) -> list[TitleInfo]:
        """List all available titles with metadata."""
        pass

    @abstractmethod
    def get_references_to(self, title: int, section: str) -> list[str]:
        """Get sections that this section references."""
        pass

    @abstractmethod
    def get_referenced_by(self, title: int, section: str) -> list[str]:
        """Get sections that reference this section."""
        pass
