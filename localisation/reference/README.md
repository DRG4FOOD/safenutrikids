# Regional Country and Language and Diestary Reference (Europe + Turkey)

This folder provides **optional reference datasets** to support developers who wish to localise content using the **SafeNutriKids Localisation Layer**.  
These datasets are **not required** by the localisation engine, but they are highly useful when building catalogues, ensuring metadata consistency, or implementing culturally sensitive content selection.

The reference collection currently includes:

- **Regional countries and country codes** (Europe + Turkey)  
- **Languages, autonyms and scripts** (Europe + Turkey)  
- **Dietary patterns and constraints**, inspired by the *Open Food Facts* “These diets” project note

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

## 3. Dietary Attributes Reference

This dataset provides a structured list of **dietary patterns**, **vegetarian/vegan variants**, and **dietary constraints** to support culturally aware nutrition personalisation.

The dataset is inspired by the  
**Open Food Facts “These diets” project note**:  
https://wiki.openfoodfacts.org/These_diets

It includes well-known dietary patterns such as:

- Vegetarian, vegan  
- Ovo-vegetarian, lacto-vegetarian, ovo-lacto-vegetarian  
- Buddhist vegetarianism, Jain vegetarianism  
- Raw veganism, raw foodism  
- Fruitarianism  
- Flexitarian, pescatarian  
- Macrobiotic diet  
- Kangatarianism  
- Gluten-free, lactose-free  
- Omnivore (default fallback)

### `dietary_attributes.v1.0.csv`
Human-readable dataset with:

- `id` — unique identifier  
- `parent_id` — optional hierarchy (e.g. vegan ← vegetarian)  
- `description_en` — short, clear dietary description  
- `category` — e.g. *vegetarian_pattern*, *diet_pattern*, *diet_constraint*  
- `public_domain_definition` — whether the diet has an open, public definition  
- `diet_society` / `diet_society_url` — societies or certification bodies when applicable  
- `rule_set_notes` — summary of known rule-sets  
- `open_food_facts_source` — provenance link to Open Food Facts documentation  

### `dietary_attributes.v1.0.json`
Machine-readable JSON version for:

- validating dietary metadata  
- enabling structured personalisation logic  
- building user-facing selectors linked to dietary needs  
- integrating into recommendation rules or AI prompting flows  

> **Important:** These dietary patterns are provided strictly as **optional FOOD-rule metadata**.  
> They are **not** intended as medical guidance or as identity labels.

---

## Source & Licensing

Country and language data are derived from the **EU Publications Office** controlled vocabularies:  
<https://publications.europa.eu/en/web/eu-vocabularies>

Diet patterns draw on public documentation from **Open Food Facts**, including:  
https://wiki.openfoodfacts.org/These_diets  
and related allergen/dietary-category pages.

All datasets are licensed under **CC BY 4.0**, enabling reuse with attribution.

Additional formatting, curation, and validation were added as part of the DRG4FOOD Toolbox contribution.
---

## How to Use These Reference Datasets

Developers may use these optional datasets to:

- Build **consistent ContentVariant catalogues**  
- Validate localisation metadata before ingestion  
- Create **country/language/diet selectors** in applications  
- Support **culturally and diet-aware AI personalisation**  
- Improve metadata quality across DRG4FOOD components  

These files are **optional but recommended** to be buiklt upon for implementations that require structured, culturally sensitive localisation and dietary attributes.

---