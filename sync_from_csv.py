#!/usr/bin/env python3
"""
Script: Sincronizar Imagens usando arquivo CSV
Lê os timestamps de um arquivo CSV e adiciona as imagens automaticamente
"""

import csv
from sync_images_openshot import OpenShotImageSync

# ===== CONFIGURAÇÕES =====
ARQUIVO_CSV = "timestamps.csv"  # Arquivo com as informações
PROJETO = "video_com_imagens.osp"
CRIAR_NOVO = True

# Configurações do vídeo (se criar novo)
LARGURA = 1920
ALTURA = 1080
FPS = 30

# Configurações das imagens
LAYER_PADRAO = 2
DURACAO_PADRAO = 3.0  # Se não especificada no CSV


def ler_timestamps_csv(arquivo_csv):
    """
    Lê o arquivo CSV com as informações das imagens
    
    Formato esperado do CSV:
    imagem,timestamp,duracao
    foto1.jpg,5.0,3.0
    foto2.jpg,10.5,2.5
    
    OU (sem duração, usa valor padrão):
    imagem,timestamp
    foto1.jpg,5.0
    foto2.jpg,10.5
    """
    imagens = []
    
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as f:
            # Detecta automaticamente se tem cabeçalho
            sniffer = csv.Sniffer()
            sample = f.read(1024)
            f.seek(0)
            has_header = sniffer.has_header(sample)
            
            reader = csv.reader(f)
            
            if has_header:
                next(reader)  # Pula o cabeçalho
            
            for linha_num, row in enumerate(reader, start=1):
                if not row or row[0].startswith('#'):  # Ignora linhas vazias ou comentários
                    continue
                
                try:
                    if len(row) >= 3:
                        # Formato: imagem, timestamp, duração
                        imagem = row[0].strip()
                        timestamp = float(row[1].strip())
                        duracao = float(row[2].strip())
                    elif len(row) >= 2:
                        # Formato: imagem, timestamp (usa duração padrão)
                        imagem = row[0].strip()
                        timestamp = float(row[1].strip())
                        duracao = DURACAO_PADRAO
                    else:
                        print(f"⚠️  Linha {linha_num} ignorada: formato inválido")
                        continue
                    
                    imagens.append((imagem, timestamp, duracao))
                    
                except ValueError as e:
                    print(f"⚠️  Erro na linha {linha_num}: {e}")
                    continue
        
        return imagens
        
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {arquivo_csv}")
        return []
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return []


def main():
    print("\n" + "="*60)
    print("🎬 SINCRONIZAÇÃO DE IMAGENS (CSV) PARA OPENSHOT")
    print("="*60 + "\n")
    
    # Lê os timestamps do arquivo CSV
    print(f"📄 Lendo timestamps de: {ARQUIVO_CSV}\n")
    imagens = ler_timestamps_csv(ARQUIVO_CSV)
    
    if not imagens:
        print("❌ Nenhuma imagem válida encontrada no arquivo CSV")
        print("\nFormato esperado do CSV:")
        print("imagem,timestamp,duracao")
        print("foto1.jpg,5.0,3.0")
        print("foto2.jpg,10.5,2.5")
        return
    
    print(f"✓ {len(imagens)} imagens encontradas no CSV\n")
    
    # Mostra preview das imagens
    print("📋 Preview das imagens:")
    print("-" * 60)
    for i, (img, ts, dur) in enumerate(imagens, 1):
        print(f"{i:2d}. {img:30s} → {ts:6.1f}s (dura {dur:.1f}s)")
    print("-" * 60 + "\n")
    
    # Inicializa o sincronizador
    sync = OpenShotImageSync(PROJETO)
    
    if CRIAR_NOVO:
        print(f"📝 Criando novo projeto: {PROJETO}")
        sync.create_new_project(width=LARGURA, height=ALTURA, fps=FPS)
    else:
        print(f"📂 Carregando projeto existente: {PROJETO}")
        if not sync.load_project():
            print("❌ Erro ao carregar projeto. Abortando.")
            return
    
    # Adiciona todas as imagens
    print(f"\n📸 Adicionando imagens ao projeto...\n")
    sync.add_multiple_images(imagens, layer=LAYER_PADRAO)
    
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
