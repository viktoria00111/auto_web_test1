import time

import pytest
from testpage import OperationHelper

username = '1stud'
password = 'ef080ce410'


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login('1stud')
    test_page1.enter_pswd('ef080ce410')
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_cont_name("Konstantin")
    test_page1.enter_cont_email("konstantin_test_mail@gmail.com")
    test_page1.enter_cont_text("Hey, this is text message")
    time.sleep(1)

    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"



