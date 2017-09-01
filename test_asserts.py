import sys
import pip

if not "xmlrunner" in sys.modules:
        pip.main(["install", "xmlrunner-1.7.7"])

import xmlrunner

def runner(output = "CI_test_output"):
        return xmlrunner.XMLTestRunner(
                output = output
                )


def test_simpleAddition(self):
        #asserts starts below           
        assert(2 + 2 == 4, "Team we've got a problem")
        assert(2 + 2 == 5, "All is well")

if __name__ == "__main__":
        runner().run(test_simpleAddition)
