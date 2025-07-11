from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(model="gpt-4.1", temperature=0)

    prompt = ChatPromptTemplate.from_template(
        "{input} has a LinkedIn profile, you need to find it. Only return the URL!")

    chain = prompt | llm | StrOutputParser()

    tools_for_agent_serach = [
        Tool(
            name="Crawl Google 4 LinkedIn profile",
            func=get_profile_url_tavily,
            description="Search Google for a person's LinkedIn profile URL"
        )
    ]

    react_prommp = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent_serach,
        prompt=react_prommp
    )
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tools_for_agent_serach, verbose=True)

    result = agent_executor.invoke({"input": name})

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup("Jennifer (Halabi) Cole work in Sendbird ")
    print(linkedin_url)
