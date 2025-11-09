#!/usr/bin/env python3
"""
Script Prático: Sincronizar Imagens com OpenShot
Execute este script para adicionar suas imagens ao projeto
"""

from sync_images_openshot import OpenShotImageSync

# ===== CONFIGURAÇÕES - EDITE AQUI =====

# Nome do arquivo de projeto OpenShot (.osp)
PROJETO = "meu_video.osp"

# Você pode escolher criar um NOVO projeto ou CARREGAR um existente
CRIAR_NOVO = True  # Mude para False para carregar projeto existente

# Se criar novo, defina as configurações do vídeo
LARGURA = 1920
ALTURA = 1080
FPS = 30

# ===== OPÇÃO 1: Imagens com timestamps específicos =====
# Formato: ("caminho/da/imagem.png", tempo_em_segundos, duracao_em_segundos)
IMAGENS_TIMESTAMPS = [
    ("imagem1.png", 5.0, 3.0),    # Aparece aos 5s, dura 3s
    ("imagem2.png", 12.5, 2.0),   # Aparece aos 12.5s, dura 2s
    ("imagem3.png", 20.0, 4.5),   # Aparece aos 20s, dura 4.5s
    ("imagem4.png", 30.0, 3.0),   # Aparece aos 30s, dura 3s
]

# ===== OPÇÃO 2: Imagens em intervalos regulares =====
# Lista de imagens que serão adicionadas em intervalos fixos
IMAGENS_LISTA = [
    "foto1.jpg",
    "foto2.jpg", 
    "foto3.jpg",
    "foto4.jpg",
    "foto5.jpg",
]

# Configurações para intervalos
TEMPO_INICIAL = 0.0      # Quando a primeira imagem aparece (segundos)
INTERVALO = 5.0          # Tempo entre cada imagem (segundos)
DURACAO_PADRAO = 2.0     # Quanto tempo cada imagem fica visível (segundos)

# ===== ESCOLHA O MODO =====
# "timestamps" = usar IMAGENS_TIMESTAMPS
# "intervalo" = usar IMAGENS_LISTA com intervalos regulares
MODO = "timestamps"  # Mude para "intervalo" se preferir

# ===== CONFIGURAÇÕES AVANÇADAS (opcional) =====
LAYER = 2               # Camada (números maiores ficam na frente)
POSICAO_X = 0.0         # Posição horizontal (0.0=esquerda, 1.0=direita)
POSICAO_Y = 0.0         # Posição vertical (0.0=topo, 1.0=fundo)
ESCALA_X = 1.0          # Escala horizontal (1.0 = 100%)
ESCALA_Y = 1.0          # Escala vertical (1.0 = 100%)

# ====================================
# NÃO PRECISA EDITAR ABAIXO DESTA LINHA
# ====================================

def main():
    print("\n" + "="*60)
    print("🎬 SINCRONIZAÇÃO DE IMAGENS PARA OPENSHOT")
    print("="*60 + "\n")
    
    # Inicializa o sincronizador
    sync = OpenShotImageSync(PROJETO)
    
    # Cria novo ou carrega projeto existente
    if CRIAR_NOVO:
        print(f"📝 Criando novo projeto: {PROJETO}")
        sync.create_new_project(width=LARGURA, height=ALTURA, fps=FPS)
    else:
        print(f"📂 Carregando projeto existente: {PROJETO}")
        if not sync.load_project():
            print("❌ Erro ao carregar projeto. Abortando.")
            return
    
    print(f"\n🎯 Modo selecionado: {MODO.upper()}")
    print("-" * 60)
    
    # Adiciona as imagens de acordo com o modo escolhido
    if MODO == "timestamps":
        print(f"\n📸 Adicionando {len(IMAGENS_TIMESTAMPS)} imagens em timestamps específicos...\n")
        sync.add_multiple_images(IMAGENS_TIMESTAMPS, layer=LAYER)
        
    elif MODO == "intervalo":
        print(f"\n📸 Adicionando {len(IMAGENS_LISTA)} imagens em intervalos de {INTERVALO}s...\n")
        sync.add_images_at_interval(
            image_paths=IMAGENS_LISTA,
            start_time=TEMPO_INICIAL,
            interval=INTERVALO,
            duration=DURACAO_PADRAO,
            layer=LAYER
        )
    
    else:
        print(f"❌ Modo inválido: {MODO}")
        print("Use 'timestamps' ou 'intervalo'")
        return
    
    # Salva o projeto
    print("\n💾 Salvando projeto...")
    if sync.save_project():
        print("\n" + "="*60)
        print("✅ CONCLUÍDO COM SUCESSO!")
        print("="*60)
        print(f"\n📂 Arquivo gerado: {PROJETO}")
        print("👉 Abra este arquivo no OpenShot para ver o resultado\n")
    else:
        print("\n❌ Erro ao salvar o projeto\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
