#!/usr/bin/env python3
"""
Assistente Interativo - Sincronização de Imagens OpenShot
Ferramenta amigável para criar projetos sem editar código
"""

from sync_images_openshot import OpenShotImageSync
import os


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')


def imprimir_cabecalho():
    """Imprime o cabeçalho do assistente"""
    print("\n" + "="*70)
    print("🎬 ASSISTENTE DE SINCRONIZAÇÃO DE IMAGENS PARA OPENSHOT")
    print("="*70 + "\n")


def obter_configuracoes_projeto():
    """Obtém as configurações básicas do projeto"""
    imprimir_cabecalho()
    print("📋 CONFIGURAÇÕES DO PROJETO\n")
    
    nome_projeto = input("Nome do arquivo de projeto (.osp): ").strip()
    if not nome_projeto.endswith('.osp'):
        nome_projeto += '.osp'
    
    print("\n📐 Resolução do vídeo:")
    print("1. Full HD (1920x1080) - Recomendado")
    print("2. HD (1280x720)")
    print("3. 4K (3840x2160)")
    print("4. Personalizado")
    
    opcao = input("\nEscolha a resolução (1-4): ").strip()
    
    if opcao == "1":
        largura, altura = 1920, 1080
    elif opcao == "2":
        largura, altura = 1280, 720
    elif opcao == "3":
        largura, altura = 3840, 2160
    else:
        largura = int(input("Largura (pixels): ").strip())
        altura = int(input("Altura (pixels): ").strip())
    
    fps = input("\nTaxa de quadros (fps) [30]: ").strip()
    fps = float(fps) if fps else 30.0
    
    return nome_projeto, largura, altura, fps


def adicionar_imagens_manual():
    """Modo manual de adição de imagens"""
    imagens = []
    
    print("\n📸 ADICIONAR IMAGENS\n")
    print("Digite as informações de cada imagem.")
    print("Digite 'fim' no caminho da imagem quando terminar.\n")
    
    contador = 1
    while True:
        print(f"\n--- Imagem {contador} ---")
        caminho = input("Caminho da imagem (ou 'fim' para terminar): ").strip()
        
        if caminho.lower() == 'fim':
            break
        
        if not os.path.exists(caminho):
            print(f"⚠️  AVISO: Arquivo não encontrado: {caminho}")
            continuar = input("Adicionar mesmo assim? (s/n): ").strip().lower()
            if continuar != 's':
                continue
        
        timestamp = float(input("Timestamp (segundos): ").strip())
        duracao = float(input("Duração (segundos): ").strip())
        
        imagens.append((caminho, timestamp, duracao))
        contador += 1
        
        print(f"✓ Imagem adicionada!")
    
    return imagens


def adicionar_imagens_intervalo():
    """Modo de intervalo regular"""
    print("\n📸 ADICIONAR IMAGENS EM INTERVALOS\n")
    
    # Pedir lista de imagens
    print("Digite os caminhos das imagens, um por linha.")
    print("Digite 'fim' quando terminar.\n")
    
    imagens = []
    contador = 1
    while True:
        caminho = input(f"Imagem {contador} (ou 'fim'): ").strip()
        if caminho.lower() == 'fim':
            break
        imagens.append(caminho)
        contador += 1
    
    if not imagens:
        return None
    
    # Configurações do intervalo
    print(f"\n✓ {len(imagens)} imagens adicionadas\n")
    tempo_inicial = float(input("Tempo inicial (segundos) [0]: ").strip() or "0")
    intervalo = float(input("Intervalo entre imagens (segundos): ").strip())
    duracao = float(input("Duração de cada imagem (segundos): ").strip())
    
    return {
        'imagens': imagens,
        'tempo_inicial': tempo_inicial,
        'intervalo': intervalo,
        'duracao': duracao
    }


def adicionar_imagens_arquivo():
    """Importar de arquivo de texto"""
    print("\n📄 IMPORTAR DE ARQUIVO\n")
    print("O arquivo deve ter o formato:")
    print("caminho/imagem.png,timestamp,duracao")
    print("(uma imagem por linha)\n")
    
    arquivo = input("Caminho do arquivo: ").strip()
    
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo não encontrado: {arquivo}")
        return None
    
    imagens = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha_num, linha in enumerate(f, 1):
                linha = linha.strip()
                if not linha or linha.startswith('#'):
                    continue
                
                partes = linha.split(',')
                if len(partes) >= 3:
                    caminho = partes[0].strip()
                    timestamp = float(partes[1].strip())
                    duracao = float(partes[2].strip())
                    imagens.append((caminho, timestamp, duracao))
        
        print(f"✓ {len(imagens)} imagens importadas")
        return imagens
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return None


