#Autor: Dr. Aldo Gonzalez Vazquez
#Licence: MIT
#Version: 1.1
#Mini-Test-OOP class cuichapa, Ver.
import os

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
                "question": "4. ¿Que es una clase?",
                "options": [
                    "a) Código en lenguaje ensamblador",
                    "b) Es el plano del programa orientado a objetos",
                    "c) Código no optimizado",
                    "d) Código fuente incompleto"
                ],
                "answer": "b"
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
                    "b) pkg update",
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
                "question": "10. Es una subclase de hormiga",
                "options": [
                    "a) aroma",
                    "b) comida",
                    "c) reina",
                    "d) Colonia"
                ],
                "answer": "c"
            }
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_test(self):
        self.clear_screen()
        print("=== Test sobre Compiladores e Intérpretes ===\n")
        
        for i, q in enumerate(self.questions, 1):
            print(q["question"])
            for option in q["options"]:
                print(option)
            
            while True:
                user_answer = input("\nElige una opción (a/b/c/d): ").lower().strip()
                if user_answer in ['a', 'b', 'c', 'd']:
                    break
                print("Por favor ingresa una opción válida (a, b, c o d)")
            
            if user_answer == q["answer"]:
                self.score += 1
                print("✅ Correcto!")
            else:
                print(f"❌ Incorrecto! La respuesta correcta es {q['answer']}")
            
            input("\nPresiona Enter para continuar...")
            self.clear_screen()
        
        self.show_results()

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
    test = CompilersTest()
    test.run_test()
