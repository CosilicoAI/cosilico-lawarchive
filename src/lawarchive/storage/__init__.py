"""Storage backends for the law archive."""

from lawarchive.storage.base import StorageBackend
from lawarchive.storage.sqlite import SQLiteStorage

__all__ = ["StorageBackend", "SQLiteStorage"]
