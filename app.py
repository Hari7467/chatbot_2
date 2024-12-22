## import libraries
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
##streamlit
st.title("CHATBOT USING GEMMA2:9B:IT AND GROQ API")
st.write("plaese Enter your groq api key to pull the model")
st.write("if you don't have api key go groq.com and get api")
groq_api_key=st.text_input("ENTER YOUR API KEY")
if groq_api_key:
    user_input=st.text_input("HOW CAN I HELP WITH YOU?")
    ##Pull the model using groq api
    model=ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)
    ##define stroutput parser to extraxt the actual content from ai message
    parser=StrOutputParser()
    ##using LCEL and prompt template to interact with chatbot
    generic_template = "{operation}"
    prompt = ChatPromptTemplate.from_template(generic_template)
    chain=prompt|model|parser
    if user_input:
        messages = prompt.format(operation=user_input)
        result=chain.invoke(messages)
        st.write(result)

