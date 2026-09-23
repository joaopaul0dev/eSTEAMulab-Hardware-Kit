import os

# Definição da estrutura de pastas e componentes
estrutura = {
    "assets": [],
    "docs": ["setup-ambiente.md", "troubleshooting.md"],
    "01-saidas-digitais": ["README.md", "codigo_exemplo.ino"],
    "02-entradas-digitais": ["README.md", "codigo_exemplo.ino"],
    "03-sensor-ldr": ["README.md", "codigo_exemplo.ino"],
    "04-ultrassonico": ["README.md", "codigo_exemplo.ino"],
    "05-sensor-dht": ["README.md", "codigo_exemplo.ino"],
    "06-servomotor": ["README.md", "codigo_exemplo.ino"],
    "07-display-oled": ["README.md", "codigo_exemplo.ino"],
    "08-esp32-webserver": ["README.md", "codigo_exemplo.ino"],
    "09-esp32-iot-cloud": ["README.md", "codigo_exemplo.ino"]
}

print("🚀 A iniciar a criação da estrutura do eSTEAMulab Hardware Kit...\n")

for pasta, arquivos in estrutura.items():
    # Cria a pasta principal do componente ou diretório
    os.makedirs(pasta, exist_ok=True)
    print(f"📁 Pasta criada/verificada: {pasta}/")
    
    # Se for a pasta 'docs', cria os ficheiros de documentação
    if pasta == "docs":
        for arq in arquivos:
            caminho_arq = os.path.join(pasta, arq)
            if not os.path.exists(caminho_arq):
                with open(caminho_arq, "w", encoding="utf-8") as f:
                    if "setup-ambiente" in arq:
                        f.write("# Guia de Configuração do Ambiente\n\nInstruções para instalar a IDE do Arduino e os drivers do ESP32/Arduino.")
                    elif "troubleshooting" in arq:
                        f.write("# Solução de Problemas (Troubleshooting)\n\nErros comuns e como resolvê-los na bancada.")
                print(f"   └── 📄 Ficheiro criado: {caminho_arq}")

    # Se forem pastas de componentes, cria o README.md e o ficheiro .ino base
    elif pasta.startswith(("01", "02", "03", "04", "05", "06", "07", "08", "09")):
        for arq in arquivos:
            caminho_arq = os.path.join(pasta, arq)
            if not os.path.exists(caminho_arq):
                with open(caminho_arq, "w", encoding="utf-8") as f:
                    if arq.endswith(".md"):
                        f.write(f"# Nome do Componente\n\nBreve descrição do funcionamento do componente.\n\n## Esquema de Ligação\n| Pino | ESP32 / Arduino |\n|---|---|\n\n![Esquema](esquematico.png)\n")
                    elif arq.endswith(".ino"):
                        f.write("// Código de exemplo base para teste rápido no eSTEAMulab\n\nvoid setup() {\n  Serial.begin(115200);\n}\n\nvoid loop() {\n  // Insere a tua lógica aqui\n}\n")
                print(f"   └── 📄 Ficheiro criado: {caminho_arq}")

# Cria ficheiros raiz se não existirem
fich_raiz = {
    "LICENSE": "MIT License\n\nCopyright (c) 2026 eSTEAMulab",
    ".gitignore": "downloads/\n*.local\n.DS_Store"
}

for nome, conteudo in fich_raiz.items():
    if not os.path.exists(nome):
        with open(nome, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"📄 Ficheiro raiz criado: {nome}")

print("\n✨ Estrutura gerada com sucesso! Podes começar a preencher os conteúdos e adicionar as imagens 'esquematico.png' em cada pasta.")