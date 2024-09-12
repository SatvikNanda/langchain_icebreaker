import os
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools import tools
from dotenv import load_dotenv

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """Given the full name {name_of_person}, find and return the link to their LinkedIn profile page.
    Your answer should contain only the URL."""

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl google for LinkedIn profile page",
            func=tools.get_profile_url_tavily,
            description="Useful for finding the LinkedIn Page URL for a given person",
        )
    ]

    # Retrieve the prompt from Langchain hub using API key
    react_prompt = hub.pull("hwchase17/react", api_key=os.getenv("LANGSMITH_API_KEY"))

    # Create the agent
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    # Debug: Check formatted prompt
    formatted_prompt = prompt_template.format_prompt(name_of_person=name)
    print(f"Formatted prompt: {formatted_prompt}")

    # Invoke the agent and get the result
    result = agent_executor.invoke(
        input={"input": formatted_prompt}
    )

    # Debug: Check full result
    print(f"Full result: {result}")

    # Extract LinkedIn profile URL
    linkedin_profile_url = result.get("output")  # Make sure "output" exists
    if not linkedin_profile_url:
        raise ValueError("No output found in result, please check the result structure.")

    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = lookup(name="Sanya Nanda")
    print(f"LinkedIn Profile URL: {linkedin_url}")
