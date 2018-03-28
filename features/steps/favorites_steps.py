from behave import given, when, then, use_step_matcher

use_step_matcher('re')


def get_titles(selector):
    return [selector[i].text for i in range(len(selector))]


@given('Ищем по запросу (?P<request>.+)')
def _(context, request):
    context.base_elements.search_bar.click()
    context.base_elements.search_input.send_keys(request + ' \n')


@when('Добавляем в избранное')
def _(context):
    for i in range(len(context.base_elements.favorite_buttons)):
        context.base_elements.favorite_buttons[i].click()


@then('Запоминаем тайтлы объявлений')
def _(context):
    # свайпим, чтобы подгрузились тайтлы, которые не влезли в экран
    context.driver.swipe(200, 450, 200, 100)
    context.titles = get_titles(context.base_elements.product_titles)


@then('Открываем раздел избранного')
def _(context):
    context.driver.swipe(1, 200, 500, 200)
    context.base_elements.favorites_menu.click()


@then('Проверяем, что избранное добавилось')
def _(context):
    favorites_titles = get_titles(context.base_elements.product_titles)
    for i in range(len(context.titles)):
        assert context.titles[i] in favorites_titles, '{0} is not in {1}'.format(context.titles[i], favorites_titles)


@then('Удаляем элемент из избранного и проверяем, что его нет')
def _(context):
    current_titles = get_titles(context.base_elements.product_titles)
    context.base_elements.favorite_buttons[0].click()
    new_titles = get_titles(context.base_elements.product_titles)
    # проверяем, что элемент удалился
    assert current_titles[0] not in new_titles, '{0} in {1}'.format(current_titles[0], new_titles)
    # проверяем, что остальные элементы остались
    for i in range(len(new_titles)):
        assert new_titles[i] in current_titles, '{0} is not in {1}'.format(new_titles[i], current_titles)
