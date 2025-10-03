# PhonePe-Transaction-Intelligence-Dashboard
The PhonePe Transaction Intelligence Dashboard is a data-driven platform that analyzes and visualizes digital payment trends across India. Built with PostgreSQL, Python, and Streamlit, it provides insights into transactions, insurance, and user engagement at state, district, and pincode levels. The dashboard supports customer segmentation, market strategies, and decision-making in the digital payments ecosystem.
# Framework:
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
Generate visualizations with Matplotlib, Seaborn, and Plotly:
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
streamlit run app.py in command prompt/powershell.

