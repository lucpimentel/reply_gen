import openai
import streamlit as st
from auxfunctions import openai_api_call


st.title('Welcome to The Tweet Reply Generator!')

api_key = st.text_input('Insert your OpenAI API key:')

tweet = st.text_input('Insert the Tweet you want to reply to:')


reply_type = st.selectbox('Reply type:',
             ['Adding new similar thoughts','Supportive','Appreciative','Insightful','Thoughtful','Agreeable','Conclusive','Disagreeable','Empathetic','Fake Personal Story'],
             index=0)


tone = st.selectbox('Tone of voice:',
                    ['Neutral', 'Curious','Empathic','Conclusive','Uplifting', 'Casual Yet Formal', 'Cheerful', 'Upbeat', 'Formal', 'Disrespectful'],
                    index=0)


openai.api_key = api_key


prompt = f'''You are an expert twitter reply generator, I will provide you with a tweet and your job is to come up with a reply to it.
Here is the tweet in double brackets I want you to reply for me: [[{tweet}]]
Now create a {reply_type} reply for me using a {tone} tone:'''



generate_reply_button = st.button("Generate Tweet Reply",)


# Create a button to call the function
if generate_reply_button:
    with st.spinner("Loading..."):
        reply = openai_api_call(prompt,0.7)
        st.text_area('Tweet Reply:', reply, height=200)
        generate_reply_button = False
