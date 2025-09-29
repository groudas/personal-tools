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
        response_text = call_gemma("""<instruções> 1) Elabore um raciocínio rápido acerca da pergunta 2) Responda sim ou não com o seguinte formato: [[sim]] / [[não]] </instruções>\n\n<alerta>Aviso de: Ventos Costeiros\nGrau de severidade: Perigo\nInício: 26/09/2025 01h00min\nFim: 28/09/2025 10h00min\nRiscos Potenciais:\nINMET publica aviso iniciando em: 26/09/2025 01:00. Intensificação dos ventos nas regiões litorâneas, movimentando dunas de areia sobre construções na orla..\n\nInstruções:\nContate a Defesa Civil (telefone: 199).\nMunicípios:\nArambaré - RS (4300851), Araranguá - SC (4201406), Arroio do Sal - RS (4301057), Arroio Grande - RS (4301305), Balneário Arroio do Silva - SC (4201950), Balneário Gaivota - SC (4202073), Balneário Pin...\n\nÁreas Afetadas:\nMetropolitana de Porto Alegre, Sul Catarinense, Sudeste Rio-grandense\n</alerta>\n\n<pergunta>Este alerta é do grau de severidade "Perigo" ou "Grande Perigo"?</pergunta>""")
        print(response_text)
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
