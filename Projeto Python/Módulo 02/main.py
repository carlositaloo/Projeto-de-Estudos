import os

# Obtenha o diretório onde este script está localizado
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Construa o caminho relativo para o seu script principal
# Ajuste o caminho relativo conforme necessário
main_script = os.path.join(diretorio_script, "Exercício 045 – GAME Pedra Papel e Tesoura.py")

# Comando para abrir um novo terminal e executar o script principal
# Aspas duplas são usadas para lidar com espaços no nome do arquivo
command = f"python \"{main_script}\""

# No Windows, você pode usar algo como:
os.system(f"start cmd /k {command}")

# Certifique-se de que este script e o script principal estão no local correto em relação um ao outro
