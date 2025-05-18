## Data Profiling, Cleaning & EDA Process

The following steps were performed for each country dataset as documented in the Jupyter notebooks in the `notebooks/` directory:

1. **Data Profiling:**
   - Loaded raw CSV files for each country (Benin, Sierra Leone, Togo).
   - Inspected data types, missing values, and summary statistics.
   - Identified key columns such as timestamps, region/site/location, and GHI (Global Horizontal Irradiance).

2. **Data Cleaning:**
   - Handled missing or anomalous values (e.g., removed or imputed NaNs, filtered outliers).
   - Standardized column names and formats for consistency across datasets.
   - Converted date/time columns to appropriate datetime formats.
   - Saved cleaned datasets as `*_clean.csv` in the `data/` directory for use in the dashboard.

3. **Exploratory Data Analysis (EDA):**
   - Visualized distributions of GHI and other relevant variables.
   - Explored temporal patterns (e.g., daily, monthly trends).
   - Compared GHI across different regions/sites within each country.
   - Identified top-performing regions/sites based on average GHI.

The results of these steps are available in the respective notebooks:
- `benin_eda.ipynb`
- `sierraleone_eda.ipynb`
- `togo_eda.ipynb`
- `compare_countries.ipynb` (for cross-country comparisons)

The cleaned data produced from this process powers the interactive Streamlit dashboard in this project.

---
