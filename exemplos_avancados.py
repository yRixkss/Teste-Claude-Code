#!/usr/bin/env python3
"""
Exemplos Avançados - Sincronização de Imagens no OpenShot
Casos de uso mais complexos e profissionais
"""

from sync_images_openshot import OpenShotImageSync


def exemplo_video_tutorial():
    """
    Exemplo: Vídeo tutorial com imagens explicativas
    Adiciona screenshots em momentos-chave da explicação
    """
    print("\n" + "="*60)
    print("EXEMPLO: Vídeo Tutorial com Screenshots")
    print("="*60)
    
    sync = OpenShotImageSync("tutorial.osp")
    sync.create_new_project(width=1920, height=1080, fps=30)
    
    # Estrutura do tutorial
    tutorial_images = [
        # Introdução
        ("screenshot_abertura.png", 0.0, 5.0),
        
        # Passo 1
        ("passo1_interface.png", 10.0, 8.0),
        ("passo1_detalhe.png", 18.0, 6.0),
        
        # Passo 2
        ("passo2_menu.png", 30.0, 7.0),
        ("passo2_opcoes.png", 37.0, 5.0),
        
        # Passo 3
        ("passo3_configuracao.png", 50.0, 9.0),
        
        # Conclusão
        ("resultado_final.png", 70.0, 10.0),
        ("agradecimento.png", 85.0, 5.0),
    ]
    
    sync.add_multiple_images(tutorial_images, layer=2)
    sync.save_project()
    print("✓ Projeto tutorial criado com sucesso!")


def exemplo_apresentacao_corporativa():
    """
    Exemplo: Apresentação corporativa com gráficos e logos
    Logo fixo + gráficos que aparecem em momentos específicos
    """
    print("\n" + "="*60)
    print("EXEMPLO: Apresentação Corporativa")
    print("="*60)
    
    sync = OpenShotImageSync("apresentacao.osp")
    sync.create_new_project(width=1920, height=1080, fps=30)
    
    # Logo da empresa (fica o tempo todo, canto superior direito)
    sync.add_image_at_timestamp(
        image_path="logo_empresa.png",
        timestamp=0.0,
        duration=180.0,  # 3 minutos
        layer=5,
        x=0.88,
        y=0.05,
        scale_x=0.12,
        scale_y=0.12
    )
    
    # Slide de título
    sync.add_image_at_timestamp(
        "titulo_apresentacao.png",
        0.0, 8.0, layer=2
    )
    
    # Seção 1: Visão Geral
    sync.add_image_at_timestamp(
        "grafico_mercado.png",
        15.0, 12.0, layer=2
    )
    
    # Seção 2: Análise Financeira
    graficos_financeiros = [
        ("grafico_receita.png", 35.0, 10.0),
        ("grafico_lucro.png", 50.0, 10.0),
        ("grafico_crescimento.png", 65.0, 12.0),
    ]
    sync.add_multiple_images(graficos_financeiros, layer=2)
    
    # Seção 3: Planos Futuros
    sync.add_image_at_timestamp(
        "roadmap.png",
        90.0, 15.0, layer=2
    )
    
    # Slide de encerramento
    sync.add_image_at_timestamp(
        "obrigado.png",
        120.0, 10.0, layer=2
    )
    
    sync.save_project()
    print("✓ Apresentação corporativa criada!")


def exemplo_video_musical():
    """
    Exemplo: Vídeo musical com letras sincronizadas
    Adiciona imagens da letra em sincronia com a música
    """
    print("\n" + "="*60)
    print("EXEMPLO: Vídeo Musical com Letras")
    print("="*60)
    
    sync = OpenShotImageSync("musica.osp")
    sync.create_new_project(width=1920, height=1080, fps=30)
    
    # Timestamps da música (ajuste conforme sua música)
    letras = [
        # Verso 1
        ("letra_linha1.png", 5.5, 4.0),
        ("letra_linha2.png", 9.5, 3.5),
        ("letra_linha3.png", 13.0, 4.0),
        ("letra_linha4.png", 17.0, 3.0),
        
        # Refrão
        ("refrao_1.png", 22.0, 5.0),
        ("refrao_2.png", 27.0, 5.0),
        
        # Verso 2
        ("letra_linha5.png", 35.0, 4.0),
        ("letra_linha6.png", 39.0, 3.5),
        
        # Refrão final
        ("refrao_1.png", 45.0, 5.0),
        ("refrao_2.png", 50.0, 5.0),
    ]
    
    sync.add_multiple_images(letras, layer=3)
    sync.save_project()
    print("✓ Vídeo musical com letras criado!")


