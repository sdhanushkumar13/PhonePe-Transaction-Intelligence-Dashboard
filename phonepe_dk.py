import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
import pandas as pd
import plotly.express as px
import requests
import json


# Dataframe Creation

# sql connection

mydb = psycopg2.connect(host= "localhost",
                        user = "postgres",
                         port = "5432",
                          database = "Ppe_data",
                           password = "root" )

cursor = mydb.cursor()

#aggregated_transaction_dataframe

cursor.execute("SELECT * FROM aggregated_transaction")
mydb.commit()
Table1 = cursor.fetchall()

A_transaction = pd.DataFrame(Table1, columns = ("States", "Years", "Quarter", "Transaction_type",
                                                "Transaction_count", "Transaction_amount" ))

#aggregated_insurance_dataframe

cursor.execute("SELECT * FROM aggregated_insurance")
mydb.commit()
Table2 = cursor.fetchall()

A_insurance = pd.DataFrame(Table2, columns = ("States", "Years", "Quarter", "Transaction_type",
                                                "Transaction_count", "Transaction_amount" ))

#aggregated_user_dataframe

cursor.execute("SELECT * FROM aggregated_user")
mydb.commit()
Table3 = cursor.fetchall()

A_user = pd.DataFrame(Table3, columns = ("States", "Years", "Quarter", "Brands",
                                                "Transaction_count", "Percentage" ))

#map_transaction_dataframe

cursor.execute("SELECT * FROM map_transaction")
mydb.commit()
Table4 = cursor.fetchall()

M_transaction = pd.DataFrame(Table4, columns = ("States", "Years", "Quarter", "Districts",
                                                "Transaction_count", "Transaction_amount" ))

#map_insurance_dataframe

cursor.execute("SELECT * FROM map_insurance")
mydb.commit()
Table5 = cursor.fetchall()

M_insurance = pd.DataFrame(Table5, columns = ("States", "Years", "Quarter", "Districts",
                                                "Transaction_count", "Transaction_amount" ))

#map_user_dataframe

cursor.execute("SELECT * FROM map_user")
mydb.commit()
Table6 = cursor.fetchall()

M_user = pd.DataFrame(Table6, columns = ("States", "Years", "Quarter", "Districts",
                                                "RegisteredUsers", "AppOpens" ))

#top_transaction_dataframe

cursor.execute("SELECT * FROM top_transaction")
mydb.commit()
Table7 = cursor.fetchall()

T_transaction = pd.DataFrame(Table7, columns = ("States", "Years", "Quarter", "Pincodes",
                                                "Transaction_count", "Transaction_amount" ))

#top_insurance_dataframe

cursor.execute("SELECT * FROM top_insurance")
mydb.commit()
Table8 = cursor.fetchall()

T_insurance = pd.DataFrame(Table8, columns = ("States", "Years", "Quarter", "Pincodes",
                                                "Transaction_count", "Transaction_amount" ))

#top_user_dataframe

cursor.execute("SELECT * FROM top_user")
mydb.commit()
Table9 = cursor.fetchall()

T_user = pd.DataFrame(Table9, columns = ("States", "Years", "Quarter", "Pincodes",
                                                "RegisteredUsers" ))


## Functions

