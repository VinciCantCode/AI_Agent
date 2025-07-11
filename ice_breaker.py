import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

print("API Key loaded successfully")
information = """ Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who is the 47th president of the United States. A member of the Republican Party, he served as the 45th president from 2017 to 2021.

Born into a wealthy family in New York City, Trump graduated from the University of Pennsylvania in 1968 with a bachelor's degree in economics. He became the president of his family's real estate business in 1971, renamed it the Trump Organization, and began acquiring and building skyscrapers, hotels, casinos, and golf courses. He launched side ventures, many licensing the Trump name, and filed for six business bankruptcies in the 1990s and 2000s. From 2004 to 2015, he hosted the reality television show The Apprentice, bolstering his fame as a billionaire. Presenting himself as a political outsider, Trump won the 2016 presidential election against Democratic Party nominee Hillary Clinton.

During his first presidency, Trump imposed a travel ban on seven Muslim-majority countries and enforced a family separation policy on the border. He rolled back environmental and business regulations, signed the Tax Cuts and Jobs Act, and appointed three Supreme Court justices. In foreign policy, Trump withdrew the U.S. from agreements on climate, trade, and Iran's nuclear program, and initiated a trade war with China. In response to the COVID-19 pandemic from 2020, he downplayed its severity, contradicted health officials, and signed the CARES Act. After losing the 2020 presidential election to Joe Biden, Trump attempted to overturn the result, culminating in the January 6 Capitol attack in 2021. He was impeached in 2019 for abuse of power and obstruction of Congress, and in 2021 for incitement of insurrection; the Senate acquitted him both times.

In 2023, Trump was found liable in civil cases for sexual abuse and defamation and for business fraud. He was found guilty of falsifying business records in 2024, making him the first U.S. president convicted of a felony. After winning the 2024 presidential election against Kamala Harris, he was sentenced to a penalty-free discharge, and two felony indictments against him for retention of classified documents and obstruction of the 2020 election were dismissed without prejudice. A racketeering case related to the 2020 election in Georgia is pending.

Trump began his second presidency by initiating mass layoffs of federal workers. He imposed tariffs on nearly all countries, including large tariffs on China, Canada, and Mexico. His administration's actions—including intimidation of political opponents and civil society, deportations of immigrants, and extensive use of executive orders—have drawn over 300 lawsuits challenging their legality. High-profile cases have underscored his broad interpretation of the unitary executive theory and have led to significant conflicts with the federal courts.

Trump is the central figure of Trumpism, and his faction is dominant within the Republican Party. Many of his comments and actions have been characterized as racist or misogynistic, and he has made false and misleading statements and promoted conspiracy theories to a degree unprecedented in American politics. Trump's actions, especially in his second term, have been described as authoritarian and contributing to democratic backsliding. After his first term, scholars and historians ranked him as one of the worst presidents in American history.
"""

if __name__ == "__main__":

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        3. His birthday
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
llm = ChatOllama(model="llama3", temperature=0.8)

chain = summary_prompt_template | llm

result = chain.invoke(input={"information": information})

print("\n" + "=" * 50)
print("AI Generated Summary Result:")
print("=" * 50)
print(result.content)
print("=" * 50)
print(f"Total tokens used: {result.response_metadata['token_usage']['total_tokens']}")
print(f"Input tokens: {result.response_metadata['token_usage']['prompt_tokens']}")
print(f"Output tokens: {result.response_metadata['token_usage']['completion_tokens']}")
print("=" * 50)
