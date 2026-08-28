# mini-test-oop

Mini test interactivo de consola sobre **Programación Orientada a Objetos**, comandos y conceptos de **Termux**, desarrollado en Python.

## Descripción

El programa presenta **10 preguntas de opción múltiple** (a, b, c, d). El usuario responde cada pregunta en la terminal, recibe retroalimentación inmediata y, al terminar, se muestra la puntuación final con un mensaje según el desempeño.

Está pensado como material de repaso y evaluación para estudiantes de fundamentos de programación.

## Estructura del programa

El programa se organiza en una única clase `CompilersTest` con los siguientes componentes:

| Componente | Tipo | Descripción |
|---|---|---|
| `REQUIRED_KEYS` | Constante | Claves obligatorias en cada pregunta (`question`, `options`, `answer`) |
| `VALID_ANSWERS` | Constante | Respuestas válidas admitidas (`a`, `b`, `c`, `d`) |
| `CompilersTest` | Clase | Encapsula la lógica del test |
| `__init__` | Método | Inicializa puntuación, define las 10 preguntas y valida su estructura |
| `validate_questions` | Método | Valida estructura de preguntas (enunciado, 4 opciones, respuesta y etiquetas) |
| `clear_screen` | Método | Limpia la consola (Windows/Linux/macOS) |
| `run_test` | Método | Orquesta el flujo principal del test |
| `_get_answer` | Método | Lee y valida la respuesta del usuario |
| `show_results` | Método | Muestra la puntuación final y un mensaje de desempeño |

### Flujo de ejecución

```
main → CompilersTest() → validate_questions()
          ↓
      run_test → clear_screen()
          ↓
      bucle por pregunta →
          _get_answer() → evaluación → continuar (Enter)
          ↓
      show_results()
```

### Manejo de excepciones

| Excepción | Lugar | Comportamiento |
|---|---|---|
| `ValueError`, `TypeError`, `KeyError` | `validate_questions` | Verifican la integridad de las preguntas |
| `OSError` | `clear_screen` | Fallback: imprime líneas en blanco |
| `EOFError`, `KeyboardInterrupt` | `_get_answer` y `run_test` | Salida controlada del test |
| `Exception` | `run_test` y `__main__` | Captura errores inesperados |

## Criterios de evaluación

- **9–10** -> Excelente
- **7–8** -> Buen trabajo
- **5–6** -> Puedes mejorar
- **0–4** -> Debes repasar el tema

## Requisitos

- Python 3

## Uso

```bash
python mini-test-oop.py
```

## Autor y licencia

- **Autor:** Dr. Aldo Gonzalez Vazquez
- **Licencia:** MIT
- **Versión:** 1.1