
import os

from dotenv import load_dotenv

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SequentialChain

load_dotenv()


KEY = os.getenv("open_api_key")

# os.environ['OPENAI_API_KEY'] = open_api_key

# chain = LLMChain(llm=llm,prompt = prompt_name)

def generate_restaurant(cuisine):
    llm = OpenAI(temperature=0.6,openai_api_key = KEY)
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template="""I want to open {cuisine} restaurant . Suggest me the good names"""
    )
    chain = LLMChain(llm=llm, prompt=prompt_name, output_key='restaurant_name')

    food_name = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest me the menu items for {restaurant_name} """
    )
    food_chain = LLMChain(llm=llm, prompt=food_name, output_key='menu')

    seq_chain = SequentialChain(chains=[chain, food_chain],
                                input_variables=['cuisine'],
                                output_variables=['restaurant_name', 'menu']
                                )

    response  = seq_chain({'cuisine': cuisine})

    return response


# if name == '__main__':
#     print(generate_restaurant('Indian'))
