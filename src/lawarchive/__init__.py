"""Cosilico Law Archive - Open source US statute text via API."""

from lawarchive.archive import LawArchive
from lawarchive.models import Section, Subsection, Citation, SearchResult

__version__ = "0.1.0"
__all__ = ["LawArchive", "Section", "Subsection", "Citation", "SearchResult"]
