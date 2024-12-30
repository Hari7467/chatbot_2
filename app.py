import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
## Chatprompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a useful assistant.please respond to the user queries."),
        ("user","Guestion:{question}")
    ]
)

def generate_response(question,api_key,temperature,llm,max_tokens):
    llm=ChatGroq(model=llm,api_key=api_key)
    str_parser=StrOutputParser()
    chain=prompt|llm|str_parser
    answer=chain.invoke({"question":question})
    return answer

##Tittle of the chatbot
st.title("Enhance Q&A chatbot using open source model")

## sidebar for settings
st.sidebar.title("settings")
api_key=st.sidebar.text_input("Enter your qroq api key:",type="password")

##Drop to select varoius llm models
llm=st.sidebar.selectbox("Select models:",["gemma2-9b-it","llama-3.3-70b-versatile","llama3-8b-8192","llama3-70b-8192"])

##adjust response parameter
temperature=st.sidebar.slider("Temperature:",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens:",min_value=50,max_value=300,value=150)

## Main Interface user Input
st.write("Go ahead and Ask any questions:")
user_input=st.text_input("you:")

if user_input:
    response=generate_response(user_input,api_key,temperature,llm,max_tokens)
    st.write(response)
else:
    st.write("Please ask any questions")
