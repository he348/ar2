import fitz  # PyMuPDF
from spellchecker import SpellChecker

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai texto de um arquivo PDF.

    Parâmetros:
    - caminho_pdf (str): O caminho do arquivo PDF.

    Retorna:
    - str: O texto extraído do PDF, ou None em caso de erro.
    """
    texto = ""
    try:
        with fitz.open(caminho_pdf) as pdf_documento:
            for pagina_num in range(pdf_documento.page_count):
                pagina = pdf_documento[pagina_num]
                texto += pagina.get_text()
        return texto
    except FileNotFoundError:
        print(f"Erro: Arquivo PDF não encontrado em '{caminho_pdf}'")
        return None
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return None

def corrigir_ortografia(texto, idioma='pt'):
    """
    Corrige a ortografia de um texto.

    Parâmetros:
    - texto (str): O texto a ser corrigido.
    - idioma (str): O idioma do texto (padrão é 'pt' para português).

    Retorna:
    - str: O texto corrigido.
    """
    corretor = SpellChecker(language=idioma)
    palavras = texto.split()
    palavras_corrigidas = []
    for palavra in palavras:
        if palavra.isalpha():  # Verifica se é uma palavra (ignora pontuação)
            palavra_corrigida = corretor.correction(palavra)
            if palavra_corrigida:
                palavras_corrigidas.append(palavra_corrigida)
            else:
                palavras_corrigidas.append(palavra)  # Mantém a palavra original se não houver correção
        else:
            palavras_corrigidas.append(palavra)  # Mantém palavras não alfabéticas
    return ' '.join(palavras_corrigidas)

def salvar_texto_em_txt(texto, caminho_txt):
    """
    Salva um texto em um arquivo TXT.

    Parâmetros:
    - texto (str): O texto a ser salvo.
    - caminho_txt (str): O caminho para salvar o arquivo TXT.
    """
    try:
        with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
            arquivo_txt.write(texto)
        print(f"Texto salvo com sucesso em '{caminho_txt}'")
    except Exception as e:
        print(f"Erro ao salvar texto em TXT: {e}")

if __name__ == "__main__":
    # Instruções de execução:
    # 1. Certifique-se de ter o Python 3.x instalado.
    # 2. Instale as bibliotecas PyMuPDF e pyspellchecker usando pip:
    #    pip install pymupdf pyspellchecker
    # 3. Execute o script a partir da linha de comando:
    #    python nome_do_script.py
    # 4. O script solicitará o caminho do arquivo PDF e o caminho para salvar o arquivo TXT.

    caminho_pdf = input("Digite o caminho do arquivo PDF: ")
    caminho_txt = input("Digite o caminho para salvar o arquivo TXT: ")

    texto_extraido = extrair_texto_pdf(caminho_pdf)

    if texto_extraido:
        texto_corrigido = corrigir_ortografia(texto_extraido)
        salvar_texto_em_txt(texto_corrigido, caminho_txt)