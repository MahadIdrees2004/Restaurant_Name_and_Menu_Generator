import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0.2)

def generate_restaurant_and_menu(cuisine: str):
   
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest 3 to 4 unique and fancy restaurant names for {cuisine} food. Return only the names, each on a new line."
    )
    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="restaurant_names")
    name_result = name_chain.invoke({"cuisine": cuisine})

    # Prompt for menu
    menu_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest a short, delicious menu for a {cuisine} restaurant. Return comma-separated items only."
    )
    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu")
    menu_result = menu_chain.invoke({"cuisine": cuisine})

    return {
        "restaurant_names": name_result["restaurant_names"],
        "menu": menu_result["menu"]
    }
