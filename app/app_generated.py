import openai
import streamlit as st
import requests


# api key
openai.api_key = st.secrets["api_key"]

# initialise lists to store prompts and generated outputs
prompts: list[str|None] = []
generated_outputs: list[str|None] = []

# function to check for internet connection
def check_internet() -> bool:
    try:
        # attempt to connect to google.com
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# function to check for valid API key
def check_api_key(api_key: str) -> bool:
    openai.api_key = api_key
    try:
        # attempt to get models list using the provided key
        models = openai.Model.list()
        return True
    except openai.OpenAIError:
        return False

def main():
    st.title("OpenAI Text Generator")
    st.info("Enter your OpenAI API key and select a model to generate text.")

    # get API key from user
    api_key = st.text_input("API Key")
    if not check_api_key(api_key):
        st.error("Invalid API key. Please check and try again.")
        return

    # get model options
    models = openai.Model.list()
    davinci = "text-davinci-003"
    model_options = sorted([model.id for model in models['data']])
    model_options.remove(davinci)
    model_options.insert(0, davinci)
    model = st.selectbox("Select a model", model_options)

    # get prompt from user
    prompt = st.text_area("Enter prompt") or st.file_uploader("Upload prompt file")
    prompts.append(prompt)

    # get temperature, token limit, number of outputs, and language from user
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    token_limit = st.number_input("Token limit", value=2048, min_value=1)
    num_outputs = st.number_input("Number of outputs", value=1, min_value=1)
    language = st.text_input("Language (optional)")

    # get output format and additional context from user
    output_format = st.selectbox("Output format", ["text", "html"])
    additional_context = st.text_input("Additional context (optional)")

    if st.button("Generate"):
        if not check_internet():
            st.error("No internet connection. Please check and try again.")
            return
        
        # # create a progress bar
        # progress_bar = st.progress(0)
        # total_steps = 5
        # step = 0
        # progress_bar.progress(step)

        # use OpenAI API to generate output
        completions = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=token_limit,
            n=num_outputs,
            stop=language,
            format=output_format,
            context=additional_context
        )
        # step += 1
        # progress_bar.progress(step / total_steps)
        generated_output = completions.choices[0].text
        # generated_outputs.append(generated_output)
        # step += 1
        # progress_bar.progress(step / total_steps)

        # display generated output
        st.write("Generated output:")
        if output_format == "html":
            st.write(st.html(generated_output))
        else:
            st.write(generated_output)

    # # option to save output to file
    # save_output = st.checkbox("Save output to file")
    # if save_output:
    #     file_name = st.text_input("Enter file name")
    #     if file_name:
    #         with open(file_name, "w") as f:
    #             f.write(generated_output)
    #         st.success("Output saved to file.")
    #     else:
    #         st.error("Please enter a file name.")

#     # option to share output via email or social media
#     share_output = st.checkbox("Share output")
#     if share_output:
#         share_options = ["Email", "Facebook", "Twitter"]
#         share_choice = st.selectbox("Select a sharing option", share_options)
#         if share_choice == "Email":
#             recipient_email = st.text_input("Enter recipient email")
#             message = st.text_area("Enter message (optional)")
#             # code to send email with the generated output
#             st.success("Email sent!")
#         elif share_choice == "Facebook":
#             # code to share on Facebook
#             st.success("Shared on Facebook!")
#         elif share_choice == "Twitter":
#             # code to share on Twitter
#             st.success("Shared on Twitter!")
            
#     step += 1
#     progress_bar.progress(step / total_steps)
    
# # option to view previous outputs
# if st.button("View previous outputs"):
#     previous_outputs = st.selectbox("Select output", generated_outputs)
#     st.write("Previous output:")
#     st.write(previous_outputs)
# step += 1
# progress_bar.progress(step / total_steps)
# # option to clear lists
# if st.button("Clear lists"):
#     prompts.clear()
#     generated_outputs.clear()
#     st.success("Lists cleared.")
# step += 1
# progress_bar.progress(step / total_steps)
# # option to edit previous inputs
# if st.button("Edit previous inputs"):
#     previous_prompt = st.selectbox("Select prompt", prompts)
#     new_prompt = st.text_area("Edit prompt", previous_prompt)
#     prompt_index = prompts.index(previous_prompt)
#     prompts[prompt_index] = new_prompt
#     st.success("Prompt edited.")




if __name__ == "__main__":
    main()