def exemplo_comparacao_antes_depois():
    """
    Exemplo: Vídeo de antes e depois
    Mostra imagens lado a lado com efeito de transição
    """
    print("\n" + "="*60)
    print("EXEMPLO: Comparação Antes e Depois")
    print("="*60)
    
    sync = OpenShotImageSync("antes_depois.osp")
    sync.create_new_project()
    
    transformacoes = [
        # Transformação 1
        ("antes1.jpg", "depois1.jpg", 5.0),
        # Transformação 2
        ("antes2.jpg", "depois2.jpg", 15.0),
        # Transformação 3
        ("antes3.jpg", "depois3.jpg", 25.0),
    ]
    
    for antes, depois, timestamp in transformacoes:
        # Imagem "antes" do lado esquerdo
        sync.add_image_at_timestamp(
            image_path=antes,
            timestamp=timestamp,
            duration=8.0,
            layer=2,
            x=0.25,  # Lado esquerdo
            y=0.5,
            scale_x=0.45,
            scale_y=0.45
        )
        
        # Imagem "depois" do lado direito
        sync.add_image_at_timestamp(
            image_path=depois,
            timestamp=timestamp,
            duration=8.0,
            layer=2,
            x=0.75,  # Lado direito
            y=0.5,
            scale_x=0.45,
            scale_y=0.45
        )
        
        # Texto "ANTES" e "DEPOIS"
        sync.add_image_at_timestamp(
            "texto_antes.png",
            timestamp, 8.0, layer=3,
            x=0.25, y=0.1, scale_x=0.2, scale_y=0.2
        )
        sync.add_image_at_timestamp(
            "texto_depois.png",
            timestamp, 8.0, layer=3,
            x=0.75, y=0.1, scale_x=0.2, scale_y=0.2
        )
    
    sync.save_project()
    print("✓ Vídeo de comparação criado!")


def exemplo_contador_progressivo():
    """
    Exemplo: Contador ou temporizador visual
    Adiciona números sequenciais em intervalos regulares
    """
    print("\n" + "="*60)
    print("EXEMPLO: Contador Progressivo")
    print("="*60)
    
    sync = OpenShotImageSync("contador.osp")
    sync.create_new_project()
    
    # Gera lista de imagens de números (assumindo que você tem numero_1.png até numero_60.png)
    numeros = [f"numero_{i}.png" for i in range(1, 61)]
    
    # Adiciona um número a cada segundo
    sync.add_images_at_interval(
        image_paths=numeros,
        start_time=0.0,
        interval=1.0,  # Um número por segundo
        duration=1.0,  # Cada número dura 1 segundo
        layer=4
    )
    
    sync.save_project()
    print("✓ Contador progressivo criado!")


def exemplo_galeria_fotos_automatica():
    """
    Exemplo: Galeria de fotos automática de uma pasta
    Busca todas as imagens de uma pasta e cria slideshow
    """
    print("\n" + "="*60)
    print("EXEMPLO: Galeria de Fotos Automática")
    print("="*60)
    
    import os
    import glob
    
    # Busca todas as imagens em uma pasta
    pasta_fotos = "minhas_fotos/"  # Altere para sua pasta
    extensoes = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    
    fotos = []
    for ext in extensoes:
        fotos.extend(glob.glob(os.path.join(pasta_fotos, ext)))
    
    if not fotos:
        print(f"⚠️  Nenhuma foto encontrada em {pasta_fotos}")
        print("   Criando exemplo com fotos dummy...")
        fotos = [f"foto_{i}.jpg" for i in range(1, 11)]
    
    sync = OpenShotImageSync("galeria_fotos.osp")
    sync.create_new_project()
    
    # Configurações do slideshow
    DURACAO_FOTO = 4.0      # Cada foto fica 4 segundos
    INTERVALO = 4.5         # Nova foto a cada 4.5 segundos (0.5s de transição)
    
    print(f"📸 Criando slideshow com {len(fotos)} fotos")
    sync.add_images_at_interval(
        image_paths=fotos,
        start_time=0.0,
        interval=INTERVALO,
        duration=DURACAO_FOTO,
        layer=1
    )
    
    # Adiciona música de fundo (se tiver)
    # sync.add_audio("musica_fundo.mp3", 0.0, duracao_total)
    
    sync.save_project()
    print(f"✓ Galeria com {len(fotos)} fotos criada!")
    print(f"   Duração total: {len(fotos) * INTERVALO:.1f} segundos")


