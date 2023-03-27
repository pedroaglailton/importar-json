import json

# Define as chaves que queremos extrair do arquivo JSON
keys_to_extract = ["color", "ocrText", "category", "make", "view"]

# Define o nome do arquivo de entrada e do arquivo de saída
input_file = "placas.json"
output_file = "resultado.json"

# Lê o arquivo de entrada
with open(input_file, "r") as f:
    data = json.load(f)

# Extrai apenas as informações desejadas
extracted_data = []
for item in data:
    tags = item.get("tags", [])
    for tag in tags:
        extracted_item = {}
        extracted_item["color"] = tag.get("color", "")
        extracted_item["ocrText"] = tag.get("anprResult", {}).get("ocrText", "")
        extracted_item["category"] = tag.get("mmrResult", {}).get("category", "")
        extracted_item["make"] = ""
        extracted_item["view"] = tag.get("mmrResult", {}).get("view", "")
        extracted_data.append(extracted_item)

# Salva as informações extraídas em um novo arquivo JSON
with open(output_file, "w") as f:
    json.dump(extracted_data, f)
