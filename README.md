# 🎬 Script de Sincronização de Imagens para OpenShot

Automatize a adição de múltiplas imagens em timestamps específicos no OpenShot Video Editor.

## 📋 Índice

1. [Requisitos](#requisitos)
2. [Como Usar](#como-usar)
3. [Métodos Disponíveis](#métodos-disponíveis)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Formato do CSV](#formato-do-csv)
6. [Dicas e Truques](#dicas-e-truques)

---

## 🔧 Requisitos

- Python 3.6 ou superior
- OpenShot Video Editor instalado
- Suas imagens em formatos: PNG, JPG, JPEG, GIF, etc.

**Instalação:**
```bash
# Não precisa instalar nada! O script usa JSON para manipular projetos OpenShot
python3 exemplo_uso.py
```

---

## 🚀 Como Usar

### Método 1: Editar o Script Diretamente

**Arquivo:** `exemplo_uso.py`

1. Abra o arquivo `exemplo_uso.py`
2. Edite a seção de configurações no topo do arquivo:

```python
# Nome do arquivo de projeto
PROJETO = "meu_video.osp"

# Criar novo ou carregar existente
CRIAR_NOVO = True

# Defina suas imagens e timestamps
IMAGENS_TIMESTAMPS = [
    ("imagem1.png", 5.0, 3.0),    # Aparece aos 5s, dura 3s
    ("imagem2.png", 12.5, 2.0),   # Aparece aos 12.5s, dura 2s
    ("imagem3.png", 20.0, 4.5),   # Aparece aos 20s, dura 4.5s
]
```

3. Execute o script:
```bash
python3 exemplo_uso.py
```

4. Abra o arquivo `.osp` gerado no OpenShot

---

### Método 2: Usar Arquivo CSV

**Arquivo:** `sync_from_csv.py`

1. Crie um arquivo CSV com suas imagens e timestamps:

```csv
imagem,timestamp,duracao
logo.png,0.0,5.0
foto1.jpg,5.5,3.0
foto2.jpg,10.0,2.5
```

2. Configure o script `sync_from_csv.py`:
```python
ARQUIVO_CSV = "timestamps.csv"
PROJETO = "meu_video.osp"
```

3. Execute:
```bash
python3 sync_from_csv.py
```

---

## 📚 Métodos Disponíveis

### `create_new_project(width, height, fps)`
Cria um novo projeto OpenShot.

```python
sync = OpenShotImageSync("projeto.osp")
sync.create_new_project(width=1920, height=1080, fps=30)
```

### `load_project()`
Carrega um projeto OpenShot existente.

```python
sync = OpenShotImageSync("projeto_existente.osp")
sync.load_project()
```

### `add_image_at_timestamp()`
Adiciona uma imagem em um timestamp específico.

```python
sync.add_image_at_timestamp(
    image_path="foto.jpg",
    timestamp=5.0,      # Aparece aos 5 segundos
    duration=3.0,       # Dura 3 segundos
    layer=2,            # Camada 2 (maior = mais na frente)
    x=0.0,              # Posição X (0.0 a 1.0)
    y=0.0,              # Posição Y (0.0 a 1.0)
    scale_x=1.0,        # Escala horizontal
    scale_y=1.0         # Escala vertical
)
```

### `add_multiple_images()`
Adiciona múltiplas imagens de uma vez.

```python
imagens = [
    ("img1.png", 5.0, 3.0),
    ("img2.png", 10.0, 2.0),
    ("img3.png", 15.0, 4.0),
]
sync.add_multiple_images(imagens, layer=2)
```

### `add_images_at_interval()`
Adiciona imagens em intervalos regulares.

```python
imagens = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
sync.add_images_at_interval(
    image_paths=imagens,
    start_time=0.0,     # Começa em 0s
    interval=5.0,       # Uma imagem a cada 5s
    duration=2.0,       # Cada imagem dura 2s
    layer=1
)
```

### `save_project()`
Salva o projeto.

```python
sync.save_project()  # Salva no mesmo arquivo
sync.save_project("novo_projeto.osp")  # Salva em novo arquivo
```

---

## 💡 Exemplos Práticos

### Exemplo 1: Adicionar Logo no Canto

```python
from sync_images_openshot import OpenShotImageSync

sync = OpenShotImageSync("video_com_logo.osp")
sync.create_new_project()

# Logo no canto superior direito, durante todo o vídeo
sync.add_image_at_timestamp(
    image_path="logo.png",
    timestamp=0.0,
    duration=60.0,  # 1 minuto
    layer=5,        # Camada alta (fica na frente)
    x=0.85,         # 85% para a direita
    y=0.05,         # 5% do topo
    scale_x=0.15,   # 15% do tamanho
    scale_y=0.15
)

sync.save_project()
```

### Exemplo 2: Slideshow de Fotos

```python
from sync_images_openshot import OpenShotImageSync

sync = OpenShotImageSync("slideshow.osp")
sync.create_new_project()

fotos = [
    "ferias1.jpg", "ferias2.jpg", "ferias3.jpg",
    "ferias4.jpg", "ferias5.jpg"
]

# Uma foto a cada 4 segundos, cada uma dura 3.5 segundos
sync.add_images_at_interval(
    image_paths=fotos,
    start_time=0.0,
    interval=4.0,
    duration=3.5,
    layer=1
)

sync.save_project()
```

### Exemplo 3: Gráficos em Apresentação

```python
from sync_images_openshot import OpenShotImageSync

sync = OpenShotImageSync("apresentacao.osp")
sync.create_new_project()

graficos = [
    ("grafico_vendas.png", 10.0, 5.0),    # Mostra aos 10s
    ("grafico_lucro.png", 20.0, 5.0),     # Mostra aos 20s
    ("grafico_crescimento.png", 30.0, 5.0), # Mostra aos 30s
]

sync.add_multiple_images(graficos, layer=2)
sync.save_project()
```

---

## 📄 Formato do CSV

### Formato Básico
```csv
imagem,timestamp,duracao
foto1.jpg,0.0,3.0
foto2.jpg,5.0,2.5
foto3.jpg,10.0,4.0
```

### Formato Sem Duração (usa padrão)
```csv
imagem,timestamp
foto1.jpg,0.0
foto2.jpg,5.0
foto3.jpg,10.0
```

### Com Comentários
```csv
# Isto é um comentário
imagem,timestamp,duracao
# Abertura
logo.png,0.0,5.0
# Conteúdo principal
foto1.jpg,5.0,3.0
foto2.jpg,10.0,3.0
```

---

## 🎯 Dicas e Truques

### 1. Caminhos de Imagens
```python
# Caminho relativo (mesma pasta do script)
"foto.jpg"

# Caminho absoluto
"/home/usuario/imagens/foto.jpg"

# Caminho relativo a uma pasta
"imagens/foto.jpg"
```

### 2. Layers (Camadas)
- **Layer 1**: Fundo
- **Layer 2-3**: Conteúdo principal
- **Layer 4-5**: Overlays (logos, marcas d'água)
- Números maiores ficam **na frente**

### 3. Posicionamento
```python
# Centralizado
x=0.5, y=0.5

# Canto superior esquerdo
x=0.0, y=0.0

# Canto superior direito
x=1.0, y=0.0

# Canto inferior esquerdo
x=0.0, y=1.0

# Canto inferior direito
x=1.0, y=1.0
```

### 4. Escala
```python
# Tamanho original
scale_x=1.0, scale_y=1.0

# Metade do tamanho
scale_x=0.5, scale_y=0.5

# Dobro do tamanho
scale_x=2.0, scale_y=2.0

# Apenas largura (mantém proporção)
scale_x=0.5, scale_y=0.5
```

### 5. Timestamps Precisos
```python
# Segundos inteiros
5.0  # 5 segundos

# Com decimais
5.5  # 5 segundos e meio
10.75  # 10 segundos e 750 milissegundos

# Minutos para segundos
2 * 60 + 30  # 2 minutos e 30 segundos = 150 segundos
```

---

## 🔍 Troubleshooting

### Erro: "Imagem não encontrada"
- Verifique se o caminho está correto
- Use caminho absoluto se estiver em dúvida
- Verifique se o arquivo existe

### Projeto não abre no OpenShot
- Certifique-se que o OpenShot está atualizado
- Verifique se o arquivo .osp foi salvo corretamente
- Tente criar um novo projeto

### Imagens não aparecem no vídeo
- Verifique os timestamps
- Confirme que a duração é maior que 0
- Verifique o layer (números baixos ficam atrás)

---

## 📞 Suporte

Para mais informações sobre OpenShot:
- Website: https://www.openshot.org/
- Documentação: https://www.openshot.org/user-guide/

---

## 📝 Licença

Este script é fornecido como está, sem garantias. Use por sua conta e risco.

---

**Desenvolvido para facilitar a vida de editores de vídeo! 🎥**
