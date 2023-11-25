import os

os.system('cls')
# Caminho absoluto para o diretório do script atual
diretorio_script = os.path.dirname(os.path.abspath(__file__))

print(diretorio_script)

# Construir o caminho relativo a partir do diretório do script
caminho_relativo = os.path.join(diretorio_script, "..", "..")
# Resolve o caminho relativo para um caminho absoluto
caminho_relativo = os.path.abspath(caminho_relativo)

print(caminho_relativo)