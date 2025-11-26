"""
Public interface for the SafeNutriKids localisation layer. This package
provides the data models and selection logic used to choose culturally
and linguistically appropriate content variants for child-centred
nutrition education.
"""

from .models import ContentVariant, LocalisationConfigError
from .localiser import NutritionLocaliser

__all__ = [
    "ContentVariant",
    "LocalisationConfigError",
    "NutritionLocaliser",
]