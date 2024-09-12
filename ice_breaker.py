from typing import Tuple
from agents.linked_lookup_agent import lookup as linkedin_lookup_agent
from custom_chains import (
    get_summary_chain,
    get_interests_chain,
    get_ice_breaker_chain,
)
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import (
    Summary,
    IceBreaker,
    TopicOfInterest,
)
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
#from langchain_ollama import ChatOllama // just an alternate option
from langchain_core.output_parsers import StrOutputParser



import os


def ice_break_with(name: str) -> Tuple[Summary, TopicOfInterest, IceBreaker, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(Linkedin_profile_url=linkedin_username)

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data},
    )

    interests_chain = get_interests_chain()
    interests: TopicOfInterest = interests_chain.invoke(
        input={"information": linkedin_data}
    )

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers: IceBreaker = ice_breaker_chain.invoke(
        input={"information": linkedin_data}
    )
    #print(summary_and_facts)
    return (
        summary_and_facts,
        interests,
        ice_breakers,
        linkedin_data.get("profile_pic_url"),
    )

    # summary_template = """
    # given the Linkedin information {information} about a person, I want you to create:
    # 1. a short summary
    # 2. two interesting facts about them
    # \n{format_instructions}
    # """

    # summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
    #                                          partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
    # #llm = ChatOllama(model="llama3")

    # chain = summary_prompt_template | llm | summary_parser
    # #linkedin_data = scrape_linkedin_profile(Linkedin_profile_url="https://www.linkedin.com/in/sanya-nanda-aba12218b/", mock=True)

    # res:Summary = chain.invoke(input={"information":linkedin_data})
    
    # return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Ice breaker Enter")
    ice_break_with(name="Satvik Nanda")

    

    