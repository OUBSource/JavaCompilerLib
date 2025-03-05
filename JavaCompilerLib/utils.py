# utils.py
import os

class Utils:
    @staticmethod
    def check_java_installed():
        """Проверяет, установлен ли Java."""
        return os.system("java -version") == 0

    @staticmethod
    def check_gradle_installed():
        """Проверяет, установлен ли Gradle."""
        return os.system("gradle -v") == 0
