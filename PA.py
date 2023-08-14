# Imports
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Headerrr Perron
st.header("Data Rebels Project Assistant 😎")

course =  st.radio("Selecciona tu curso", ("Python Fundamentals", "Data Product Owner", "Data Translator"))

kind_of_text =  st.radio("Selecciona una opcion a evaluar", ("Problematica", "Proyecto"))

# Lets let the user decide how creative the model must be 
creatividad = st.slider("Define el nivel de creatividad con el que quieres que genere la propuesta de proyecto!", 0.0, 1.0, 0.0, step=0.1)
# Setting the API key (We using chatgpt)
llm = OpenAI(openai_api_key="key", temperature=creatividad)

# We let the input
data = st.text_input(f"Introduce la descripcion de tu {kind_of_text}", placeholder="Filtrado automatico de datos y egenracion de KPI's")

# Courses description
python_fundamentals = "Fundamentos de Python, aprenden de forma basica Streamlit, Pandas, Numpy, Openpyxl, ciclos, y POO"
data_product_owner = ""

# Courses dictionary
courses_dictionary = {"Python Fundamentals" : python_fundamentals}

# Create the prompt templates
promtp_proyect_definition = PromptTemplate(
    input_variables=["course", "data"],
    template="Escribe una idea de proyecto extremadamente viable y facil de hacer, con una defincion de alcance, que pueda ser construido aplicando los siguientes conocimientos:{course}, para cumplir el siguiente objetivo: {data}. Explica como se puede inetgrar cada tecnologia al proyecto."
    )
promtp_problem_solving = PromptTemplate(
    input_variables=["course", "data"],
    template="Escribe una idea de proyecto extremadamente viable y facil de hacer, que pueda ser construido aplicando los siguientes conocimientos:{course}, para resolver la siguiente problematica: {data}. Explica como se puede inetgrar cada tecnologia al proyecto.")


# Creating the chains
proyect_chain  = LLMChain(llm=llm, prompt=promtp_proyect_definition, verbose=True, output_key="ideas")
problem_chain = LLMChain(llm=llm, prompt=promtp_problem_solving, output_key="ideas", verbose=True)


# Numero de ideas por generar # Depreciaaado
# n_ideas = st.number_input(label="Ingresa el numero de ideas a generar",  min_value=1, max_value=10, value=2)

if st.button("Generar"):
    with st.spinner("Creando ideas..."):
        if kind_of_text== "Proyecto":
            ideas = proyect_chain.run(course=courses_dictionary[course], data=data)
            st.header("🤖Ideas de proyecto (Generadas por AI)")
            st.write(ideas)
            print(ideas)
        else:
            ideas = problem_chain.run(course=courses_dictionary[course], data=data)
            st.header("🤖Ideas de proyecto (Generadas por AI)")
            st.write(ideas)
    st.success("🔥")