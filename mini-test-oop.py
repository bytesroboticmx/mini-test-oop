#Autor: Dr. Aldo Gonzalez Vazquez
#Licence: MIT
#Version: 1.2
#Mini-Test-basic 
import os

REQUIRED_KEYS = ("question", "options", "answer")
VALID_ANSWERS = ("a", "b", "c", "d")

class CompilersTest:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "1. ¿Qué es Termux?",
                "options": [
                    "a) Un programa que ejecuta código línea por línea",
                    "b) Un programa que emula una consola de comandos",
                    "c) Un programa que solo verifica errores sintácticos",
                    "d) Un programa que optimiza hardware"
                ],
                "answer": "b"
            },
            {
                "question": "2. ¿Cual es el comando para ver archivos y carpetas?",
                "options": [
                    "a) man",
                    "b) cat",
                    "c) ls",
                    "d) mkdir"
                ],
                "answer": "c"
            },
            {
                "question": "3. ¿Cual es el comando para cambiar de carpeta?",
                "options": [
                    "a) nmap",
                    "b) cd",
                    "c) man",
                    "d) char"
                ],
                "answer": "b"
            },
            {
                "question": "4. Son las operaciones basicas con numeros enteros",
                "options": [
                    "a) Código en lenguaje ensamblador",
                    "b) Es el plano del programa orientado a objetos",
                    "c) Sumar, restar, multiplicar, dividir",
                    "d) Código fuente incompleto"
                ],
                "answer": "c"
            },
            {
                "question": "5. ¿Que es python:",
                "options": [
                    "a) Solo compilación",
                    "b) Solo interpretación",
                    "c) Lenguaje de programacion de alto nivel",
                    "d) Ejecución directa del código fuente"
                ],
                "answer": "c"
            },
            {
                "question": "6. ¿Cual es el comando para actualizar el sistema en Termux?",
                "options": [
                    "a) apt purge",
                    "b) pkg update && pkg upgrade",
                    "c) pkg install",
                    "d) dnf update"
                ],
                "answer": "b"
            },
            {
                "question": "7. Es un programa de gestion de versiones, utilizado en Termux.",
                "options": [
                    "a) mercury",
                    "b) git",
                    "c) svn",
                    "d) vim"
                ],
                "answer": "b"
            },
            {
                "question": "8. Es el comando para verificar la instalacion de python3",
                "options": [
                    "a) git --version",
                    "b) python -V",
                    "c) python2 --h",
                    "d) python main.py"
                ],
                "answer": "b"
            },
            {
                "question": "9. Comando para crear una carpeta",
                "options": [
                    "a) mkdir",
                    "b) cd",
                    "c) cat",
                    "d) carpet"
                ],
                "answer": "a"
            },
            {
                "question": "10. Comando para cambiar de repositorio en Termux",
                "options": [
                    "a) repo-load",
                    "b) load-server",
                    "c) termux-change-repo",
                    "d) Access denied"
                ],
                "answer": "c"
            }
        ]

        self.validate_questions()

    def validate_questions(self):
        if not isinstance(self.questions, list) or not self.questions:
            raise ValueError("La lista de preguntas no es válida o está vacía")

        for i, q in enumerate(self.questions, 1):
            if not isinstance(q, dict):
                raise TypeError(f"La pregunta {i} no es un diccionario")

            missing = [k for k in REQUIRED_KEYS if k not in q]
            if missing:
                raise KeyError(f"La pregunta {i} no tiene las claves requeridas: {missing}")

            if not isinstance(q["question"], str) or not q["question"].strip():
                raise ValueError(f"La pregunta {i} tiene un enunciado vacío")

            options = q["options"]
            if not isinstance(options, (list, tuple)) or len(options) != 4:
                raise ValueError(f"La pregunta {i} debe tener exactamente 4 opciones")

            for j, opt in enumerate(options, 1):
                if not isinstance(opt, str) or not opt.strip():
                    raise ValueError(f"La pregunta {i} tiene la opción {j} inválida")

            answer = q["answer"]
            if answer not in VALID_ANSWERS:
                raise ValueError(f"La pregunta {i} tiene una respuesta inválida: '{answer}'")

            option_index = VALID_ANSWERS.index(answer)
            if not options[option_index].strip().startswith(f"{answer})"):
                raise ValueError(
                    f"La pregunta {i} tiene la opción '{answer}' mal etiquetada"
                )

    def clear_screen(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except OSError:
            print("\n" * 2)

    def run_test(self):
        try:
            self.clear_screen()
            print("=== Test basico sobre computacion y termux ===\n")

            for q in self.questions:
                print(q["question"])
                for option in q["options"]:
                    print(option)

                try:
                    user_answer = self._get_answer()
                except (EOFError, KeyboardInterrupt):
                    print("\nEntrada interrumpida. Saliendo del test.")
                    break

                if user_answer == q["answer"]:
                    self.score += 1
                    print("✅ Correcto!")
                else:
                    print(f"❌ Incorrecto! La respuesta correcta es {q['answer']}")

                try:
                    input("\nPresiona Enter para continuar...")
                except (EOFError, KeyboardInterrupt):
                    print("\nEntrada interrumpida. Saliendo del test.")
                    break
                self.clear_screen()

            self.show_results()
        except Exception as e:
            print(f"Error inesperado durante el test: {e}")

    def _get_answer(self):
        while True:
            try:
                user_answer = input("\nElige una opción (a/b/c/d): ").lower().strip()
            except (EOFError, KeyboardInterrupt):
                raise
            if user_answer in VALID_ANSWERS:
                return user_answer
            print("Por favor ingresa una opción válida (a, b, c o d)")

    def show_results(self):
        print("=== Resultados ===")
        print(f"Puntuación final: {self.score}/10")
        if self.score >= 9:
            print("🎉 Excelente!")
        elif self.score >= 7:
            print("👍 Buen trabajo!")
        elif self.score >= 5:
            print("😐 Puedes mejorar")
        else:
            print("📚 Debes repasar el tema")

if __name__ == "__main__":
    try:
        test = CompilersTest()
        test.run_test()
    except (EOFError, KeyboardInterrupt):
        print("\n\nTest interrumpido. Hasta pronto!")
    except Exception as e:
        print(f"\nError al iniciar el test: {e}")
