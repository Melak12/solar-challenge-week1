# Solar Challenge Week 1
A project for learning Git and CI/CD.

## Setup
1. Clone: `git clone https://github.com/Melak12/solar-challenge-week1.git`
2. Create venv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`

## Streamlit Dashboard

This project includes an interactive dashboard for visualizing solar data insights using Streamlit.

### Development Process
- The dashboard is implemented in `app/main.py` using Streamlit and Altair for interactive visualizations.
- Utility functions for data loading and processing are in `app/utils.py`.
- Data files are located in the `data/` directory.
- The dashboard allows users to select a country, view boxplots of GHI by region, see the top regions by average GHI, and filter data interactively.

### Usage Instructions

1. **Activate the virtual environment:**
   ```cmd
   .venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**
   ```cmd
   cd app
   streamlit run main.py
   ```
4. **Open the dashboard:**
   - The app will open in your default browser. If not, visit the URL shown in the terminal (usually http://localhost:8501).

### Features
- Country selection sidebar
- Boxplot of GHI by region (top 10 regions)
- Table of top 5 regions by average GHI
- Interactive slider to filter data by GHI range

