#-------------------------------------------install useful library 
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
#----------------------------------------page title 
st.set_page_config(page_title="KP Chatgpt", page_icon="🤖", initial_sidebar_state="expanded")
#-----------------------------------remove hidden streamlit made 
hide_streamlit_style = """
            <style>
            #footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#------------------------------------------------sidebar written 
with st.sidebar:
    st.title('''       😎 KP Chatgpt 🤖        ''')
    st.markdown("------------------")
    option = "About"
    st.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.markdown('''
     Kundeshwar V. Pundalik believes that KP Chatgpt has the potential to revolutionize various industries, such as customer service, education, and entertainment.This app is an LLM-powered chatgpt built using:
    - [Source](<https://github.com/kundeshwar/kp_chatgpt>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(4)
    st.write('Made with ❤️ by Kundeshwar Pundalik 😍')
#-------------------------------------for main body 
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm KP, How may I help you?"]
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi kp!']

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

#-------------------------------------------
# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

#----------------------------------------------Calling to hugechat function 
# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response
#----------------------------------------------input and output setting 
## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))

