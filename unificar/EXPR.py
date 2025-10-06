import os
import json

# Caminho raiz do seu projeto Django
# Exemplo: "/home/usuario/meu_projeto_django"
projeto = "C:/Users/eduar/Desktop/Portfolio_Django"

# Extensões que queremos incluir
extensoes = ('.html', '.py')

arquivos = []

for raiz, dirs, files in os.walk(projeto):
    for nome in files:
        if nome.endswith(extensoes):
            caminho = os.path.join(raiz, nome)
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
            except Exception as e:
                conteudo = f"[ERRO AO LER ARQUIVO: {e}]"
            
            # Caminho relativo para facilitar
            caminho_relativo = os.path.relpath(caminho, projeto)

            arquivos.append({
                "path": caminho_relativo,
                "type": nome.split('.')[-1],
                "content": conteudo
            })

saida = {
    "project_name": os.path.basename(projeto),
    "root_path": projeto,
    "files": arquivos
}

# Gera o JSON organizado
with open("projeto_django_unificado.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=2)

print("✅ Arquivo 'projeto_django_unificado.json' gerado com sucesso!")
