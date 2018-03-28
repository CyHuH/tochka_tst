from settings import CAPABILITIES, APPIUM_SERVER
from appium import webdriver
from elements.base_elements import BaseElements


def before_all(context):
    context.driver = webdriver.Remote(
        command_executor=APPIUM_SERVER,
        desired_capabilities=CAPABILITIES)
    context.driver.implicitly_wait(3000)


def before_scenario(context, scenario):
    context.base_elements = BaseElements(context.driver)


def after_all(context):
    context.driver.quit()
