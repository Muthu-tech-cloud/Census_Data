# Census Data Standardization and Analysis Pipeline

## 🧩 Project Overview
This project aims to clean, standardize, and analyze census data for accurate storage, querying, and visualization. It includes handling missing data, formatting inconsistencies, state reorganization, and storing data in both MongoDB and a relational database. Insights are visualized using Streamlit.

---

#Technologies Used
- Python
- Pandas
- SQL (MySQL)
- MongoDB
- Streamlit


# Task 1: Column Renaming
Standardized inconsistent column names for clarity and uniformity across datasets.

# Task 2: State/UT Name Standardization
Converted names to Title Case and replaced symbols like "&" with "and".

# Task 3: New State/UT Formation
Handled formation of Telangana (2014) and Ladakh (2019) by updating district mappings.

# Task 4: Missing Data Handling
- Calculated missing data percentage.
- Filled missing values using logical formulas (e.g., `Population = Male + Female`).
- Compared missing data before and after processing.

# Task 5: MongoDB Integration
Stored cleaned dataset in MongoDB under collection `census`.

# Task 6: SQL Database Upload
Fetched data from MongoDB and uploaded to a relational database with appropriate constraints.

# Task 7: Streamlit Dashboard
Executed queries on SQL and visualized insights:
- Population and literacy by district
- Worker and household statistics
- Education, religion, transport & income distribution



