import rasterio
from rasterio.enums import Resampling

# Caminho para o arquivo TIFF de entrada
input_path = ""

# Caminho para o arquivo TIFF de saída
output_path = ""

# Fator de escala (ex: 0.5 = reduz pela metade)
scale_factor = 0.1

with rasterio.open(input_path) as src:
    # Calcula novas dimensões
    new_width = int(src.width * scale_factor)
    new_height = int(src.height * scale_factor)

    # Redimensiona todas as bandas
    data = src.read(
        out_shape=(src.count, new_height, new_width),
        resampling=Resampling.bilinear
    )

    # Ajusta a transformação espacial
    new_transform = src.transform * src.transform.scale(
        src.width / new_width,
        src.height / new_height
    )

    # Escreve nova imagem mantendo metadados
    with rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=new_height,
        width=new_width,
        count=src.count,
        dtype=data.dtype,
        crs=src.crs,
        transform=new_transform
    ) as dst:
        dst.write(data)

print("Redimensionamento completo!")
