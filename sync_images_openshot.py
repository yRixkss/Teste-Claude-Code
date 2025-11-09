#!/usr/bin/env python3
"""
Script para sincronizar imagens com timestamps no OpenShot
Automatiza a adição de múltiplas imagens em momentos específicos do vídeo
"""

import json
import os
from typing import List, Dict, Tuple


class OpenShotImageSync:
    """Classe para sincronizar imagens com timestamps no OpenShot"""
    
    def __init__(self, project_path: str):
        """
        Inicializa o sincronizador
        
        Args:
            project_path: Caminho para o arquivo .osp do projeto OpenShot
        """
        self.project_path = project_path
        self.project_data = None
        
    def load_project(self) -> bool:
        """Carrega o projeto OpenShot existente"""
        try:
            with open(self.project_path, 'r', encoding='utf-8') as f:
                self.project_data = json.load(f)
            print(f"✓ Projeto carregado: {self.project_path}")
            return True
        except FileNotFoundError:
            print(f"✗ Arquivo não encontrado: {self.project_path}")
            return False
        except json.JSONDecodeError:
            print(f"✗ Erro ao decodificar JSON do projeto")
            return False
    
    def create_new_project(self, width: int = 1920, height: int = 1080, fps: float = 30.0):
        """Cria um novo projeto OpenShot"""
        self.project_data = {
            "version": {"openshot-qt": "3.1.1", "libopenshot": "0.3.2"},
            "width": width,
            "height": height,
            "fps": {"num": int(fps), "den": 1},
            "sample_rate": 44100,
            "channels": 2,
            "channel_layout": 3,
            "clips": [],
            "files": [],
            "effects": [],
            "layers": [],
            "scale": 15,
            "tick_pixels": 100,
            "playhead_position": 0,
            "profile": "HD 1080p 30 fps",
            "markers": []
        }
        print(f"✓ Novo projeto criado ({width}x{height} @ {fps}fps)")
    
    def add_image_at_timestamp(self, 
                               image_path: str, 
                               timestamp: float, 
                               duration: float = 2.0,
                               layer: int = 1,
                               x: float = 0.0,
                               y: float = 0.0,
                               scale_x: float = 1.0,
                               scale_y: float = 1.0) -> bool:
        """
        Adiciona uma imagem em um timestamp específico
        
        Args:
            image_path: Caminho da imagem
            timestamp: Tempo em segundos onde a imagem deve aparecer
            duration: Duração da imagem em segundos
            layer: Camada/layer do vídeo (maior = mais na frente)
            x, y: Posição da imagem (0-1, normalizado)
            scale_x, scale_y: Escala da imagem
            
        Returns:
            True se sucesso, False caso contrário
        """
        if not os.path.exists(image_path):
            print(f"✗ Imagem não encontrada: {image_path}")
            return False
        
        # Adiciona o arquivo à lista de arquivos do projeto
        file_id = f"file_{len(self.project_data['files']) + 1}"
        file_entry = {
            "id": file_id,
            "path": os.path.abspath(image_path),
            "media_type": "image"
        }
        self.project_data['files'].append(file_entry)
        
        # Cria o clip
        clip_id = f"clip_{len(self.project_data['clips']) + 1}"
        clip_entry = {
            "id": clip_id,
            "file_id": file_id,
            "position": timestamp,
            "start": 0,
            "end": duration,
            "layer": layer,
            "alpha": {
                "Points": [
                    {"co": {"X": 1, "Y": 1}, "interpolation": 0}
                ]
            },
            "location_x": {
                "Points": [
                    {"co": {"X": 1, "Y": x}, "interpolation": 0}
                ]
            },
            "location_y": {
                "Points": [
                    {"co": {"X": 1, "Y": y}, "interpolation": 0}
                ]
            },
            "scale_x": {
                "Points": [
                    {"co": {"X": 1, "Y": scale_x}, "interpolation": 0}
                ]
            },
            "scale_y": {
                "Points": [
                    {"co": {"X": 1, "Y": scale_y}, "interpolation": 0}
                ]
            }
        }
        self.project_data['clips'].append(clip_entry)
        
        print(f"✓ Imagem adicionada: {os.path.basename(image_path)} em {timestamp}s")
        return True
    
    def add_multiple_images(self, 
                           image_timestamps: List[Tuple[str, float, float]],
                           layer: int = 1):
        """
        Adiciona múltiplas imagens com seus timestamps
        
        Args:
            image_timestamps: Lista de tuplas (caminho_imagem, timestamp, duração)
            layer: Camada para todas as imagens
        """
        successful = 0
        for img_path, timestamp, duration in image_timestamps:
            if self.add_image_at_timestamp(img_path, timestamp, duration, layer):
                successful += 1
        
        print(f"\n✓ Total: {successful}/{len(image_timestamps)} imagens adicionadas com sucesso")
    
    def add_images_at_interval(self,
                              image_paths: List[str],
                              start_time: float = 0.0,
                              interval: float = 5.0,
                              duration: float = 2.0,
                              layer: int = 1):
        """
        Adiciona imagens em intervalos regulares
        
        Args:
            image_paths: Lista de caminhos das imagens
            start_time: Tempo inicial em segundos
            interval: Intervalo entre imagens em segundos
            duration: Duração de cada imagem
            layer: Camada das imagens
        """
        current_time = start_time
        for img_path in image_paths:
            self.add_image_at_timestamp(img_path, current_time, duration, layer)
            current_time += interval
        
        print(f"\n✓ {len(image_paths)} imagens adicionadas em intervalos de {interval}s")
    
    def save_project(self, output_path: str = None):
        """Salva o projeto OpenShot"""
        if output_path is None:
            output_path = self.project_path
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.project_data, f, indent=2, ensure_ascii=False)
            print(f"\n✓ Projeto salvo: {output_path}")
            return True
        except Exception as e:
            print(f"\n✗ Erro ao salvar projeto: {e}")
            return False


