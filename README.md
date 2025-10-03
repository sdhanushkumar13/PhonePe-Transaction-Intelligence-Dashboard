# PhonePe-Transaction-Intelligence-Dashboard
The PhonePe Transaction Intelligence Dashboard is a data-driven platform that analyzes and visualizes digital payment trends across India. Built with PostgreSQL, Python, and Streamlit, it provides insights into transactions, insurance, and user engagement at state, district, and pincode levels. The dashboard supports customer segmentation, market strategies, and decision-making in the digital payments ecosystem.
# Project Framework:
## Data Extraction
Clone the GitHub repository containing PhonePe transaction datasets.
Load the data into a SQL database for structured analysis.
## SQL Database & Table Creation
Set up a relational database using PostgreSQL.
Create tables to organize data:
Aggregated Tables
aggregated_user → user-related data
aggregated_transaction → aggregated transaction data
aggregated_insurance → insurance-related data
Map Tables
map_user → mapping user data
map_map → mapping values for states & districts
map_insurance → mapping insurance data
Top Tables
top_user → top users
top_map → top states, districts, pincodes
top_insurance → top insurance categories
## Data Analysis (Business Case Studies) with Python
Use Pandas for data manipulation.
Generate visualizations with Plotly:
Bar Charts → transaction/insurance volumes
Pie Charts → category distributions
Line Charts → user engagement trends
Choropleth Maps → state/district-level insights
## Dashboard Creation
Build an interactive Streamlit dashboard integrating SQL + Python outputs.
Provide filters (Year, Quarter, State, District, Category).
Enable real-time exploration of:
Transaction trends
Insurance adoption
User growth and device engagement
## Run the app
streamlit run [filename].py in command prompt/powershell.

# Python Framework:
Step 1 → Importing Libraries:
Begin by importing the required Python libraries such as pandas, psycopg2, plotly, requests, and streamlit to handle data extraction, analysis, visualization, and dashboard creation.
Step 2 → DataFrame Creation:
Establish a SQL connection to the PostgreSQL database and retrieve records from the created tables. The extracted data is then converted into pandas DataFrames for structured manipulation and analysis.
Step 3 → Function Development:
Define custom Python functions that operate on the DataFrames to perform aggregations, filtering, and calculations. These functions generate intermediate results and prepare data for meaningful insights and visualization.
Step 4 → Dashboard Development:
Build an interactive Streamlit dashboard to integrate the results and visualizations. The dashboard allows users to explore transactions, insurance, and user trends dynamically through filters, plots, and maps.

# Notes:
The dashboard addresses five key business cases, each designed to extract actionable insights from PhonePe transaction data:
→ Decoding Transaction Dynamics
→ Device Dominance and User Engagement
→ Transaction Analysis for Market Expansion
→ Insurance Engagement Analysis
→ User Engagement and Growth Strategy
Each case study is analyzed through SQL queries, Python functions, and interactive visualizations in Streamlit, enabling stakeholders to interpret trends effectively.
