import os
import re

def analisar_projeto_php(caminho):
    padroes = {}
    for raiz, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo.endswith('.php'):
                with open(os.path.join(raiz, arquivo), 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()
                    ns = re.findall(r'namespace\s+([^\s;]+);', conteudo)
                    if ns:
                        padroes['namespace'] = ns[0]
    return padroes