def menu_adicionar_imagens():
    """Menu para escolher método de adição"""
    print("\n🎯 COMO DESEJA ADICIONAR AS IMAGENS?\n")
    print("1. Manualmente (digitar uma por uma)")
    print("2. Intervalos regulares (slideshow)")
    print("3. Importar de arquivo")
    print("0. Cancelar")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == "1":
        return adicionar_imagens_manual(), 'manual'
    elif opcao == "2":
        return adicionar_imagens_intervalo(), 'intervalo'
    elif opcao == "3":
        return adicionar_imagens_arquivo(), 'manual'
    else:
        return None, None


def configurar_layer():
    """Configurar a camada (layer)"""
    print("\n📊 CONFIGURAR CAMADA (LAYER)\n")
    print("Camadas maiores ficam na frente:")
    print("1 = Fundo")
    print("2-3 = Conteúdo principal")
    print("4-5 = Overlays/logos")
    
    layer = input("\nNúmero da camada [2]: ").strip()
    return int(layer) if layer else 2


def mostrar_resumo(nome_projeto, largura, altura, fps, imagens_info, layer):
    """Mostra um resumo antes de criar o projeto"""
    print("\n" + "="*70)
    print("📋 RESUMO DO PROJETO")
    print("="*70)
    print(f"\n📂 Arquivo: {nome_projeto}")
    print(f"📐 Resolução: {largura}x{altura} @ {fps} fps")
    print(f"📊 Layer: {layer}")
    
    if isinstance(imagens_info, list):
        print(f"📸 Imagens: {len(imagens_info)}")
        print("\nPreview:")
        for i, (img, ts, dur) in enumerate(imagens_info[:5], 1):
            print(f"  {i}. {os.path.basename(img)} → {ts}s (dura {dur}s)")
        if len(imagens_info) > 5:
            print(f"  ... e mais {len(imagens_info) - 5} imagens")
    else:
        print(f"📸 Imagens: {len(imagens_info['imagens'])}")
        print(f"⏱️  Intervalo: {imagens_info['intervalo']}s")
        print(f"⏱️  Duração: {imagens_info['duracao']}s")
    
    print("\n" + "="*70)


def main():
    """Função principal do assistente"""
    limpar_tela()
    imprimir_cabecalho()
    
    print("Bem-vindo ao assistente interativo!")
    print("Vamos criar seu projeto passo a passo.\n")
    
    input("Pressione ENTER para começar...")
    
    # 1. Configurações do projeto
    nome_projeto, largura, altura, fps = obter_configuracoes_projeto()
    
    # 2. Adicionar imagens
    imagens_info, modo = menu_adicionar_imagens()
    
    if not imagens_info:
        print("\n❌ Nenhuma imagem adicionada. Encerrando...")
        return
    
    # 3. Configurar layer
    layer = configurar_layer()
    
    # 4. Mostrar resumo
    limpar_tela()
    mostrar_resumo(nome_projeto, largura, altura, fps, imagens_info, layer)
    
    confirmacao = input("\n✅ Criar projeto? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("\n❌ Operação cancelada.")
        return
    
    # 5. Criar projeto
    print("\n" + "="*70)
    print("🔧 CRIANDO PROJETO...")
    print("="*70 + "\n")
    
    sync = OpenShotImageSync(nome_projeto)
    sync.create_new_project(width=largura, height=altura, fps=fps)
    
    if modo == 'intervalo':
        sync.add_images_at_interval(
            image_paths=imagens_info['imagens'],
            start_time=imagens_info['tempo_inicial'],
            interval=imagens_info['intervalo'],
            duration=imagens_info['duracao'],
            layer=layer
        )
    else:
        sync.add_multiple_images(imagens_info, layer=layer)
    
    sync.save_project()
    
    # 6. Finalização
    print("\n" + "="*70)
    print("✅ PROJETO CRIADO COM SUCESSO!")
    print("="*70)
    print(f"\n📂 Arquivo: {nome_projeto}")
    print("👉 Abra este arquivo no OpenShot para visualizar")
    print("\n🎬 Bom trabalho!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