def exemplo_uso_basico():
    """Exemplo básico de uso do script"""
    print("=" * 60)
    print("EXEMPLO 1: Adicionando imagens em timestamps específicos")
    print("=" * 60)
    
    # Cria um novo projeto
    sync = OpenShotImageSync("meu_projeto.osp")
    sync.create_new_project(width=1920, height=1080, fps=30)
    
    # Define as imagens e seus timestamps
    # Formato: (caminho_da_imagem, timestamp_em_segundos, duração_em_segundos)
    imagens = [
        ("imagem1.png", 5.0, 3.0),   # Aparece aos 5s, dura 3s
        ("imagem2.png", 10.0, 2.5),  # Aparece aos 10s, dura 2.5s
        ("imagem3.png", 15.0, 4.0),  # Aparece aos 15s, dura 4s
    ]
    
    # Adiciona todas as imagens
    sync.add_multiple_images(imagens, layer=2)
    
    # Salva o projeto
    sync.save_project()


def exemplo_uso_intervalo():
    """Exemplo com imagens em intervalos regulares"""
    print("\n" + "=" * 60)
    print("EXEMPLO 2: Adicionando imagens em intervalos regulares")
    print("=" * 60)
    
    # Cria um novo projeto
    sync = OpenShotImageSync("projeto_intervalo.osp")
    sync.create_new_project()
    
    # Lista de imagens
    imagens = [
        "foto1.jpg",
        "foto2.jpg",
        "foto3.jpg",
        "foto4.jpg",
        "foto5.jpg"
    ]
    
    # Adiciona uma imagem a cada 5 segundos, cada uma durando 2 segundos
    sync.add_images_at_interval(
        image_paths=imagens,
        start_time=0.0,    # Começa em 0 segundos
        interval=5.0,      # Intervalo de 5 segundos
        duration=2.0,      # Cada imagem dura 2 segundos
        layer=1
    )
    
    # Salva o projeto
    sync.save_project()


def exemplo_uso_avancado():
    """Exemplo avançado com posicionamento customizado"""
    print("\n" + "=" * 60)
    print("EXEMPLO 3: Uso avançado com posicionamento")
    print("=" * 60)
    
    # Carrega projeto existente ou cria novo
    sync = OpenShotImageSync("projeto_avancado.osp")
    sync.create_new_project()
    
    # Adiciona imagens com posicionamento específico
    sync.add_image_at_timestamp(
        image_path="logo.png",
        timestamp=0.0,
        duration=10.0,
        layer=3,
        x=0.8,      # Posição X (0=esquerda, 1=direita)
        y=0.1,      # Posição Y (0=topo, 1=fundo)
        scale_x=0.2,  # Escala X (20% do tamanho original)
        scale_y=0.2   # Escala Y (20% do tamanho original)
    )
    
    sync.save_project()


if __name__ == "__main__":
    print("\n🎬 Script de Sincronização de Imagens para OpenShot\n")
    
    # Descomente o exemplo que deseja executar:
    
    # exemplo_uso_basico()
    # exemplo_uso_intervalo()
    # exemplo_uso_avancado()
    
    print("\n" + "=" * 60)
    print("INSTRUÇÕES DE USO:")
    print("=" * 60)
    print("""
1. Edite este script e descomente um dos exemplos acima, ou
2. Importe a classe OpenShotImageSync no seu próprio script:
   
   from sync_images_openshot import OpenShotImageSync
   
3. Crie uma instância e use os métodos disponíveis
4. Abra o arquivo .osp gerado no OpenShot para visualizar

MÉTODOS DISPONÍVEIS:
- create_new_project(): Cria um novo projeto
- load_project(): Carrega um projeto existente
- add_image_at_timestamp(): Adiciona uma imagem em timestamp específico
- add_multiple_images(): Adiciona várias imagens de uma vez
- add_images_at_interval(): Adiciona imagens em intervalos regulares
- save_project(): Salva o projeto

PARÂMETROS IMPORTANTES:
- timestamp: Tempo em segundos onde a imagem aparece
- duration: Quanto tempo a imagem fica visível
- layer: Camada (números maiores ficam na frente)
- x, y: Posição normalizada (0.0 a 1.0)
- scale_x, scale_y: Escala da imagem (1.0 = tamanho original)
    """)
