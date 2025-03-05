# project_manager.py
import os

class ProjectManager:
    @staticmethod
    def create_project(name: str):
        """Создает структуру нового Java-проекта."""
        os.makedirs(f"{name}/src", exist_ok=True)
        with open(f"{name}/src/Main.java", "w") as file:
            file.write('public class Main { public static void main(String[] args) { System.out.println("Hello, Java!"); }}')
        return f"Проект {name} создан."
