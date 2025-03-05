#compiler
import subprocess

class JavaCompiler:
    @staticmethod
    def compile(java_file: str):
        """Компилирует Java-файл и возвращает вывод в stdout и stderr."""
        try:
            # Запуск компиляции с помощью javac
            result = subprocess.run(
                ["javac", java_file],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                # Если компиляция не удалась, возвращаем stderr
                return "", result.stderr
            # Если компиляция успешна, возвращаем stdout и пустой stderr
            return result.stdout, ""

        except FileNotFoundError:
            # Если команда javac не найдена, возвращаем ошибку
            return "", "javac не найден. Убедитесь, что Java установлен и доступен в PATH."
        except Exception as e:
            # В случае других ошибок возвращаем сообщение об исключении
            return "", str(e)

    @staticmethod
    def run(class_name: str):
        """Запускает скомпилированный Java-класс и возвращает вывод в stdout и stderr."""
        try:
            # Запуск скомпилированного Java-класса
            result = subprocess.run(
                ["java", class_name],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                # Если возникла ошибка при выполнении программы, возвращаем stderr
                return "", result.stderr
            # Если выполнение успешно, возвращаем stdout и пустой stderr
            return result.stdout, ""

        except FileNotFoundError:
            # Если команда java не найдена, возвращаем ошибку
            return "", "java не найден. Убедитесь, что Java установлен и доступен в PATH."
        except Exception as e:
            # В случае других ошибок возвращаем сообщение об исключении
            return "", str(e)
