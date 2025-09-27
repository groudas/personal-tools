import os
from google import generativeai as genai

# Atribua a API com o seguinte comando: $env:API_KEY="YOUR_API_KEY"
genai.configure(api_key=os.environ["API_KEY"]) # <-- Adicionado o parêntese de fechamento aqui

def call_gemma(prompt: str, model_name: str = "gemma-3-27b-it", temperature: float = 0.7) -> str:
    # ... código existente da função ...
    if prompt is None:
        raise ValueError("Prompt inexistente.")
    model = genai.GenerativeModel(model_name=model_name)

    # Use generate_content with generation_config for temperature
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(temperature=temperature)
    )
    return response.text

if __name__ == "__main__":
    # Esta parte só será executada quando o script for rodado diretamente
    # Você pode colocar aqui a chamada para o argparse ou uma chamada de teste
    try:
        # Exemplo de chamada de teste:
        response_text = call_gemma("Explique a teoria da relatividade de forma simples.")
        print(response_text)
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")