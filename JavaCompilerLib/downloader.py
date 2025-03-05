# downloader.py
import requests

class JavaDownloader:
    @staticmethod
    def download(url: str, output_path: str):
        """Загружает файл по URL."""
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return True
        return False
