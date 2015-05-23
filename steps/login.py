#coding=utf-8

from nose.tools import *
from behave import *

package_id = "com.seabornlee.robolectricdemo"

@given(u'我在{text_field_id}输入{text}')
def step_impl(context, text_field_id, text):
    text_field = context.driver.find_element_by_id(package_id + ":id/et_" + text_field_id)
    text_field.send_keys(text)

@when(u'我点击{text_on_button}按钮')
def step_impl(context, text_on_button):
    context.driver.find_element_by_id(package_id + ":id/btn_" + text_on_button).click()


@then(u'我应该看到{label_id}是{expected_text}')
def step_impl(context, label_id, expected_text):
    text = context.driver.find_element_by_id(package_id + ":id/" + label_id).text
    eq_(expected_text, text)

