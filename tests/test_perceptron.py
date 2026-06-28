import unittest

from src.perceptron import Perceptron
from src.dataset import training_data


class TestPerceptron(unittest.TestCase):
    def test_accepts_customer_with_high_income_and_good_history(self):
        model = Perceptron()
        model.train(training_data)
        self.assertEqual(model.predict([8, 1]), 1)

    def test_rejects_customer_with_low_income_and_bad_history(self):
        model = Perceptron()
        model.train(training_data)
        self.assertEqual(model.predict([1, 0]), 0)

    def test_learns_all_training_examples(self):
        model = Perceptron()
        model.train(training_data)

        for inputs, expected in training_data:
            self.assertEqual(model.predict(inputs), expected)

    def test_predict_rejects_invalid_input_size(self):
        model = Perceptron()

        with self.assertRaisesRegex(ValueError, "Se esperaban 2 entradas"):
            model.predict([8])
