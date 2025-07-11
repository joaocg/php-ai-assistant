from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def gerar_codigo_php(padroes, descricao):
    prompt = f"""No projeto, usamos namespace {padroes.get('namespace', 'App\\Default')}.
Gere um novo código PHP para: {descricao}"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=300)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
