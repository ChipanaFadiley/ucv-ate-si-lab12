# Laboratorio UCV - Perceptron Simple

Implementacion desde cero de un perceptron simple para una aprobacion preliminar de creditos. El modelo usa dos entradas:

- Ingreso mensual, expresado en una escala numerica del laboratorio.
- Historial crediticio, donde `1` representa historial favorable y `0` historial desfavorable.

## Estructura

- `src/dataset.py`: datos de entrenamiento.
- `src/perceptron.py`: implementacion del perceptron simple.
- `main.py`: ejecucion de ejemplo.
- `tests/test_perceptron.py`: pruebas unitarias con pytest.
- `.github/workflows/build.yml`: CI con pruebas y analisis de SonarCloud.

## Ejecucion local

```bash
pip install -r requirements.txt
pytest --cov=src --cov=main --cov-report=xml
python main.py
```

En Windows PowerShell, si `pytest` no esta disponible como comando global, usa el modulo de Python del entorno virtual:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest --cov=src --cov=main --cov-report=xml
.\.venv\Scripts\python.exe main.py
```

## Preguntas de analisis

1. Los pesos representan la importancia de cada entrada en la decision final. En este caso, indican cuanto influyen el ingreso mensual y el historial crediticio.
2. El bias desplaza la frontera de decision. Permite que la neurona no dependa solo de las entradas ponderadas y ajuste mejor el punto desde el cual aprueba o rechaza.
3. El perceptron aprende comparando su prediccion con el valor esperado. Si se equivoca, calcula el error y actualiza pesos y bias usando la tasa de aprendizaje.
4. Un perceptron simple no puede resolver XOR porque XOR no es linealmente separable. No existe una sola recta que separe correctamente sus clases.
5. Un perceptron multicapa puede combinar varias fronteras de decision y aprender relaciones no lineales, por eso puede resolver problemas como XOR.

## Reto MIT: problema XOR

XOR devuelve `1` cuando sus dos entradas son diferentes y `0` cuando son iguales:

| Entrada A | Entrada B | Salida |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

El problema es que los puntos positivos `(0, 1)` y `(1, 0)` quedan en esquinas opuestas del plano, mientras que los negativos `(0, 0)` y `(1, 1)` ocupan las otras dos esquinas. Una sola recta no puede separarlos sin cometer errores.

Un perceptron multicapa si puede resolverlo porque usa una capa oculta. Por ejemplo, dos neuronas ocultas pueden aprender condiciones intermedias parecidas a OR y AND, y una neurona de salida puede combinarlas para producir XOR. Esa composicion permite formar una frontera no lineal.
