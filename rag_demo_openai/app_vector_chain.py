from vector_chain import get_results, get_direct_results
import streamlit as st
import logging

# Configure
st.set_page_config(layout='wide')
placeholder = st.empty()
emoji_feedback = st.empty()
user_placeholder = st.empty()

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
      {"role": "ai", "content": f"This chatbot is powered by OpenAI + Neo4j. It uses only vector indexes"}, 
    ]

# Display chat messages from history on app rerun
with placeholder.container():
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

user_input = st.chat_input(placeholder="Ask questions regarding the source data", key="user_input")

# Whenever there's user input - display it in chat history and get bot response
if user_input:
  with user_placeholder.container():
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
      st.markdown(user_input)

    with st.chat_message("ai"):

      with st.spinner('...'):

        message_placeholder = st.empty()
        thought_container = st.container()

        # Response generation
        content = get_results(user_input)

        new_message = {"role": "ai", "content": content}
        st.session_state.messages.append(new_message)

      message_placeholder.markdown(content)