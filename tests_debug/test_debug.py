import pytest
import time
from base.base_test import BaseTest

class TestDebug(BaseTest):


    def test_debug(self, driver, request: pytest.FixtureRequest):
        print(f"\nSTART {request.node.name}")
        # driver.get("https://beta2.syncwise360.com/login")
        # request.cls.driver.get("https://beta2.syncwise360.com/login")
        print(self.it_is_my_test)

        print(f"\nFINISH {request.node.name}")
        time.sleep(3)
