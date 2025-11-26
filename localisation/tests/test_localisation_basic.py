"""
Basic tests for the SafeNutriKids localisation layer.

These tests cover two core behaviours:
1. Selecting the best-matching variant when language/country/age align.
2. Falling back to the first variant when there is no suitable match.
"""

from safenutrikids.localisation import NutritionLocaliser, ContentVariant


def _build_basic_catalogue():
    """
    Small in-memory catalogue mirroring the hydration example used in the docs.

    It defines one English and one Turkish variant for the same content key:
    - both are for children aged 6–8
    - both are tagged for Turkey ("TR")
    """
    return {
        "hydration_basics": [
            ContentVariant(
                id="hydration_en_child_6_8",
                language="en",
                country="TR",
                age_min=6,
                age_max=8,
                payload="Drinking water regularly helps you stay focused at school.",
            ),
            ContentVariant(
                id="hydration_tr_child_6_8",
                language="tr",
                country="TR",
                age_min=6,
                age_max=8,
                payload="Su içmek, okulda dikkatini toplamana yardımcı olur.",
            ),
        ]
    }


def test_language_and_country_match_prefers_turkish_variant():
    """
    When the caller asks for Turkish in Turkey, the Turkish child variant
    should be selected.
    """
    catalogue = _build_basic_catalogue()
    localiser = NutritionLocaliser(catalogue)

    result = localiser.select(
        content_key="hydration_basics",
        language="tr",
        country="TR",
        age=7,
    )

    assert result.id == "hydration_tr_child_6_8"
    assert result.language == "tr"
    assert result.country == "TR"


def test_fallback_returns_first_variant_when_no_match():
    """
    When no variant matches the requested context, the engine should return
    the first defined variant for that content key.
    """
    catalogue = _build_basic_catalogue()
    localiser = NutritionLocaliser(catalogue)

    result = localiser.select(
        content_key="hydration_basics",
        language="fr",  # not present in the catalogue
        country="FR",
        age=10,
    )

    assert result.id == "hydration_en_child_6_8"