import unittest
from unittest.mock import patch
import openai


class TestOpenaiScript(unittest.TestCase):

    def test_GPT(self):
        question = "如何获得璃月丸"
        expected_answer = "```cypher\nMATCH (m:Material {name: \"璃月丸\"})\nMATCH (m)<-[:Material]-(p:Promote)<-[:Promote]-(c:Character)\nRETURN c.name\n```"
        with patch.dict('os.environ', {'gpt_key': 'test_key'}):
            actual_answer = openai.GPT(question)
        self.assertEqual(actual_answer, expected_answer)


if __name__ == '__main__':
    unittest.main()