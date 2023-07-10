from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@given('el usuario está registrado')
def step_impl(context):
   pass


@when('cuando introduce un nombre de usuario')
def step_impl(context):
   context.driver.find_element(By.ID, "username").send_keys("tomsmith")


@when('cuando introduce un nombre falso de usuario')
def step_impl(context):
   context.driver.find_element(By.ID, "username").send_keys("sdasdf")


@when('cuando introduce su password')
def step_impl(context):
   context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")


@when('el usuario pulsa "Login"')
def step_impl(context):
   context.driver.find_element(By.CSS_SELECTOR, "#login > button").click()


@then('el usuario accede al portal')
def step_impl(context):
   try:
      assert context.driver.find_element(By.CSS_SELECTOR, "#content > div > a:nth-child(3)").is_displayed(), "no se ve el boton logout"
   except NoSuchElementException as e:
      raise AssertionError("no se ve el boton logout")


@then('el usuario no accede al portal')
def step_impl(context):
   try:
      assert not context.driver.find_element(By.CSS_SELECTOR, "#content > div > a:nth-child(3)").is_displayed(), "no se ve el boton logout"
   except NoSuchElementException as e:
      pass