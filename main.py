from src.llm import perguntar 


def main(): 
    while True: 
        pergunta_usuario = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if pergunta_usuario.lower() == 'sair':
            break
        resposta = perguntar(pergunta_usuario)
        print(f" \n Resposta: {resposta}\n")

if __name__ == "__main__":
    main()