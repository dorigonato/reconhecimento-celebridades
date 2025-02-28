from pathlib import Path
import boto3
from PIL import Image, ImageDraw, ImageFont

# Inicializa o cliente AWS Rekognition
client = boto3.client("rekognition")

def get_path(file_name: str) -> str:
    """Retorna o caminho completo do arquivo na pasta images."""
    return str(Path(__file__).parent / "images" / file_name)

def recognize_celebrities(photo: str):
    """Envia a imagem para o AWS Rekognition e retorna as celebridades reconhecidas."""
    with open(photo, "rb") as image:
        return client.recognize_celebrities(Image={"Bytes": image.read()})

def draw_boxes(image_path: str, output_path: str, face_details: list):
    """Desenha caixas vermelhas ao redor dos rostos das celebridades reconhecidas."""
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # Substituído por Arial
    except IOError:
        font = ImageFont.load_default()  # Usa fonte padrão se Arial não estiver disponível
    
    width, height = image.size

    for face in face_details:
        box = face["Face"]["BoundingBox"]
        left = int(box["Left"] * width)
        top = int(box["Top"] * height)
        right = int((box["Left"] + box["Width"]) * width)
        bottom = int((box["Top"] * height) + (box["Height"] * height))

        confidence = face.get("MatchConfidence", 0)
        if confidence > 90:
            draw.rectangle([left, top, right, bottom], outline="red", width=3)

            text = face.get("Name", "")
            text_size = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = text_size[2] - text_size[0], text_size[3] - text_size[1]
            text_position = (left, max(0, top - text_height - 5))
            draw.rectangle([text_position, (text_position[0] + text_width, text_position[1] + text_height)], fill="red")
            draw.text(text_position, text, font=font, fill="white")

    image.save(output_path)
    print(f"Imagem salva com resultados em: {output_path}")
    
"""O código agora processa todas as imagens .jpg na pasta images,
    eliminando a necessidade de listar arquivos manualmente"""
if __name__ == "__main__":
    image_dir = Path(__file__).parent / "images"
    photo_paths = list(image_dir.glob("*.jpg"))  # Busca todas as imagens JPG na pasta
    
    if not photo_paths:
        print("Nenhuma imagem encontrada na pasta images.")
    
    for photo_path in photo_paths:
        response = recognize_celebrities(str(photo_path))
        faces = response.get("CelebrityFaces", [])
        
        if not faces:
            print(f"Nenhuma celebridade encontrada na imagem: {photo_path}")
            continue

        output_path = photo_path.with_name(f"{photo_path.stem}-resultado.jpg")
        draw_boxes(str(photo_path), str(output_path), faces)
