from page_objects import PageObject, PageElement, MultiPageElement


class BaseElements(PageObject):
    favorite_buttons = MultiPageElement(id_='com.avito.android:id/btn_favorite')
    product_titles = MultiPageElement(id_='com.avito.android:id/title')
    search_bar = PageElement(id_='com.avito.android:id/search_current_query')
    search_input = PageElement(id_='com.avito.android:id/search_edit_text')
    menu_or_back_button = PageElement(id_='//android.view.ViewGroup[@resource-id="com.avito.android:id/toolbar"]/android.widget.ImageButton')
    favorites_menu = PageElement(id_='com.avito.android:id/btn_favorites')
