# Regional Country and Language Reference (Europe + Turkey)

This folder provides an optional reference dataset to support developers who wish to localise content using the **SafeNutriKids Localisation Layer**.  
The dataset contains a curated list of EU Member States plus Turkey, with local names, English names, ISO country codes, and authoritative EU URIs.

These files are **not required** by the localisation engine but serve as convenient lookup tables when building catalogues or implementing culturally aware content selection.

---

## 1. Country Reference (Europe + Turkey)

### `regional_countries_europe.v1.0.csv`
Human-readable table containing:

- `local_name` — country name in the country’s primary or official language(s)  
- `country_en` — English country name  
- `ISO_31661_alpha2` — ISO 3166-1 alpha-2 country code  
- `ISO_31661_num` — ISO 3166-1 numeric code  
- `country_uri` — EU Publications Office controlled vocabulary URI (EU Vocabularies)

### `regional_countries_europe.v1.0.json`
Machine-readable JSON version of the same dataset, useful for:

- validation  
- building dynamic dropdowns  
- enriching localisation catalogues  
- statistical processing or pipeline integration  


## 2. Language Reference (Europe + Turkey)

### `regional_languages_europe.v1.0.csv`
Contains official national languages for the same region set, with:

- **language_code** — ISO 639-1 code (e.g., `en`, `tr`, `et`)  
- **language_en** — language name in English  
- **autonym** — language name in its own language (e.g., *Türkçe*)  
- **script** — primary writing system (e.g., Latin, Cyrillic, Greek)  
- **notes** — optional clarifications (e.g., “widely used as second language”)  

### `regional_languages_europe.v1.0.json`
Machine-readable version for:

- backend systems  
- AI prompting pipelines  
- metadata validation  
- automatically generating language options  

---
## Source & Licensing

The country names, codes, and URIs are derived from the **EU Publications
Office** controlled vocabularies:

<https://publications.europa.eu/en/web/eu-vocabularies>

These datasets are licensed under **CC BY 4.0**, which permits reuse with attribution.

Additional formatting, local-name enrichment, and data cleaning were added as part of the DRG4FOOD Toolbox contribution.

---

## How to Use This Reference

Developers can use this reference data to:

- Build consistent **ContentVariant** catalogues  
- Validate metadata before ingestion  
- Create **language/country selectors** in UIs  
- Integrate culturally-aware **AI prompting** or personalisation logic  
- Provide culturally aligned content recommendations  

These reference files are **optional but recommended** for any implementation that requires structured, culturally-aware localisation.

---