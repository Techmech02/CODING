from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize the Chat Model
chat = ChatOpenAI(model_name="gpt-3.5-turbo")

# Create a conversation
messages = [HumanMessage(content="What is LangChain?")]
response = chat(messages)

# Print response
print(response.content)
