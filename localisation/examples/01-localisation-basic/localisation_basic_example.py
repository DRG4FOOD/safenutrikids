"""
Example: Using the localisation layer to select child-appropriate nutrition content.

This script loads a sample JSON catalogue, constructs a NutritionLocaliser instance,
and selects the best-matching content variant based on language, country, and age.
It models a realistic scenario: an English- or Turkish-speaking child living in
Turkey, where the app should return content in the chosen language for the local
context.
"""

from safenutrikids.localisation import NutritionLocaliser
import json
from pathlib import Path


def main() -> None:
    # Load the example catalogue
    catalogue_path = Path(__file__).parent / "hydration_example.json"
    with open(catalogue_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Ask the user which language they want to see
    lang = input("Choose language (en/tr): ").strip().lower()

    if lang not in ("en", "tr"):
        print("Unsupported language. Please choose 'en' or 'tr'.")
        return

    # Construct the localiser from the JSON config
    localiser = NutritionLocaliser.from_dict(config)

    # In this example we assume a 7-year-old child living in Turkey (country='TR')
    variant = localiser.select(
        content_key="hydration_basics",
        language=lang,
        country="TR",
        age=7,
    )

    print("\nSelected text:")
    print(variant.payload)


if __name__ == "__main__":
    main()