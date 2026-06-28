from collections.abc import Sequence

TrainingExample = tuple[Sequence[float], int]


class Perceptron:
    """Perceptron simple para clasificacion binaria."""

    def __init__(self, learning_rate: float = 0.1) -> None:
        self.weights = [0.0, 0.0]
        self.bias = 0.0
        self.learning_rate = learning_rate

    def activation(self, value: float) -> int:
        return 1 if value >= 0 else 0

    def predict(self, inputs: Sequence[float]) -> int:
        if len(inputs) != len(self.weights):
            msg = (
                f"Se esperaban {len(self.weights)} entradas, "
                f"pero se recibieron {len(inputs)}."
            )
            raise ValueError(msg)

        total = self.bias

        for value, weight in zip(inputs, self.weights):
            total += value * weight

        return self.activation(total)

    def train(self, training_data: Sequence[TrainingExample], epochs: int = 20) -> None:
        for _ in range(epochs):
            for inputs, expected in training_data:
                prediction = self.predict(inputs)
                error = expected - prediction

                for index, input_value in enumerate(inputs):
                    self.weights[index] += self.learning_rate * error * input_value

                self.bias += self.learning_rate * error
