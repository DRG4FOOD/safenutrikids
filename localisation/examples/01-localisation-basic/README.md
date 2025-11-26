# Example 01 – Localisation (Basic)

This folder contains a simple end-to-end example showing how the SafeNutriKids
localisation layer can be used to select culturally and linguistically
appropriate content variants.

## Files

### `localisation_basic_example.py`
Demonstrates how to:
- load a localisation catalogue from JSON
- initialise the `NutritionLocaliser`
- interactively select the best variant based on language, country, and age
- print the selected output

This example models a realistic scenario:

**A child living in Turkey who may speak English or Turkish**, where the app
should return age-appropriate content in the chosen language while respecting
the local context.

During execution, the script prompts the user:  
`Choose language (en/tr):`

### `hydration_example.json`
A small catalogue containing two variants for the key `hydration_basics`:

- an English variant (`language: "en"`, `country: "TR"`)
- a Turkish variant (`language: "tr"`, `country: "TR"`)

Both are suitable for ages 6–8.  
The localisation layer chooses the best match based on metadata.

## Running the example

From the repository root, after installing the package:

```bash
python localisation/examples/01-localisation-basic/localisation_basic_example.py
```

You will then be prompted to choose a language.