def exemplo_multiplas_layers():
    """
    Exemplo: Composição complexa com múltiplas camadas
    Fundo + conteúdo + overlay + legenda + logo
    """
    print("\n" + "="*60)
    print("EXEMPLO: Composição Multi-camadas")
    print("="*60)
    
    sync = OpenShotImageSync("composicao.osp")
    sync.create_new_project()
    
    # Layer 1: Fundo (sempre visível)
    sync.add_image_at_timestamp(
        "fundo_gradiente.png",
        0.0, 60.0, layer=1
    )
    
    # Layer 2: Conteúdo principal
    conteudo = [
        ("slide1.png", 0.0, 10.0),
        ("slide2.png", 10.0, 10.0),
        ("slide3.png", 20.0, 10.0),
    ]
    sync.add_multiple_images(conteudo, layer=2)
    
    # Layer 3: Overlays e efeitos
    sync.add_image_at_timestamp(
        "particulas.png",
        0.0, 30.0, layer=3,
        x=0.5, y=0.5, scale_x=1.2, scale_y=1.2
    )
    
    # Layer 4: Legendas
    legendas = [
        ("legenda1.png", 0.0, 10.0),
        ("legenda2.png", 10.0, 10.0),
        ("legenda3.png", 20.0, 10.0),
    ]
    sync.add_multiple_images(legendas, layer=4)
    
    # Layer 5: Logo (sempre no topo)
    sync.add_image_at_timestamp(
        "logo.png",
        0.0, 60.0, layer=5,
        x=0.9, y=0.05, scale_x=0.1, scale_y=0.1
    )
    
    sync.save_project()
    print("✓ Composição multi-camadas criada!")


def menu_interativo():
    """Menu para executar os exemplos"""
    print("\n" + "="*70)
    print("🎬 EXEMPLOS AVANÇADOS - SINCRONIZAÇÃO DE IMAGENS OPENSHOT")
    print("="*70)
    print("\nEscolha um exemplo para executar:\n")
    print("1. Vídeo Tutorial com Screenshots")
    print("2. Apresentação Corporativa")
    print("3. Vídeo Musical com Letras")
    print("4. Comparação Antes e Depois")
    print("5. Contador Progressivo")
    print("6. Galeria de Fotos Automática")
    print("7. Composição Multi-camadas")
    print("0. Sair")
    print("\n" + "="*70)
    
    while True:
        try:
            escolha = input("\nDigite o número do exemplo (0 para sair): ").strip()
            
            if escolha == "0":
                print("\n👋 Até logo!")
                break
            elif escolha == "1":
                exemplo_video_tutorial()
            elif escolha == "2":
                exemplo_apresentacao_corporativa()
            elif escolha == "3":
                exemplo_video_musical()
            elif escolha == "4":
                exemplo_comparacao_antes_depois()
            elif escolha == "5":
                exemplo_contador_progressivo()
            elif escolha == "6":
                exemplo_galeria_fotos_automatica()
            elif escolha == "7":
                exemplo_multiplas_layers()
            else:
                print("❌ Opção inválida! Digite um número de 0 a 7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    # Descomente para usar o menu interativo:
    # menu_interativo()
    
    # Ou execute um exemplo específico diretamente:
    # exemplo_video_tutorial()
    # exemplo_apresentacao_corporativa()
    # exemplo_video_musical()
    # exemplo_comparacao_antes_depois()
    # exemplo_contador_progressivo()
    # exemplo_galeria_fotos_automatica()
    # exemplo_multiplas_layers()
    
    print("\n💡 DICA: Descomente a linha do exemplo que deseja executar")
    print("   ou use menu_interativo() para escolher interativamente\n")
