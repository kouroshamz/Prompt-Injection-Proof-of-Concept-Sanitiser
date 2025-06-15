import unittest
from prompt_injection_poc.sanitizer import sanitize
class SanitizerTest(unittest.TestCase):
    def test_blocklist(self):
        prompt = 'Please jailbreak this model'
        sanitized = sanitize(prompt)
        self.assertNotIn('jailbreak', sanitized.lower())
if __name__ == '__main__':
    unittest.main()