def transaction_amount_count_Y(df, year):

    if str(year) == "All":
         tacy = df[df["Years"] == year]
         tacy.reset_index(drop=True, inplace=True)
         
         tacy_group = tacy.groupby("States")[["Transaction_count",
                                               "Transaction_amount"]].sum()
         tacy_group.reset_index(inplace=True)
         title_suffix = "All Years"

    else :
        year == int(year)
        tacy = df[df["Years"] == year]
        tacy.reset_index(drop=True, inplace=True)
         
        tacy_group = tacy.groupby("States")[["Transaction_count",
                                               "Transaction_amount"]].sum()
        tacy_group.reset_index(inplace=True)
        title_suffix = f"{year}"

    #tacy = df[df["Years"] == year]
    #tacy.reset_index(drop=True, inplace=True)

    #tacy_group = tacy.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    #tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
    
        fig_amount0 = px.bar(tacy_group, x="States", y= "Transaction_amount", 
                            title= f"{year} - TRANSACTION AMOUNT", 
                            color_discrete_sequence= px.colors.sequential.Bluered, 
                            height= 600, width= 500)
        st.plotly_chart(fig_amount0)

    with col2:

        fig_count0 = px.bar(tacy_group, x="States", y= "Transaction_count", 
                           title= f"{year} - TRANSACTION COUNT", 
                           color_discrete_sequence= px.colors.sequential.BuGn_r, 
                           height= 600, width= 500)
        st.plotly_chart(fig_count0)


    col1,col2 = st.columns(2)
    with col1:
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data1 = json.loads(response.content)

        states_name = []
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])
        states_name.sort()

        fig_india_1 = px.choropleth(tacy_group, geojson=data1, locations="States", 
                                    featureidkey="properties.ST_NM", 
                                    color="Transaction_amount", 
                                    color_continuous_scale="Rainbow", 
                                    range_color=(tacy_group["Transaction_amount"].min(), tacy_group["Transaction_amount"].max()), 
                                    hover_name= "States", title=f"{year} - TRANSACTION AMOUNT", fitbounds= "locations", 
                                    height= 600, width= 600)
    
        fig_india_1.update_geos(visible=False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth(tacy_group, geojson=data1, locations="States", 
                                    featureidkey="properties.ST_NM", 
                                    color="Transaction_count", 
                                    color_continuous_scale="Rainbow", 
                                    range_color=(tacy_group["Transaction_count"].min(), tacy_group["Transaction_count"].max()), 
                                    hover_name= "States", title=f"{year} - TRANSACTION COUNT", fitbounds= "locations", 
                                    height= 600, width= 600)
    
        fig_india_2.update_geos(visible=False)
        st.plotly_chart(fig_india_2)


    return tacy

def transaction_amount_count_Y_Q(df, quarter):

    tacy = df[df["Quarter"] == quarter]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)

    with col1:    
        fig_amount = px.bar(tacy_group, x="States", y= "Transaction_amount", title= f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Bluered)
        st.plotly_chart(fig_amount)

    with col2:    
        fig_count = px.bar(tacy_group, x="States", y= "Transaction_count", title= f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.BuGn_r)
        st.plotly_chart(fig_count)

    col1,col2 = st.columns(2)

    with col1:
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data1 = json.loads(response.content)

        states_name = []
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])
        states_name.sort()

        fig_india_1 = px.choropleth(tacy_group, geojson=data1, locations="States", 
                                    featureidkey="properties.ST_NM", 
                                    color="Transaction_amount", 
                                    color_continuous_scale="Rainbow", 
                                    range_color=(tacy_group["Transaction_amount"].min(), tacy_group["Transaction_amount"].max()), 
                                    hover_name= "States", title=f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION AMOUNT", fitbounds= "locations", 
                                    height= 600, width= 600)
    
        fig_india_1.update_geos(visible=False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth(tacy_group, geojson=data1, locations="States", 
                                    featureidkey="properties.ST_NM", 
                                    color="Transaction_count", 
                                    color_continuous_scale="Rainbow", 
                                    range_color=(tacy_group["Transaction_count"].min(), tacy_group["Transaction_count"].max()), 
                                    hover_name= "States", title=f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION COUNT", fitbounds= "locations", 
                                    height= 600, width= 600)
    
        fig_india_2.update_geos(visible=False)
        st.plotly_chart(fig_india_2)

    return tacy

def Agg_tran_type(df, state):


    tacy = df[df["States"] == state]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("Transaction_type")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_pie_1 = px.pie(data_frame= tacy_group, names= "Transaction_type", values= "Transaction_amount",
                                width= 600, title= f"{df['Years'].min()} {state.upper()} - TRANSACTION AMOUNT", hole= 0.5,)
        st.plotly_chart(fig_pie_1)

    with col2:
        fig_pie_2 = px.pie(data_frame= tacy_group, names= "Transaction_type", values= "Transaction_count",
                                width= 600, title= f"{df['Years'].min()} {state.upper()} - TRANSACTION COUNT", hole= 0.5,)
        st.plotly_chart(fig_pie_2)

def Agg_user_plot_1(df, year):
    A_user_Y  = df[df["Years"] == year]
    A_user_Y.reset_index(drop= True, inplace= True)

    A_user_Y_group = pd.DataFrame(A_user_Y.groupby("Brands")["Transaction_count"].sum())
    A_user_Y_group.reset_index(inplace=True)

    fig_bar_1 = px.bar(A_user_Y_group, x= "Brands", y= "Transaction_count",
                    title= f"{year} - BRANDS AND TRANSACTION COUNT", width= 800, color_discrete_sequence= px.colors.sequential.Blues_r,
                    hover_name= "Brands")

    st.plotly_chart(fig_bar_1)

    return A_user_Y

def Agg_user_plot_2(df, quarter):

    A_user_Y_Q  = df[df["Quarter"] == quarter]
    A_user_Y_Q.reset_index(drop= True, inplace= True)

    A_user_Y_Q_group = pd.DataFrame(A_user_Y_Q.groupby("Brands")["Transaction_count"].sum()) 
    A_user_Y_Q_group.reset_index(inplace=True)


    fig_bar_2 = px.bar(A_user_Y_Q_group, x= "Brands", y= "Transaction_count",
                        title= f"{df['Years'].min()} QUARTER {quarter} - BRANDS AND TRANSACTION COUNT", width= 800, 
                        color_discrete_sequence= px.colors.sequential.Blues_r, hover_name= "Brands")

    st.plotly_chart(fig_bar_2)

    return A_user_Y_Q

def Agg_user_plot_3(df, state):
    Agg_user_Y_Q_S = df[df["States"] == state]
    Agg_user_Y_Q_S.reset_index(drop=True, inplace=True)

    fig_line_3 = px.line(Agg_user_Y_Q_S, x= "Brands", y= "Transaction_count", hover_data= "Percentage",
                        title= f"{df['Years'].min()} {state.upper()} QUARTER {df['Quarter'].min()} - BRANDS, TRANSACTION COUNT AND PERCENTAGE ", width=1000, markers=True)

    st.plotly_chart(fig_line_3)

def Map_insu_Districts(df, state):

    tacy = df[df["States"] == state]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("Districts")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        fig_bar_1 = px.bar(tacy_group, x= "Transaction_amount", y= "Districts", orientation = "h", height = 800,
                                title= f"{state.upper()} - DISTRICTS AND TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Agsunset_r)
        st.plotly_chart(fig_bar_1)
    with col2:
        fig_bar_2 = px.bar(tacy_group, x= "Transaction_count", y= "Districts", orientation = "h", height = 800,
                                title= f"{state.upper()} -  DISTRICTS AND TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.Burgyl_r)
        
        st.plotly_chart(fig_bar_2)

def map_user_plot_1(df,year):

    M_user_Y  = df[df["Years"] == year]
    M_user_Y.reset_index(drop= True, inplace= True)

    M_user_Y_group = M_user_Y.groupby("States")[["RegisteredUsers", "AppOpens"]].sum()
    M_user_Y_group.reset_index(inplace=True)

    fig_line_4 = px.line(M_user_Y_group, x= "States", y= ["RegisteredUsers", "AppOpens"],
                        title= f" {year} - REGISTERED USERS AND APPOPENS ", width=1000, height = 800, markers=True)

    st.plotly_chart(fig_line_4)

    return M_user_Y

def map_user_plot_2(df,quarter):

    M_user_Y_Q  = df[df["Quarter"] == quarter]
    M_user_Y_Q.reset_index(drop= True, inplace= True)

    M_user_Y_Q_group = M_user_Y_Q.groupby("States")[["RegisteredUsers", "AppOpens"]].sum()
    M_user_Y_Q_group.reset_index(inplace=True)

    fig_line_5 = px.line(M_user_Y_Q_group, x= "States", y= ["RegisteredUsers", "AppOpens"],
                        title= f"{df['Years'].min()} QUARTER {quarter} - REGISTERED USERS AND APPOPENS ", width=1000, 
                        height = 800, markers=True, color_discrete_sequence= px.colors.sequential.Rainbow_r)

    st.plotly_chart(fig_line_5)

    return M_user_Y_Q

def map_user_plot_3(df,state):
    M_user_Y_Q_S  = df[df["States"] == state]
    M_user_Y_Q_S.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        Fig_map_user_bar_1 = px.bar(M_user_Y_Q_S, x= "RegisteredUsers", y= "Districts",
                                    orientation= "h", title= f"{df['Years'].min()} QUARTER {df['Quarter'].min()} {state.upper()} DISTRICTS - REGISTERED USER",
                                    height= 800, color_discrete_sequence= px.colors.sequential.haline_r)

        st.plotly_chart(Fig_map_user_bar_1)

    with col2:
        Fig_map_user_bar_2 = px.bar(M_user_Y_Q_S, x= "AppOpens", y= "Districts",
                                    orientation= "h", title= f"{df['Years'].min()} QUARTER {df['Quarter'].min()} {state.upper()} DISTRICTS - APPOPENS",
                                    height= 800, color_discrete_sequence= px.colors.sequential.Magenta_r)

        st.plotly_chart(Fig_map_user_bar_2)

def top_ins_plot_1(df,state):
    T_ins_Y  = df[df["States"] == state]
    T_ins_Y.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_top_ins_bar_1 = px.bar(T_ins_Y, x= "Quarter", y= "Transaction_amount", hover_data= "Pincodes",
                                title= f"{df['Years'].min()} YEAR's TRANSACTION AMOUNT", height= 800, color_discrete_sequence= px.colors.sequential.Purpor_r)

        st.plotly_chart(fig_top_ins_bar_1)

    with col2:
        fig_top_ins_bar_2 = px.bar(T_ins_Y, x= "Quarter", y= "Transaction_count", hover_data= "Pincodes",
                                title= f"{df['Years'].min()} YEAR's TRANSACTION COUNT", height= 800, color_discrete_sequence= px.colors.sequential.Cividis_r)

        st.plotly_chart(fig_top_ins_bar_2)

def top_user_plot_1(df,year):
    T_user_Y  = df[df["Years"] == year]
    T_user_Y.reset_index(drop= True, inplace= True)

    T_user_Y_group = pd.DataFrame(T_user_Y.groupby(["States", "Quarter"])["RegisteredUsers"].sum())
    T_user_Y_group.reset_index(inplace=True)

    fig_top_user_plot_1 = px.bar(T_user_Y_group, x= "States", y= "RegisteredUsers", color= "Quarter",
                            width= 1000, height= 800, color_discrete_sequence = px.colors.sequential.Bluered_r,
                            hover_name= "States", title= f"{year} REGISTERED USERS")

    st.plotly_chart(fig_top_user_plot_1)

    return T_user_Y

def top_user_plot_2(df,state):
    T_user_Y_S = df[df["States"] == state]
    T_user_Y_S.reset_index(drop= True, inplace= True)

    fig_top_user_plot_2 = px.bar(T_user_Y_S, x= "Quarter", y= "RegisteredUsers",
                                title = "REGISTERED USERS, PINCODES, QUARTER",
                                width= 1000, height= 800, color= "RegisteredUsers", hover_data= "Pincodes",
                                color_continuous_scale= px.colors.sequential.Magenta_r)

    st.plotly_chart(fig_top_user_plot_2)


# Streamlit Part

st.set_page_config(layout= "wide")
st.markdown("<h1 style='text-align:center; margin:0;'>PHONEPE TRANSACTION INTELLIGENCE DASHBOARD</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Full-page watermark layer */
    .watermark-layer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;            /* allow clicks through the watermark */
      z-index: 0;                       /* sit behind page content (which we'll raise) */
      display: block;
      background-image: url("https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png");
      background-repeat: no-repeat;
      background-position: right 20px top 10px; /* position: right-top; tweak offsets */
      background-size: var(--logo-width, 220px) auto; /* width in px; keep aspect ratio */
      opacity: var(--logo-opacity, 0.2);  /* transparency (0.0 - 1.0) */
      filter: none;                        /* optional: blur(1px) or grayscale(1) */
    }

    /* Ensure your actual content appears above watermark */
    .stApp > .main, .css-1outpf7, .block-container {
      position: relative;
      z-index: 1;
    }

    </style>
    <div class="watermark-layer"></div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='page-title'></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:left; padding-top:5px; padding-bottom:10px;">
            <img src="https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    select = option_menu("MENU", ["HOME", "BUSINESS CASES"])

    st.markdown(
        """
        <style>
        .sidebar-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: inherit;
            text-align: center;
            font-size: 18px;
            color: grey;
            padding-bottom: 10px;
        }
        </style>
        <div class="sidebar-footer">
            PROJECT BY — <b>DHANUSHKUMAR S</b>
        </div>
        """,
        unsafe_allow_html=True
    )

if select == "HOME":
    
    st.markdown("""
    Welcome! This interactive dashboard presents a comprehensive analysis of PhonePe’s transaction, user, and insurance datasets. It is built to help stakeholders understand the evolution of India’s digital payment ecosystem, assess adoption patterns, and identify strategic opportunities in a rapidly expanding financial technology landscape.""")
    st.markdown("### Project Context ")
    st.markdown("""
    India’s digital payment ecosystem has transformed dramatically over the past decade, primarily driven by the Unified Payments Interface (UPI). Among the key players, PhonePe has emerged as a market leader, facilitating billions of transactions every month. Understanding these trends is critical for:  
    \n**Domain:** Finance / Digital Payments.
    \n**Product teams:** to design services tailored to user behavior.
    \n**Marketing teams:** to identify high-growth regions and adoption barriers.
    \n**Operations teams:** to mitigate risks and optimize resource allocation.
    \nThis dashboard consolidates analytical frameworks from digital finance, consumer behavior, and economic geography with empirical data from PhonePe, enabling data-backed decision-making.""")
    st.markdown("### Core Deliverables")
    st.markdown("""
    - Provides a macro-level perspective of India’s payment ecosystem.
    - Helps predict future adoption trajectories for both payments and insurance.
    - Supports policy and regulatory discussions around digital finance penetration.
    - Acts as a knowledge base for practitioners, researchers, and policymakers.""")


elif select == "BUSINESS CASES" :

    col1,col2,col3 = st.columns(3)
    with col2:
        st.markdown("<h5 style='text-align: center;'>Select Case Study</h5>", unsafe_allow_html=True)
        cases = st.selectbox("", ["Decoding Transaction Dynamics on PhonePe",
                                  "Device Dominance and User Engagement Analysis",
                                    "Transaction Analysis for Market Expansion", 
                                    "Insurance Engagement Analysis",
                                    "User Engagement and Growth Strategy" ])
        
    if cases == "Decoding Transaction Dynamics on PhonePe":
        st.subheader("The Big Picture: Yearly Transaction Insights")
        col1,col2 = st.columns(2)
        with col1:
            years = st.selectbox("Select Year", A_transaction["Years"].unique(), index=0)
        Agg_tran_tac_y = transaction_amount_count_Y(A_transaction, years)

        st.subheader("Decoding Statewise Transaction Types — Yearly Lens")
        col1,col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State",Agg_tran_tac_y["States"].unique())
        Agg_tran_type(Agg_tran_tac_y, states)  

        st.subheader("Quarterly Pulse of the Year")  
        col1,col2 = st.columns(2)
        with col1:
            quarters = st.slider("Select Quarter", Agg_tran_tac_y["Quarter"].min(), Agg_tran_tac_y["Quarter"].max(), Agg_tran_tac_y["Quarter"].min())
        Agg_tran_tac_y_Q = transaction_amount_count_Y_Q(Agg_tran_tac_y, quarters)
        col1,col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select a State to View Quarterly Breakdown",Agg_tran_tac_y_Q["States"].unique())
        Agg_tran_type(Agg_tran_tac_y_Q, states)


    elif cases == "Device Dominance and User Engagement Analysis":
        
        st.subheader("Brand Dominance")
        col1,col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", A_user["Years"].min(), A_user["Years"].max(), A_user["Years"].min())
        A_user_y = Agg_user_plot_1(A_user, years)
        with col2:
            quarters = st.slider("Select Quarter", A_user_y["Quarter"].min(), A_user_y["Quarter"].max(), A_user_y["Quarter"].min())
        A_user_y_Q = Agg_user_plot_2(A_user_y, quarters)

        st.subheader("Engagement Gap")
        col1,col2 = st.columns(2)
        with col1:
            Map_user_Y = map_user_plot_1(M_user, years)
        with col2:
            Map_user_Y_Q = map_user_plot_2(Map_user_Y, quarters)

        st.subheader("Regional Variation in Device Usage & Engagement")
        col1,col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State",A_user_y_Q["States"].unique())
        Agg_user_plot_3(A_user_y_Q, states)
        map_user_plot_3(Map_user_Y_Q, states)


    elif cases == "Transaction Analysis for Market Expansion":
        st.subheader("Annual View")
        col1,col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_transaction["Years"].min(), M_transaction["Years"].max(), M_transaction["Years"].min())
        Map_tran_tac_y = transaction_amount_count_Y(M_transaction, years)
        col1,col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State",Map_tran_tac_y["States"].unique())
        Map_insu_Districts(Map_tran_tac_y, states)

        st.subheader("Quarterly View")
        col1,col2 = st.columns(2)
        with col1:
            quarters = st.slider("Select Quarter", Map_tran_tac_y["Quarter"].min(), Map_tran_tac_y["Quarter"].max(), Map_tran_tac_y["Quarter"].min())
        Map_tran_tac_y_Q = transaction_amount_count_Y_Q(Map_tran_tac_y, quarters)
        Map_insu_Districts(Map_tran_tac_y_Q, states)
        
        
    elif cases == "Insurance Engagement Analysis":
        st.subheader("Annual View")
        col1,col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_insurance["Years"].min(), M_insurance["Years"].max(), M_insurance["Years"].min())
        Map_insu_tac_y = transaction_amount_count_Y(M_insurance, years)
        col1,col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State",Map_insu_tac_y["States"].unique())
        Map_insu_Districts(Map_insu_tac_y, states) 

        st.subheader("Quarterly View")
        col1,col2 = st.columns(2)
        with col1:
            quarters = st.slider("Select Quarter", Map_insu_tac_y["Quarter"].min(), Map_insu_tac_y["Quarter"].max(), Map_insu_tac_y["Quarter"].min())
        Map_insu_tac_y_Q = transaction_amount_count_Y_Q(Map_insu_tac_y, quarters)
        Map_insu_Districts(Map_insu_tac_y_Q, states)


    elif cases == "User Engagement and Growth Strategy":

        st.subheader("Engagement Overview")
        col1,col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_user["Years"].min(), M_user["Years"].max(), M_user["Years"].min())
            Map_user_Y = map_user_plot_1(M_user, years)
        with col2:
            quarters = st.slider("Select Quarter", Map_user_Y["Quarter"].min(), Map_user_Y["Quarter"].max(), Map_user_Y["Quarter"].min())
            Map_user_Y_Q = map_user_plot_2(Map_user_Y, quarters)

        st.subheader("Regional Engagement")
        states = st.selectbox("Select State",Map_user_Y_Q["States"].unique())
        map_user_plot_3(Map_user_Y_Q, states)
        


