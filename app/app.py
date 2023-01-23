import openai
import streamlit as st
import requests
import time

# api key
openai.api_key = st.secrets["api_key"]

# setup variables and containers

# streamlit setup
st.title("Grid App" )
st.info("A positioning framework for digital product development that uses natural language processing (davinci-003 model from OpenAI) and prompt engineering to generate product artifacts", icon="ℹ️")
st.header(":violet[Links]:link:")
st.markdown("**Documentation** : https://grid.sarantium.dev")
st.markdown("**Source** : https://github.com/sarantium/grid")
st.markdown("**App** : https://gridpm.streamlit.app")

# GRID
st.header(":violet[Grid Table]")

TABLE = """
The Grid is a positioning framework that is used in digital product development. It is represented in a table format, with a header row containing the letters A to N, and a header column containing the numbers 1 to 3. The cell representing the intersection of the header row and header column is left blank. Specifically, the table includes the following rows:

Row 1: Contains the following terms, which are repeated as indicated: philosophy (twice), scope (thrice), project (twice), growth (four times), maturity (twice), and decline (once).
Row 2: Contains the following terms: epistemology, methodology, vision, strategy, needs, structure, steering, discover, define, develop, deliver, research, improve, and end-of-life.
Row 3: Contains unique and distinct emojis that correspond to the concept represented by the corresponding cell in Row 2, which are intended to visually represent the stage and phase of the product development process and make it easy to understand. Use a wide variation of emojis. The emojis must not be repeated across any cells in Row 3.

Create a table in markdown format that represents the Grid framework as described above. 
"""

if st.button(label="generate", key=1, help="generates the grid table with contextually relevant icons for each column"):
    completions = openai.Completion.create(
        model= "text-davinci-003",
        prompt= TABLE,
        max_tokens= 3000,
        temperature= 0.9,
        top_p= 1,
        n= 1,
        stream= False,
        )

    response = completions.choices[0].text
    st.markdown(response)



# PERSONA
st.header(":violet[Widget 1 : User Persona Generator]:sunglasses:")
CONTEXT = st.text_area(
    label="Please describe the main **:red[problem]** your **:red[product or feature]** aims to solve for your **:red[target audience]**", 
    max_chars=200,
    placeholder="problem:  \nproduct or feature:  \ntarget audience:  \n")

# persona
PERSONA = """

Name: [Insert name of persona]

Demographics:
Age: [Insert age range]
Gender: [Insert gender]
Education level: [Insert education level]
Income level: [Insert income level and range]
Occupation: [Insert occupation and specific job title]
Location: [Insert location and specific city or region]
Family status: [Insert if the persona is single, married, with or without children and their ages if applicable]

Motivations and Goals: [Insert specific, measurable and achievable motivations and goals of the persona, including both short-term and long-term goals]
Pain Points: [Insert specific, measurable and achievable pain points of the persona that the product is intended to solve]

Behavioral Patterns:
Frequency of use: [Insert frequency of use and duration of use]
Preferred time of use: [Insert preferred time of use]
Preferred device: [Insert preferred device]
Technology proficiency: [Insert technology proficiency level]

Digital Habits:
Preferred social media platforms: [Insert preferred social media platforms]
Browsing habits: [Insert browsing habits]
Email usage: [Insert email usage habits]

Purchasing Habits and Behaviour:
Research process: [Insert how persona research products and services]
Purchase decision influencers: [Insert what factors influence their purchase decision]
Brand loyalty: [Insert brand loyalty level]
Decision-making process: [Insert decision-making process of the persona]

Social and Cultural Influences: [Insert social and cultural background]
Personal Characteristics: [Insert personality traits and characteristics that may influence behavior and decision-making]

Additional Information: [Insert any additional information about the persona that may be relevant to the product or service, such as hobbies, interests, or lifestyle habits]

Quotes or examples: [Insert any quotes or specific examples that may help to illustrate the persona's behavior, motivations, or pain points]

Images or avatars: [Insert any images or avatars that may help to visualize the persona, such as a stock photo or a drawing of the persona]

Key Takeaways: [Summarize the main characteristics, pain points, and goals of the persona in a few bullet points]

"""
INSTRUCTION = f"Generate a user persona using the User Persona Template - {PERSONA} - and the supplied product context - {CONTEXT}. Format the response in markdown using headers, bold and italics to make the text more readable"



#openai request and response
if st.button(label="generate", key=2, help="generates a user persona in about 10 seconds"):
    with st.spinner(":robot_face: is creating a persona"):
        time.sleep(3)
    
    placeholder = st.empty()
    placeholder.text("still working on it....5 seconds to go")
    
    completions = openai.Completion.create(
        model= "text-davinci-003",
        prompt= INSTRUCTION,
        max_tokens= 3000,
        temperature= 0.9,
        top_p= 1,
        n= 1,
        stream= False,
        )
    
    placeholder.empty()
    with st.spinner(":robot_face: almost done"):
        time.sleep(3)

    # display


    response = completions.choices[0].text

    st.subheader("**:violet[User Persona]**")
    st.markdown(response)

    st.balloons()
    
    

