import os
import json
import base64
import gzip
from datetime import datetime

# Caminho raiz do seu projeto Django
projeto = "C:/Users/eduar/Documents/PycharmProjects/Pycharmforms/Portfolio"  # <-- altere aqui

# Extensões de texto
ext_texto = ('.html', '.css', '.js', '.txt', '.py')

# Extensões binárias
ext_binario = ('.svg', '.jpg', '.jpeg', '.pyc')

arquivos = []

for raiz, dirs, files in os.walk(projeto):
    for nome in files:
        caminho = os.path.join(raiz, nome)
        caminho_relativo = os.path.relpath(caminho, projeto)
        ext = os.path.splitext(nome)[1].lower()

        # Metadados
        stat = os.stat(caminho)
        tamanho_bytes = stat.st_size
        data_modificacao = datetime.fromtimestamp(stat.st_mtime).isoformat()

        # Leitura
        if ext in ext_texto:
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                arquivos.append({
                    "path": caminho_relativo,
                    "type": ext[1:],
                    "encoding": "utf-8",
                    "size_bytes": tamanho_bytes,
                    "modified_at": data_modificacao,
                    "content": conteudo
                })
            except Exception as e:
                arquivos.append({
                    "path": caminho_relativo,
                    "type": ext[1:],
                    "encoding": "error",
                    "size_bytes": tamanho_bytes,
                    "modified_at": data_modificacao,
                    "content": f"[ERRO AO LER ARQUIVO: {e}]"
                })

        elif ext in ext_binario:
            try:
                with open(caminho, 'rb') as f:
                    dados = f.read()
                conteudo_b64 = base64.b64encode(dados).decode('utf-8')
                arquivos.append({
                    "path": caminho_relativo,
                    "type": ext[1:],
                    "encoding": "base64",
                    "size_bytes": tamanho_bytes,
                    "modified_at": data_modificacao,
                    "content": conteudo_b64
                })
            except Exception as e:
                arquivos.append({
                    "path": caminho_relativo,
                    "type": ext[1:],
                    "encoding": "error",
                    "size_bytes": tamanho_bytes,
                    "modified_at": data_modificacao,
                    "content": f"[ERRO AO LER ARQUIVO: {e}]"
                })

saida = {
    "project_name": os.path.basename(projeto),
    "root_path": projeto,
    "exported_at": datetime.now().isoformat(),
    "files": arquivos
}

# JSON sem espaços extras
json_compacto = json.dumps(saida, ensure_ascii=False, separators=(',', ':')).encode("utf-8")

# Tamanho máximo por parte (5 MB)
MAX_SIZE = 5 * 1024 * 1024  

if len(json_compacto) <= MAX_SIZE:
    # Compacta em um único arquivo .gz
    with gzip.open("projeto_django_unificado.json.gz", "wb") as f:
        f.write(json_compacto)
    print("✅ Arquivo único 'projeto_django_unificado.json.gz' gerado com sucesso!")
else:
    # Divide em partes
    partes = (len(json_compacto) // MAX_SIZE) + 1
    for i in range(partes):
        inicio = i * MAX_SIZE
        fim = inicio + MAX_SIZE
        parte_bytes = json_compacto[inicio:fim]
        nome_arquivo = f"projeto_django_parte_{i+1}.json.gz"
        with gzip.open(nome_arquivo, "wb") as f:
            f.write(parte_bytes)
        print(f"✅ Arquivo '{nome_arquivo}' gerado com sucesso ({len(parte_bytes)} bytes)")


