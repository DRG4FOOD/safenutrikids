# SafeNutriKids Localisation Layer

This folder contains the **localisation layer** contributed by the SafeNutriKids
project to the DRG4FOOD Toolbox. It provides a small, reusable Python component
for selecting culturally and linguistically appropriate content variants for
children, based on explicit metadata.

The core ideas are:

- **ContentVariant** – a single variant of a content item  
  (e.g. `"hydration_basics"`) with fields such as language, country, age range,
  culture, diet and payload.
- **NutritionLocaliser** – an engine that selects the best matching variant for
  a given child profile (language, country, age, etc.), using a simple scoring
  strategy.

> Status: prototype v1.0, structured and cleaned for reuse in other DRG4FOOD
> projects and third-party applications.

---

## Folder structure

This folder contains **documentation, datasets, examples, and tests** for the
localisation layer. The actual Python package code is located in:

```
src/safenutrikids/localisation/
```

### Contents

- **`src/safenutrikids/localisation/`**  
  Core Python package:
  - `models.py` – `ContentVariant`, `LocalisationConfigError`
  - `localiser.py` – `NutritionLocaliser`
  - `__init__.py` – clean public API exports

- **`schemas/`**  
  `variant-schema.v1.0.json` – JSON Schema describing a single
  `ContentVariant` object.

- **`reference/`**  
  Optional helper datasets (not required by the engine):
  - `regional_countries_europe.*` – EU+TR country codes and names  
  - `regional_languages_europe.*` – EU+TR language codes, names and autonyms  

- **`examples/`**  
  Runnable examples:
  - `01-localisation-basic/` – load a small catalogue and select a variant
    based on language, country, and age.

- **`tests/`**  
  Basic tests ensuring the selection logic continues to work.

- **`docs/`**  
  PDF guidelines and future narrative documentation.

---

## Installation (local development)

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -e .
```

---

## Quickstart: using the localisation engine

After installing the package:

```python
from safenutrikids.localisation import NutritionLocaliser, ContentVariant
```

To run the example:

```bash
python localisation/examples/01-localisation-basic/localisation_basic_example.py
```

---

## Running tests

```bash
pytest localisation/tests
```