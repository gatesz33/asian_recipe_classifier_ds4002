# Asian Recipe Ingredients Dataset

## Data Summary

This dataset contains recipe ingredient data scraped from [Taste Asian Food](https://tasteasianfood.com/). The data captures ingredients, cooking methods, and regional associations of Asian recipes. It serves as the foundation for exploratory data analysis and classification tasks in the **Asian Recipe Classifier** project.

The dataset file is stored in our GitHub repository: [asianrecipesfinal.csv](https://github.com/gatesz33/asian_recipe_classifier_ds4002).

---

## Provenance

* **Source**: Scraped from the recipe website [tasteasianfood.com](https://tasteasianfood.com/)
* **Repository**: [Asian Recipe Classifier GitHub Repository](https://github.com/gatesz33/asian_recipe_classifier_ds4002)
* **Dataset Name**: `asianrecipesfinal.csv`
* **Collection Method**: Automated scraping and parsing of recipe pages, followed by initial cleaning and standardization.

---

## License

**CC0 1.0 Universal (CC0 1.0) Public Domain Dedication**

To the extent possible under law, the creators of this dataset have waived all copyright and related or neighboring rights to this work.

You are free to:

* Copy, modify, distribute, and perform the work
* Use the dataset for commercial or non-commercial purposes
* Do so without asking permission

[Full CC0 1.0 Legal Code](https://creativecommons.org/publicdomain/zero/1.0/)

---

## Ethical Statements

At this stage, no ethical complications have been identified with the collection or use of this dataset.
Potential considerations include:

* **Ambiguities in ingredients**: Some scraped ingredient entries may contain vague descriptors (e.g., “pieces,” “sections”), which could reduce clarity.
* **Bias by source**: Since all data originates from a single website, the dataset may not fully represent all Asian cuisines.

These risks are acknowledged, and care will be taken to ensure analysis and conclusions are transparent about these limitations.

---

## Data Dictionary

| Field Name     | Data Type | Description                              | Allowed Values / Range                      | Example                | Notes                                                     |
| -------------- | --------- | ---------------------------------------- | ------------------------------------------- | ---------------------- | --------------------------------------------------------- |
| `Ingredient`   | String    | Name of ingredient used in the recipe    | Free text (lowercase standardized)          | `eggs`                 | Parsed and standardized to lowercase; descriptors removed |
| `Region`       | String    | Country of origin for the recipe         | "China", "India", "Japan", "Malaysia", etc. | `Malaysia`             | Derived from the source site                              |
| `Recipe_ID`    | Integer   | Unique identifier for each recipe        | > 0                                         | `12345`                | Primary key                                               |
| `Recipe_Title` | String    | Title of the dish                        | Free text with standard capitalization      | `Chicken Tikka Masala` | Taken directly from recipe title                          |
| `Method`       | String    | Primary cooking method(s) for the recipe | "Boil", "Bake", "Fry", "Steam", etc.        | `Fry`                  | Scraped from instructions and standardized                |

**Uncertainties:**

* Ingredients may still include ambiguous terms and conflated descriptors.
* Additional parsing of cooking instructions is required to classify methods more accurately.

---


<img width="905" height="547" alt="image" src="https://github.com/user-attachments/assets/23be9355-0db6-44b6-aca3-da43b39468a1" />
<img width="996" height="600" alt="image" src="https://github.com/user-attachments/assets/8a3819b1-5036-4602-bf46-9935320f9dbe" />

