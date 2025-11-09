🎬 GUIA DE INÍCIO RÁPIDO
========================

## ⚡ Começar em 3 Passos

### 1️⃣ Escolha seu método

**Opção A - Editar Script Diretamente:**
```bash
python3 exemplo_uso.py
```

**Opção B - Usar Arquivo CSV:**
```bash
python3 sync_from_csv.py
```

### 2️⃣ Configure suas imagens

**No exemplo_uso.py:**
```python
IMAGENS_TIMESTAMPS = [
    ("sua_imagem1.png", 5.0, 3.0),   # Tempo: 5s, Duração: 3s
    ("sua_imagem2.png", 10.0, 2.0),  # Tempo: 10s, Duração: 2s
]
```

**No timestamps.csv:**
```csv
imagem,timestamp,duracao
sua_imagem1.png,5.0,3.0
sua_imagem2.png,10.0,2.0
```

### 3️⃣ Execute e abra no OpenShot

```bash
python3 exemplo_uso.py
# Abre o arquivo .osp gerado no OpenShot
```

---

## 📦 Arquivos Incluídos

- **sync_images_openshot.py** - Biblioteca principal
- **exemplo_uso.py** - Exemplo prático para editar
- **sync_from_csv.py** - Lê timestamps de arquivo CSV
- **timestamps.csv** - Exemplo de arquivo CSV
- **README.md** - Documentação completa

---

## 💡 Exemplos Rápidos

### Logo no Canto
```python
from sync_images_openshot import OpenShotImageSync

sync = OpenShotImageSync("video.osp")
sync.create_new_project()
sync.add_image_at_timestamp(
    "logo.png", 0.0, 60.0,  # Do início aos 60s
    layer=5, x=0.85, y=0.05, scale_x=0.15, scale_y=0.15
)
sync.save_project()
```

### Slideshow Automático
```python
from sync_images_openshot import OpenShotImageSync

sync = OpenShotImageSync("slideshow.osp")
sync.create_new_project()
fotos = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
sync.add_images_at_interval(fotos, 0.0, 4.0, 3.0, 1)
sync.save_project()
```

---

## 🎯 Parâmetros Importantes

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| timestamp | Quando aparece (segundos) | `5.0` = 5 segundos |
| duration | Quanto tempo fica (segundos) | `3.0` = 3 segundos |
| layer | Camada (maior = frente) | `1` a `5` |
| x, y | Posição (0.0 a 1.0) | `x=0.5, y=0.5` = centro |
| scale | Tamanho (1.0 = 100%) | `0.5` = metade |

---

## 🔧 Solução de Problemas

**Imagem não encontrada?**
- Use caminho completo: `/home/usuario/imagens/foto.jpg`
- Ou coloque as imagens na mesma pasta do script

**Projeto não abre?**
- Verifique se o OpenShot está instalado
- Tente criar um novo projeto

**Precisa de ajuda?**
- Leia o README.md completo
- Visite: https://www.openshot.org/

---

🚀 **Pronto para começar!**
