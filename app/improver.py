def sugerir_melhorias_php(codigo_php):
    prompt = f"""Revise o seguinte código PHP e sugira melhorias seguindo boas práticas:
```php
{codigo_php}
```"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=300)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
