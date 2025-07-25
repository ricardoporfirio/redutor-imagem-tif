# Script de Reamostragem de Imagens Raster (GeoTIFF)

Este repositório contém um script em Python para reamostrar (redimensionar) imagens geoespaciais no formato GeoTIFF. Ele foi projetado para reduzir a resolução espacial de arquivos raster grandes, tornando-os mais gerenciáveis para processamento e análise computacional.

## 📄 Descrição

Em projetos de sensoriamento remoto e geoprocessamento, é comum trabalhar com imagens de altíssima resolução (ex: ortomosaicos de drone), que podem ser computacionalmente pesadas. Este script oferece uma solução simples e eficaz para reduzir a resolução dessas imagens, aplicando um fator de escala e preservando as informações de georreferenciamento (Sistema de Coordenadas de Referência - SCR).

O exemplo prático que motivou este script foi a necessidade de reamostrar ortomosaicos com 4 cm de resolução espacial para uma nova resolução de 40 cm, a fim de viabilizar análises em um ambiente com limitações de hardware.

## ✨ Funcionalidades

-   Leitura de arquivos raster no formato GeoTIFF.
-   Redimensionamento da imagem com base em um fator de escala personalizável.
-   Suporte a diferentes algoritmos de interpolação (`bilinear`, `nearest neighbor`, `cubic`, etc.).
-   Preservação dos metadados espaciais essenciais (SCR e transformação geoespacial).
-   Criação de um novo arquivo GeoTIFF com a imagem reamostrada.

## ⚙️ Requisitos

-   Python 3.6+
-   Biblioteca `rasterio`

## 🚀 Instalação

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  Recomenda-se criar um ambiente virtual para instalar as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  Instale a biblioteca `rasterio`:
    ```bash
    pip install rasterio
    ```

## ▶️ Como Usar

1.  Coloque sua imagem GeoTIFF de entrada na pasta do projeto ou anote o caminho completo até ela.

2.  Abra o arquivo de script (ex: `reamostragem_raster.py`).

3.  Modifique as seguintes variáveis no início do script para adequá-las à sua necessidade:

    -   `input_path`: Caminho para o seu arquivo GeoTIFF de entrada.
    -   `output_path`: Caminho e nome do arquivo de saída que será gerado.
    -   `scale_factor`: Fator de escala para o redimensionamento.
    -   `resampling`: Método de interpolação a ser utilizado.

4.  Execute o script através do terminal:
    ```bash
    python reamostragem_raster.py
    ```

5.  Ao final da execução, a mensagem "Redimensionamento completo!" será exibida, e o novo arquivo GeoTIFF estará disponível no caminho de saída especificado.

### Parâmetros do Script

-   `scale_factor`: Define o tamanho da imagem de saída em relação à original.
    -   `0.5`: Reduz a imagem para 50% das dimensões (largura e altura).
    -   `0.1`: Reduz para 10% (usado para passar de 4 cm para 40 cm de resolução).
-   `resampling`: Define o algoritmo para calcular os novos valores de pixel. Os mais comuns são:
    -   `Resampling.bilinear`: (Padrão) Média ponderada dos 4 pixels vizinhos. Bom para dados contínuos (imagens, modelos de elevação).
    -   `Resampling.nearest`: Vizinho mais próximo. Preserva os valores originais dos pixels. Ideal para dados categóricos (ex: mapas de uso e cobertura do solo).
    -   `Resampling.cubic`: Interpolação cúbica dos 16 pixels vizinhos. Gera resultados mais suaves, mas é computacionalmente mais intenso.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ✍️ Como Citar

Se você utilizar este código em sua pesquisa, por favor, cite-o.

**Exemplo:**
> [Seu Nome]. ([Ano]). *Script de Reamostragem de Imagens Raster (GeoTIFF)* (Version [v1.0.0]) [Software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX


---
