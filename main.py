from src.perceptron import Perceptron
from src.dataset import training_data


def main() -> None:
    model = Perceptron()
    model.train(training_data)

    prediction = model.predict([9, 1])
    print(prediction)


if __name__ == "__main__":
    main()
