"""
SafeNutriKids Localisation Layer
================================

This library implements a metadata-driven localisation layer for child-centred
nutrition content. It selects culturally and linguistically appropriate content
variants using explicit metadata rather than hard-coded locale switches.

Core concepts:
- Content item: logical unit (e.g. "hydration_basics", "breakfast_ideas").
- Variant: concrete text or structured object tagged with metadata such as
  language, country, culture, diet and age range.
- Selection: scoring-based process to choose the best matching variant given
  a child profile and context.

License:
- MIT License (or another OSI-approved licence chosen at repository level).

Author: SafeNutriKids consortium (example implementation)
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class ContentVariant:
    """Single content variant with localisation metadata."""
    id: str
    language: str      # ISO 639-1, e.g. "en", "tr", "de"
    country: Optional[str] = None  # ISO 3166-1 alpha-2, e.g. "TR", "DE"
    culture: Optional[str] = None  # e.g. "muslim_majority", "central_europe"
    diet: Optional[str] = None     # e.g. "omnivore", "vegetarian"
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    payload: Any = None            # Text, HTML, JSON, or richer structure


class LocalisationConfigError(Exception):
    pass


class NutritionLocaliser:
    """
    Localisation engine that selects the best content variant for a given context.

    Typical usage:
        config = {
            "hydration_basics": [
                {
                    "id": "hydration_en_generic",
                    "language": "en",
                    "payload": "Drinking water regularly helps you stay focused at school.",
                },
                {
                    "id": "hydration_tr_child_6_8",
                    "language": "tr",
                    "country": "TR",
                    "age_min": 6,
                    "age_max": 8,
                    "payload": "Su içmek, okulda dikkatini toplamana yardımcı olur.",
                },
            ]
        }

        localiser = NutritionLocaliser.from_dict(config)
        variant = localiser.select(
            content_key="hydration_basics",
            language="tr",
            country="TR",
            age=7,
        )
        text = variant.payload
    """

    def __init__(self, catalogue: Dict[str, List[ContentVariant]]):
        self._catalogue = catalogue

    @classmethod
    def from_dict(cls, raw: Dict[str, List[Dict[str, Any]]]) -> "NutritionLocaliser":
        catalogue: Dict[str, List[ContentVariant]] = {}
        for content_key, variants in raw.items():
            if not isinstance(variants, list):
                raise LocalisationConfigError(
                    f"Content key '{content_key}' must map to a list of variants."
                )
            parsed: List[ContentVariant] = []
            for entry in variants:
                try:
                    variant = ContentVariant(
                        id=str(entry["id"]),
                        language=str(entry["language"]).lower(),
                        country=str(entry.get("country")).upper()
                        if entry.get("country") is not None
                        else None,
                        culture=entry.get("culture"),
                        diet=entry.get("diet"),
                        age_min=entry.get("age_min"),
                        age_max=entry.get("age_max"),
                        payload=entry.get("payload"),
                    )
                except KeyError as exc:
                    raise LocalisationConfigError(
                        f"Variant for '{content_key}' is missing mandatory field: {exc}"
                    ) from exc
                parsed.append(variant)
            catalogue[content_key] = parsed
        return cls(catalogue=catalogue)

    def select(
        self,
        content_key: str,
        language: str,
        country: Optional[str] = None,
        culture: Optional[str] = None,
        diet: Optional[str] = None,
        age: Optional[int] = None,
    ) -> ContentVariant:
        """
        Selects the best matching variant for the given content key and context.

        The scoring strategy prioritises:
          1. Exact language match.
          2. Country match.
          3. Cultural tag match.
          4. Dietary pattern match.
          5. Age range inclusion.

        In case of ties, the first defined variant with the highest score is chosen.
        """
        variants = self._catalogue.get(content_key, [])
        if not variants:
            raise KeyError(f"No variants configured for content key '{content_key}'.")

        scored: List[Tuple[int, ContentVariant]] = []
        language = language.lower()
        country = country.upper() if country is not None else None

        for variant in variants:
            score = 0

            if variant.language == language:
                score += 5

            if country is not None and variant.country == country:
                score += 3

            if culture is not None and variant.culture == culture:
                score += 2

            if diet is not None and variant.diet == diet:
                score += 2

            if age is not None:
                if variant.age_min is not None and age < variant.age_min:
                    pass
                elif variant.age_max is not None and age > variant.age_max:
                    pass
                else:
                    score += 2

            scored.append((score, variant))

        scored.sort(key=lambda item: item[0], reverse=True)
        best_score, best_variant = scored[0]

        if best_score == 0:
            # Fallback behaviour: still return the first variant to avoid empty responses.
            # Platforms may choose to override this behaviour.
            return variants[0]

        return best_variant
