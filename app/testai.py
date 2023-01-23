import openai
import streamlit as st

# api key
openai.api_key = st.secrets["api_key"]

PROMPT = """
The Grid is a positioning framework that is used in digital product development. It is represented in a table format, with a header row containing the letters A to N, and a header column containing the numbers 1 to 3. The table is divided into multiple rows, each containing different information that is relevant to the product development process. Specifically, the table includes the following rows:

Row 1: Contains the following terms, which are repeated as indicated: philosophy (twice), scope (thrice), project (twice), growth (four times), maturity (twice), and decline (once).
Row 2: Contains the following terms: epistemology, methodology, vision, strategy, needs, structure, steering, discover, define, develop, deliver, research, improve, and end-of-life.
Row 3: Contains unique and distinct emojis that correspond to the concept represented by the corresponding cell in Row 2, which are intended to visually represent the stage and phase of the product development process and make it easy to understand. Use a wide variation of emojis. The emojis must not be repeated across any cells in Row 3.

Create a table in markdown format that represents the Grid framework as described above.

"""

completions = openai.Completion.create(
    model= "text-davinci-003",
    prompt= PROMPT,
    max_tokens= 200,
    temperature= 0.9,
    top_p= 1,
    n= 1,
    stream= False,
    )

print(completions.choices[0].text)


