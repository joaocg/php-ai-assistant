# PHP AI Assistant com Starcoder

Uma aplicação open source que **analisa o padrão de um projeto PHP**, gera novos códigos seguindo esses padrões e sugere melhorias/refatorações usando IA (modelo Starcoder).

Feito para rodar localmente em Ubuntu ou Linux, mesmo sem GPU dedicada (roda em CPU, só que mais lento).


## Funcionalidades

- Analisa projetos PHP e detecta padrões (ex.: namespace, estrutura de pastas)
- Gera novos arquivos PHP seguindo o mesmo padrão
- Sugere melhorias e refatorações para arquivos PHP existentes
- Interface web simples e em português, feita com Streamlit


## Tecnologias usadas

- [Starcoder](https://huggingface.co/bigcode/starcoder) – modelo de linguagem open source para código
- Python + transformers
- Streamlit (interface web)


## Estrutura do projeto

```plaintext
php-ai-assistant/
├── app/
│   ├── analyzer.py          # Lê padrões do projeto PHP
│   ├── generator.py        # Gera novos códigos PHP seguindo os padrões
│   └── improver.py         # Sugere melhorias em códigos PHP
├── webapp/
│   └── app.py              # Interface web (em português)
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```


## Como instalar e rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/php-ai-assistant.git
cd php-ai-assistant
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
streamlit run webapp/app.py
```

---

## Como funciona

1.  **Analisa o projeto PHP**
- Lê nomes de namespaces, pastas, nomes de classes
- Detecta o padrão principal do projeto

2. **Gera novos arquivos PHP**
- Exemplo: "Gerar um Controller para produto"
- O assistente cria um prompt e pede ao modelo gerar código seguindo o padrão

3. **Sugere melhorias**
- Faça upload de um arquivo PHP
- O assistente mostra sugestões de refatoração e boas práticas


## Observação
- O Starcoder é grande e pode ser lento para rodar só na CPU
- Se quiser performance, use uma GPU dedicada (NVIDIA)
- É um projeto didático para explorar uso de IA open source em PHP


## Melhorias futuras

- Detectar mais padrões do projeto
- Melhor interface web
- Gerar testes automáticos
- Rodar outros modelos de código além do Starcoder


## Licença
MIT
