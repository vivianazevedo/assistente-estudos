from dotenv import load_dotenv
from google import genai 
from google.genai import types

load_dotenv() # importa a chave 

client = genai.Client() # objeto que conversa com servidores do google 

MODEL = "gemini-3.8-flash" # modelo de linguagem do google que vai gerar as respostas

SYSTEM_PADRAO = ("Você é um assistente de estudos para uma estudante de Sistemas de "
    "Informação. Explique de forma clara, com exemplos, em português.") #instrucoes gerais que definem o papel e jeito do modelo

def perguntar (pergunta: str, system: str = SYSTEM_PADRAO)-> str: 
    resposta = client.models.generate_content(
        model = MODEL, 
        contents = pergunta,
        config = types.GenerateContentConfig(system_instruction = system)
    )

    uso = resposta.usage_metadata #metadados de uso da API, como tokens usados e custo
    print (f"[tokens] entrada: {uso.prompt_token_count} |"
           f"saída: {uso.candidates_token_count}")

    return resposta.text 

