"""
SafeNutriKids Localisation Layer - data models

This module defines the core data structures used by the localisation layer.
It is derived from the example implementation provided by the SafeNutriKids
project and adapted for reuse within the DRG4FOOD Toolbox.

Core concepts:
- ContentVariant: a single localised variant of a content item
  (e.g. "hydration_basics"), with metadata such as language, country,
  culture, diet and age range.
- LocalisationConfigError: raised when the catalogue configuration is invalid.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ContentVariant:
    """
    Single content variant with localisation metadata.

    Attributes:
        id: Unique identifier of this variant.
        language: ISO 639-1 language code, e.g. "en", "tr", "de".
        country: Optional ISO 3166-1 alpha-2 country code, e.g. "TR", "EE".
        culture: Optional cultural tag, e.g. "muslim_majority", "central_europe".
        diet: Optional dietary pattern tag, e.g. "omnivore", "vegetarian".
        age_min: Optional minimum age (inclusive) the variant is suitable for.
        age_max: Optional maximum age (inclusive) the variant is suitable for.
        payload: The actual content (text, HTML, JSON, etc.).
    """
    id: str
    language: str
    country: Optional[str] = None
    culture: Optional[str] = None
    diet: Optional[str] = None
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    payload: Any = None


class LocalisationConfigError(Exception):
    """Raised when the localisation catalogue is misconfigured."""
    pass