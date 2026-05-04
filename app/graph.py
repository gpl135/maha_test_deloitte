# =====================================
# Thi is the implementation of Chatbot
# =====================================  

from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_openai import ChatOpenAI


# Prompt
CHAT_PROMPT = """
You are a helpful AI assistant.

User: {input}
Assistant:
"""

# State
class ChatState(TypedDict):
    input: str
    output: str
    
# Create LLM 
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Chatbot Node
def chatbot_node(state):
    user_input = state["input"]

    prompt = CHAT_PROMPT.format(input=user_input)

    response = llm.invoke(prompt)

    return {"output": response.content}


def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("chatbot", chatbot_node)

    graph.set_entry_point("chatbot")
    graph.add_edge("chatbot", END)
    

    return graph.compile()
