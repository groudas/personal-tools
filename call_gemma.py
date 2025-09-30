import os
from google import genai
from google.genai import types

# Atribua a API com o seguinte comando: $env:API_KEY="YOUR_API_KEY"
client = genai.Client(api_key=os.environ["API_KEY"])

def call_gemma(prompt: str, model_name: str = "gemma-3-27b-it", temperature: float = 0.7) -> str:
    if prompt is None:
        raise ValueError("Prompt inexistente.")

    # Use generate_content com config para temperature
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=temperature)
    )
    return response.text

if __name__ == "__main__":
    try:
        # Exemplo de chamada de teste:
        response_text = call_gemma("""<notícia 1>
idRegistro	Data	Hora	Link	Resumo	Município	Relevância	Conteúdo
1	29/09/25	22:13:00	https://xxx.com	Ponte pega fogo	Goiania		Ponte pega fogo pela manhã
</notícia 1>
<notícia 2>
idRegistro	Data	Hora	Link	Resumo	Município	Relevância	Conteúdo
2	29/09/25	09:12:00	https://yyy.com	Acidente derruba ponte	Goiania		Caminhão incendia ponte e a derruba
</notícia 2>
<instruções>
A partir destas duas notícias, crie um novo registro conforme o seguinte schema JSON:
* idEvento: Identificador único do evento.
* idRegistro originários: Lista dos IDs de registros que deram origem a este evento.
* Data Inicial: Data do primeiro registro associado.
* Hora Inicial: Hora do primeiro registro associado.
* Links registros originários: Lista dos links dos registros originais.
* Resumo: Resumo consolidado do evento.
* Município: Município principal do evento.
</instruções>""")
        print(response_text)
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
