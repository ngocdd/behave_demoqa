from behave import *


@given("go to home page")
def step_impl(context):
    context.browser.get('https://demoqa.com')


@given(u'go to text box page')
def step_impl(context):
    context.home_page.click_on_element("elements")
    context.element_page.click_on_element("text box")


@given(u'input Full Name {full_name}')
def step_impl(context, full_name):
    context.element_page.input_text("full name", full_name)
    context.name = full_name
    # print(full_name + "++")


@step("input Email {email}")
def step_impl(context, email):
    context.email = email
    context.element_page.input_text("email", email)


@step("input Current Address {current_address}")
def step_impl(context, current_address):
    context.current_address = current_address
    context.element_page.input_text("current address", current_address)


@step("input Permanent Address {permanent_address}")
def step_impl(context, permanent_address):
    context.permanent_address = permanent_address
    context.element_page.input_text("permanent address", permanent_address)


@step("click submit button")
def step_impl(context):
    context.element_page.click_on_element("submit button")


@step("check value get from text area")
def step_impl(context):
    result = context.element_page.get_element_text("result area")
    input_value = [context.name, context.email, context.permanent_address, context.current_address]
    for i in input_value:
        assert i in result


@step("input invalid Email {email}")
def step_impl(context, email):
    context.element_page.input_text("email", email)


@then("check validate wrong email")
def step_impl(context):
    result = context.element_page.get_element_attribute("email", "class")
    assert "field-error form-control" in result


@given("go to check box page")
def step_impl(context):
    context.home_page.click_on_element("elements")
    context.element_page.click_on_element("check box")


@step("click on check all")
def step_impl(context):
    context.element_page.click_on_element("home")


@step("click expand all")
def step_impl(context):
    print("")


@then("check status of all children check boxes")
def step_impl(context):
    rs = context.element_page.get_element_attribute("home", "class")
    assert "rct-icon-check" in rs
