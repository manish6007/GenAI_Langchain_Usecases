import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
from langchain.schema import HumanMessage
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Streamlit app
st.title("Chat with CSV")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Save the file to /tmp folder
    file_path = os.path.join("/tmp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    st.write("File uploaded and read successfully!")

    # Display the DataFrame
    st.dataframe(df)

    # Create the LangChain agent
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, allow_dangerous_code=True)

    CSV_PROMPT_PREFIX = """
    First set the pandas display options to show all the columns,
    get the column names, then answer the question.
    """

    CSV_PROMPT_SUFFIX = """
    - **ALWAYS** before giving the Final Answer, try another method.
    Then reflect on the answers of the two methods you did and ask yourself
    if it answers correctly the original question.
    If you are not sure, try another method.
    - If the methods tried do not give the same result, reflect and
    try again until you have two methods that have the same result.
    - If you still cannot arrive to a consistent result, say that
    you are not sure of the answer.
    - If you are sure of the correct answer, create a beautiful
    and thorough response using Markdown.
    - **DO NOT MAKE UP AN ANSWER OR USE PRIOR KNOWLEDGE,
    ONLY USE THE RESULTS OF THE CALCULATIONS YOU HAVE DONE**.
    - **ALWAYS**, as part of your "Final Answer", explain how you got
    to the answer on a section that starts with: "\n\nExplanation:\n".
    In the explanation, mention the column names that you used to get
    to the final answer.
    """

    QUESTION = st.text_input("Enter your question about the data:", key="question_input")

    if st.button("Submit"):
        # Answer the question using the agent
        response = agent.run(CSV_PROMPT_PREFIX + QUESTION + CSV_PROMPT_SUFFIX)

        # Display the response
        st.markdown("### Response from LangChain Agent")
        st.markdown(response)
