import time
from pages.ClothesCategory import ClothesCategory
from pages.MainPage import MainPage
from pages.ShippingAddress import ShippingAddress


def test_count_men_clothes(chrome):
    main_page = MainPage(chrome)
    category = ClothesCategory(chrome)
    shipping = ShippingAddress(chrome)
    main_page.hide_sticky_box("ea-stickybox-hide")
    main_page.select_from_menu(main_page.men_menu_locator("ui-id-5"),
                               main_page.men_tops_locator("ui-id-17"),
                               main_page.men_hoodies_sweatshirts_locator("ui-id-20"))
    count = category.show_per_page(12, '12')
    product = category.men_product_item_list(2)
    assert count == product
    category.click_on_item("//div[@class='product details product-item-details']/*/*"
                           "[contains(text(), 'Frankie Sweatshirt')]")
    category.select_size(3, "(//div[@aria-describedby='option-label-size-143'])[2]")
    category.select_color(3, "(//div[@aria-describedby='option-label-color-93'])[1]")
    category.add_quantity("qty", "2")
    category.button_add_to_cart("//button[@class='action primary tocart']")
    item_added = category.cart_counter(4,
                                       "2",
                                       "//a[@class='action showcart']/*/*[@class='counter-number']")
    assert item_added == "2"
    category.click_on_cart("minicart-wrapper")
    item_quantity_is_the_same = category.get_attribute("//div[@class='details-qty qty']/*[@data-item-qty='2']",
                                                       "data-item-qty")
    assert item_quantity_is_the_same == "2"
    category.click_on_item("//div[@class='product options']")
    item_size_is_the_same = category.cart_counter(4,
                                             "S",
                                             "//dl[@class='product options list']/*/*[contains(text(), 'S')]")
    assert item_size_is_the_same == "S"
    item_color_is_the_same = category.cart_counter(4,
                                            "Green",
                                            "//dl[@class='product options list']/*/*[contains(text(), 'Green')]")
    assert item_color_is_the_same == "Green"
    category.button_proceed_to_checkout("top-cart-btn-checkout")
    shipping.insert_data(4,"(//input[@id='customer-email'])[1]", "jk@gmail.com")
    shipping.insert_data(4,"//input[@name='firstname']", "John")
    shipping.insert_data(4,"//input[@name='lastname']", "Travolta")
    shipping.insert_data(4,"//input[@name='company']", "twoday")
    shipping.insert_data(4,"//input[@name='street[0]']", "Giedraiciu-3")
    shipping.find_element_with_action(4,"//input[@name='city']")
    shipping.insert_data(2, "//input[@name='city']", "Vilnius")
    time.sleep(5)
    shipping.find_element_with_action(4, "//input[@name='postcode']")
    shipping.insert_data(2, "//input[@name='postcode']", 123456)
    shipping.find_element_with_action(4, "//input[@name='telephone']")
    shipping.insert_data(2, "//input[@name='telephone']", 1234567)
    shipping.scroll_to_element(4, "//select[@name='region_id']", "Alaska")
    time.sleep(3)
    shipping.scroll_to_element(4, "//select[@name='country_id']", "Lithuania")
    shipping.find_element_with_action(4, "(//input[@class='radio'])[2]")
    category.click_on_item("(//input[@class='radio'])[2]")
    time.sleep(5)

    category.click_on_item("//button[@class='button action continue primary']")
    time.sleep(5)

    category.click_on_item("//button[@class='action primary checkout']")
    time.sleep(5)




def test_count_women_cart(chrome):
    main_page = MainPage(chrome)
    category = ClothesCategory(chrome)
    main_page.hide_sticky_box("ea-stickybox-hide")
    main_page.select_from_menu(main_page.women_menu_locator("ui-id-4"),
                               main_page.women_bottoms_locator("ui-id-10"),
                               main_page.women_pants_locator("ui-id-15"))
    category.sort_by_cheapest(2, "(//select[@id='sorter']/*[@value='price'])[1]")
    main_page.hide_sticky_box("ea-stickybox-hide")
    category.select_clothes(3,"product-price-1819")
    category.select_size(3,"(//div[@id='option-label-size-143-item-171'])[1]")
    category.select_color(3,"(//div[@id='option-label-color-93-item-49'])[1]")
    category.button_add_to_cart("(//button[@class='action tocart primary'])[1]")
    first_item = category.cart_counter(4,
                                       "1",
                                       "//a[@class='action showcart']/*/*[@class='counter-number']")
    assert first_item == "1"
    category.select_clothes(4,"product-price-1826")
    category.select_size(4,"(//div[@id='option-label-size-143-item-171'])[3]")
    category.select_color(4,"(//div[@id='option-label-color-93-item-57'])[1]")
    category.button_add_to_cart("(//button[@class='action tocart primary'])[3]")
    second_item = category.cart_counter(4,
                                        "2",
                                        "//a[@class='action showcart']/*/*[@class='counter-number']")
    assert second_item == "2"
    category.select_clothes(4, "product-price-1833")
    category.select_size(4, "(//div[@id='option-label-size-143-item-171'])[6]")
    category.select_color(4, "(//div[@id='option-label-color-93-item-49'])[4]")
    category.button_add_to_cart("(//button[@class='action tocart primary'])[6]")
    third_item = category.cart_counter(4,
                                       "3",
                                       "//a[@class='action showcart']/*/*[@class='counter-number']")
    assert third_item == "3"
    category.click_on_cart("minicart-wrapper")
    category.remove_from_cart("(//a[@title='Remove item'])[3]")
    category.click_pop_up('.action-primary.action-accept')
    after_one_remove = category.cart_counter(4,
                                         "2",
                                         "//a[@class='action showcart active']/*/*[@class='counter-number']")
    assert after_one_remove == "2"
    category.button_proceed_to_checkout("top-cart-btn-checkout")