from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = [
    """
    You are an expert to converting English questions to SQL query !
    The SQL database has the name STUDENT and has the following columns -  NAME,CLASS,
    SECTIONS \n\nFor example,\nExample 1- How many entries of records are present ?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2- Tell me all teh students studying in BCS4C?,The SQL command will be something like 
    this SELECT *FROM STUDENT  where CLASS = 'BCS4C';
    also the SQL code shoudl not have ''' in teh beginning or end and sql word in output
    
    """

]

st.set_page_config(page_title="SQL easier app")
st.header("Gemini app to Retrieve SQL Data")

question = st.text_input("ask the information: ", key="input")
submit = st.button("Ask Question")

# if submit clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The SQL query is ")

    st.header(response)
    print(response)
    response = read_sql_query(response, "student.db")
    print(response)
    st.subheader("The response is ")
    for row in response:
        print(row)
        st.header(row)
