# SafeNutriKids

![DRG4FOOD](https://img.shields.io/badge/DRG4FOOD-project-green)
![Release](https://img.shields.io/github/v/release/DRG4FOOD/safenutrikids)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)

SafeNutriKids is a DRG4FOOD Open Call project advancing **AI-driven, child-centred
nutrition education**. This repository provides the project’s open-source
contributions to the **DRG4FOOD Toolbox**, including:

- a reusable **localisation engine** for culturally and linguistically appropriate content  
- high-level **parental data-access guidelines** for GDPR-aligned platforms  

The components are designed to support responsible, transparent and adaptable
digital nutrition applications for children and families.

---

## Repository Structure

```
safenutrikids/
├── src/safenutrikids/         # Python package (localisation enabler)
│   └── localisation/
│
├── localisation/              # docs, examples, schemas, reference data
│   ├── examples/
│   ├── reference/
│   ├── schemas/
│   └── tests/
│
├── parental-access/           # documentation-only guidelines
├── pyproject.toml             # package configuration
└── README.md                  # (this file)
```

---

## Installation (local development)

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -e .
```

This installs the **SafeNutriKids** package, including the localisation module.

---

## Quickstart (Localisation Engine)

```python
from safenutrikids.localisation import NutritionLocaliser, ContentVariant
```

Run the bundled example:

```bash
python localisation/examples/01-localisation-basic/localisation_basic_example.py
```

Run the tests:

```bash
pytest localisation/tests
```

---

## Components in This Repository

### **Localisation Layer**
Reusable Python engine for selecting culturally and linguistically appropriate
content variants.  
See: `localisation/README.md`

### **Parental Data Access Guidelines**
Documentation-only resource outlining responsible structures for parental access
to children’s data in GDPR-aligned platforms.  
See: `parental-access/README.md`

---

## License

This project is released as open source as part of the DRG4FOOD Toolbox.  
See the included `LICENSE` file for terms.