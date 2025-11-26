"""
Schema-level tests for the SafeNutriKids localisation layer.

These tests make sure that:

1. The variant JSON Schema is itself valid as a JSON Schema.
2. The example catalogue (hydration_example.json) conforms to that schema.
"""

from pathlib import Path
import json

import jsonschema


# Resolve paths relative to this test file
ROOT = Path(__file__).resolve().parents[1]

VARIANT_SCHEMA_PATH = ROOT / "schemas" / "variant-schema.v1.0.json"
HYDRATION_EXAMPLE_PATH = ROOT / "examples" / "01-localisation-basic" / "hydration_example.json"


def load_json(path: Path):
    """Utility helper to load a JSON file with UTF-8 encoding."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_variant_schema_is_valid_jsonschema():
    """
    Ensure that variant-schema.v1.0.json is a valid JSON Schema document.

    If this test fails, the schema itself is malformed (e.g. typo in keywords,
    wrong types, etc.).
    """
    schema = load_json(VARIANT_SCHEMA_PATH)

    # This will raise jsonschema.exceptions.SchemaError if the schema is invalid.
    jsonschema.Draft202012Validator.check_schema(schema)


def test_hydration_example_conforms_to_variant_schema():
    """
    Validate all variants in hydration_example.json against the variant schema.

    This ensures that the example catalogue we ship is consistent with the
    ContentVariant model used by the localisation layer.
    """
    schema = load_json(VARIANT_SCHEMA_PATH)
    catalogue = load_json(HYDRATION_EXAMPLE_PATH)

    # Our example has a single key "hydration_basics", which maps to a list
    # of content variants.
    variants = catalogue.get("hydration_basics", [])

    assert variants, "Expected at least one variant in hydration_example.json"

    for variant in variants:
        # Will raise jsonschema.ValidationError if the variant doesn't match.
        jsonschema.validate(instance=variant, schema=schema)