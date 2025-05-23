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

## Refactoring & Modularity Improvements

To enhance code reusability, clarity, and maintainability across all EDA notebooks, the following refactoring steps were implemented:

- **Utility Module Creation:**
  - A shared `utils.py` file was created in the `notebooks/` directory.
  - This module contains reusable functions for data loading (`load_data`), cleaning (`clean_data`), saving cleaned data (`save_clean_data`), and common plotting routines (`plot_time_series`, `plot_monthly_boxplots`, `plot_hourly_trends`).

- **Consistent Data Access:**
  - All data loading and saving operations use the `data/` folder as the base directory, so only filenames are needed in client code.

- **Notebook Refactoring:**
  - Each country-specific notebook (`benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb`) now imports and uses these utility functions.
  - Data loading, cleaning, and saving are performed via the shared utilities, reducing code duplication.
  - Plotting of time series, monthly boxplots, and hourly trends is handled by the modular plotting functions.

- **Improved Summary Statistics:**
  - The summary statistics section in each notebook now excludes the `Timestamp` column from categorical (object) column descriptions, ensuring only relevant columns are summarized.

- **Scalability:**
  - This modular approach makes it easy to extend or update the analysis for new datasets or additional EDA steps, as changes only need to be made in the utility module.

These improvements support a more robust, maintainable, and scalable workflow for solar data analysis and reporting.

## Comprehensive Cross-Country Analysis Enhancements (2025)

To provide deeper insights and more robust recommendations for solar installation, the cross-country analysis was significantly enhanced:

- **Advanced Statistical Analysis:**
  - Added Levene's test for homogeneity of variance across countries.
  - Performed pairwise t-tests and Mann-Whitney U tests for GHI between all country pairs.
  - Included both parametric (ANOVA) and non-parametric (Kruskal–Wallis) tests for group comparisons.

- **Rich Visualizations:**
  - Added KDE (density) and violin plots for GHI, DNI, and DHI to visualize the full distribution for each country.
  - Monthly GHI trends are now compared across countries in a single plot.
  - Bar charts and boxplots provide clear visual summaries of key metrics.

- **Regional and Temporal Insights:**
  - Top regions/sites by average GHI are identified and compared for each country.
  - Monthly and regional trends are highlighted to support location-specific recommendations.

- **Strategic Recommendations:**
  - The notebook concludes with actionable, data-driven recommendations for optimal solar installation locations, based on the enhanced analysis.

- **Modular, Maintainable Code:**
  - All data loading and utility functions are imported from a shared `notebooks/utils.py` module, ensuring consistency and reusability.
  - The code is structured for easy extension with new metrics, tests, or visualizations.

These improvements make the analysis more comprehensive, statistically robust, and actionable for decision-makers in solar energy planning.
