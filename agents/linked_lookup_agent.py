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
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo",)

    template = """given the full name {name_of_person} I want to get it me a link to their linkedin profile page.
    Your answer should contain only the url"""

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl google 4 linkedin profile page",
            func=tools.get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react", api_key=os.getenv("LANGSMITH_API_KEY"))

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__=="__main__":
    linkedin_url = lookup(name="Sanya Nanda jp morgan")
    print(linkedin_url)
