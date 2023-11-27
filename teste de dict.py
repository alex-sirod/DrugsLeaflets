# Dicionário original
original_dict = {
    'A': [
        ("02", "antiácidos, inibidores da secreção gástrica e tratamento das úlceras"),
        ("01", "preparados estomatológicos (boca e dentes)")
    ]
}

# Obtendo os valores desejados
result_dict = {key: [value[1].split(", ")[0] if len(value) > 1 else value[0] for value in values] for key, values in original_dict.items()}

# Exibindo o resultado
print(original_dict)
print(result_dict)
