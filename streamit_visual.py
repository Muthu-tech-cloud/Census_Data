
import streamlit as st
import pymysql
import pandas as pd


target_db = 'myDB'
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "1234"

def get_mysql_connection():
    return pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=target_db
    )

# Run the query and handle errors
def run_query(query):
    try:
        conn = get_mysql_connection()
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error running query: {str(e)}")
        return pd.DataFrame()  # Return empty dataframe in case of error

# Streamlit UI
def display_query_result():
    st.title("MySQL Query Results")
    
    # Dropdown to select the query
    query_type = st.selectbox(
        "Select the query you want to run:",
        [
            "Total Population by District",
            "Literate Males and Females by District",
            "Percentage of Workers by District",
            "Households with LPG or PNG by District",
            "Religious Composition by District",
            "Households with Internet Access by District",
            "Educational Attainment Distribution by District",
            "Households with Access to Transportation by District",
            "Condition of Census Houses by District",
            "Household Size Distribution by District",
        ]
    )

    # Define the queries
    if query_type == "Total Population by District":
        query = """
            SELECT district, SUM(population) AS total_population
            FROM census
            GROUP BY district;
        """
    elif query_type == "Literate Males and Females by District":
        query = """
            SELECT District, 
                SUM(Literate_Male) AS Total_Male_Literate,
                SUM(Literate_Female) AS Total_Female_Literate
            FROM census GROUP BY District;
        """
    elif query_type == "Percentage of Workers by District":
        query = """
            select District ,Population,Workers, (Workers * 100.0) / Population AS worker_percentage from census;
        """
    elif query_type == "Households with LPG or PNG by District":
        query = """
                select District , LPG_or_PNG_Households from census
                """
    elif query_type == "Religious Composition by District":
        query = """
                select District, Hindus,Muslims,Christians from census;
                """
    elif query_type == "Households with Internet Access by District":
        query = """
                select District,Households_with_Internet from census;
                """
    elif query_type == "Educational Attainment Distribution by District":
        query = """
                select District,Below_Primary_Education,Primary_Education,Middle_Education,Secondary_Education,Higher_Education,Graduate_Education,Other_Education,Illiterate_Education from census;
                """
    elif query_type == "Households with Access to Transportation by District":
        query = """
                select District,Households_with_Bicycle,Households_with_Car_Jeep_Van from census;
                """

    # Run the query and display results
    if st.button("Run Query"):
        result_df = run_query(query)
        if not result_df.empty:
            st.write(f"Query Result: {query_type}")
            st.dataframe(result_df)  # Display dataframe as a table
        else:
            st.write("No data found for the query.")

# Run Streamlit App
if __name__ == "__main__":
    display_query_result()
