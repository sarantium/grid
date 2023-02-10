import openai
import streamlit as st
import os

# api key
# openai.api_key = "-"

PROMPT = """
Create a comprehensive table in markdown format that outlines 10 opportunity-solution combinations for Mintscale as they integrate 
digital twin technology, blockchain, and the automotive sector to develop advanced products in South Africa and other African countries. 
The table should provide a comprehensive overview of each opportunity,, a solution, and a catchy name for the solution. 
Consider the unique challenges and opportunities in the African market, as well as cultural and technological differences. 
The target buyers are OEMs, , mechanical workshops, insurers and data aggregators.

"""

# completions = openai.Completion.create(
#     model= "text-davinci-003",
#     prompt= PROMPT,
#     max_tokens= 1000,
#     temperature= 0.9,
#     top_p= 1,
#     n= 1,
#     stream= False,
#     )

# print(completions.choices[0].text)

SECRETS_FILE_LOC = os.path.abspath(os.path.join("..", ".streamlit", "secrets.toml"))


print(st.secrets)
