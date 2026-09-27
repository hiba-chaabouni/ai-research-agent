import wikipedia
wikipedia.set_user_agent("AIAgentTutorial/1.0 (educational project; hibac@example.com)")

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_ollama import ChatOllama
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    

llm = ChatOllama(model="llama3.2:1b")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
                (
            "system",
            """
            You are a helpful research assistant.
            Use the available tools when you need information from the web or Wikipedia.
            Give clear, useful answers. 
            If you use tools, base your final answer on the information they return.
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=6
)

# ========== GRADIO CHAT INTERFACE ==========
import gradio as gr
from datetime import datetime

def save_answer(query: str, answer: str):
    """Automatically save every answer to research_output.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n"
        f"Question: {query}\n\n"
        f"{answer}\n\n"
        f"{'='*60}\n\n"
    )
    with open("research_output.txt", "a", encoding="utf-8") as f:
        f.write(formatted_text)


def chat_with_agent(message, history):
    try:
        raw_response = agent_executor.invoke({"query": message})
        output = raw_response.get("output", "")

        # Clean the output
        if isinstance(output, list):
            texts = []
            for item in output:
                if isinstance(item, dict) and "text" in item:
                    texts.append(item["text"])
                else:
                    texts.append(str(item))
            final_answer = "\n".join(texts)
        else:
            final_answer = str(output)

        # Automatically save every answer
        save_answer(message, final_answer)

        return final_answer

    except Exception as e:
        error_msg = f"Sorry, I ran into an error: {str(e)}"
        save_answer(message, error_msg)  # even save errors
        return error_msg


demo = gr.ChatInterface(
    fn=chat_with_agent,
    title="Research Agent 🤖",
    description="Ask me anything — I research and automatically save every answer.",
    examples=[
        "What makes a great CV?",
        "Explain quantum computing simply",
        "Best countries for data analytics internships"
    ]
)

if __name__ == "__main__":
    demo.launch()