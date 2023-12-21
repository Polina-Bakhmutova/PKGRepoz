import os
from PIL import Image

def process_image(file_path):
    try:
        img = Image.open(file_path)

        image_info = {
            "Имя файла": os.path.basename(file_path),
            "Размер изображения (в пикселях)": img.size,
            "Разрешение (dot/inch)": img.info.get("dpi", "N/A"),
            "Глубина цвета": img.mode,
            "Сжатие": img.info.get("compression", "N/A"),
        }

        return image_info
    except Exception as e:
        return {"Имя файла": os.path.basename(file_path), "Ошибка": str(e)}

def process_folder(folder_path):
    image_info_list = []

    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        image_info = process_image(file_path)
        image_info_list.append(image_info)

    return image_info_list

if __name__ == "__main__":
    folder_path = "C:\\Users\\Home\\PycharmProjects\\laba2prob1"


    result = process_folder(folder_path)

    for item in result:
        for key, value in item.items():
            print(f"{key}: {value}")
        print("=" * 40)

#реализовать оконное приложение и возмоджность выбора папки