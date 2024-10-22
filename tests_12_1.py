import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):

        obj = runner.Runner('Junior')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):

        obj1 = runner.Runner('Sprinter')
        for i in range(10):
            obj1.run()
        self.assertEqual(obj1.distance, 100)

    def test_challenge(self):

        obj2 = runner.Runner("Elephant")
        obj3 = runner.Runner("Leopard")
        for i in range(10):
            obj2.walk()
            obj3.run()
        self.assertNotEqual(obj2.distance, obj3.distance)


if __name__ == "__main__":
    unittest.main()