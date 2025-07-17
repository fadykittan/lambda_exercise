import unittest
from simple_lambda_cicd.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler_returns_expected_response(self):
        event = {}
        context = None
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '"Hello World! from Lambda with CICD!"')

if __name__ == '__main__':
    unittest.main()
