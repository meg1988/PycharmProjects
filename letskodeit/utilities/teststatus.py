from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self,driver):
        super(TestStatus,self).__init__(driver)
        self.resultList = []

    def setResult(self,testName, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL for TestCase ::" + testName +" with :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED for TestCase ::" + testName +" with :: " + resultMessage)
                    self.screenShot(testName,resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED for TestCase ::" + testName +" with :: " + resultMessage)
                self.screenShot(testName, resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception occurred !!!")
            self.screenShot(testName, resultMessage)
            print_stack()

    def mark(self, testName, result, resultMessage):
        self.setResult(testName, result,resultMessage)


    def markFinal(self, testName, result, resultMessage):
        self.setResult(testName,result,resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " : ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " : ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
