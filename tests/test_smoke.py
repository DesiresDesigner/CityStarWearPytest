from functools import reduce

from base.driver_manager import DriverManager
from pages.page.cart_page import CartPage
from pages.page.main_page import MainPage
from pages.page.order_page import OrderPage
from pages.page.products_page import ProductsPage
from pages.page.product_page import ProductPage


def test_smoke():
    # DRIVER INIT
    options = [
        ("detach", True)
    ]

    driver_manager = DriverManager("chrome", options)
    driver_manager.create_driver("https://citystarwear.com/")


    # DATA FOR TEST INIT
    products_to_buy = [
        { "catalog_item": "Теплые платья", "product_name": "Утепленное платье \"Phoenix\""},
        {"catalog_item": "Комбинезоны", "product_name": "Комбинезон женский \"Oasis\""},
    ]
    products_info = []
    product_page_object = None

    # MAIN PAGE
    main_page_object = MainPage(driver_manager)
    main_page_object.close_popbox_if_exit()

    # ADD PRODUCTS TO CART
    current_page = main_page_object
    for serial_number, product_to_buy in enumerate(products_to_buy):
        #   Choosing catalog item
        current_page.open_catalog_menu()
        current_page.choose_catalog_menu_item(name=product_to_buy["catalog_item"])

        # PRODUCTS PAGE BY CATEGORY
        products_page_object = ProductsPage(driver_manager)
        assert products_page_object.get_title() == product_to_buy["catalog_item"]
        print(f'LOG: products page of expected category({product_to_buy["catalog_item"]}) opened')

        products_info.append(products_page_object.open_product(name=product_to_buy["product_name"]))
        product_page_object = ProductPage(driver_manager)
        assert product_page_object.get_name() == products_info[-1]["name"]
        print("LOG: page of expected product opened")

        assert product_page_object.get_price() == products_info[-1]["price"]
        print(f'LOG: product has expected name({products_info[-1]["name"]}) and price({products_info[-1]["price"]})')

        product_page_object.add_to_cart()
        print("LOG: 'add to cart' button applied")

        current_page = product_page_object

    # COUNT EXPECTED TOTAL PRICE
    total_price_before_delivery = reduce(
        lambda acc, x: acc + x['price'],
        products_info,
        0
    )

    # CART PAGE
    product_page_object.open_cart()
    cart_page_object = CartPage(driver_manager)
    assert "Корзина" in cart_page_object.get_title()
    print("LOG: cart successfully opened")

    # ASSERTION: names and prices of products
    for serial_number, product in enumerate(products_info):
        assert cart_page_object.get_products()[serial_number].get_name() == product['name']
        assert cart_page_object.get_products()[serial_number].get_price() == product['price']
        print(f'LOG: product with expected name({product["name"]}) and price({product["price"]}) is in cart')

    print("LOG: all expected products are in cart")

    # ASSERTION: total prices
    assert cart_page_object.get_price_before_promo() == total_price_before_delivery
    assert cart_page_object.get_price_after_promo() == total_price_before_delivery
    print(f'LOG: total price has expected value({total_price_before_delivery})')

    cart_page_object.continue_ordering()

    # ORDER PAGE
    order_page_object = OrderPage(driver_manager)
    assert "Оформление заказа" in order_page_object.get_title()
    print("LOG: order page successfully opened")

    # ASSERTION: names and prices of products
    for serial_number, product in enumerate(products_info):
        assert order_page_object.get_products()[serial_number].get_name() == product['name']
        assert order_page_object.get_products()[serial_number].get_price() == product['price']
        print(f'LOG: product with expected name({product["name"]}) and price({product["price"]}) is in order')

    print("LOG: all expected products are in order")
    # ASSERTION: total prices
    assert order_page_object.get_price_before_delivery() == total_price_before_delivery
    print(f'LOG: total price before delivery has expected value({total_price_before_delivery})')

    delivery_price = order_page_object.get_delivery_price()
    total_price_after_delivery = total_price_before_delivery + delivery_price
    assert order_page_object.get_price_after_delivery() == total_price_after_delivery
    print(f'LOG: total price after delivery has expected value({total_price_after_delivery})')

    driver_manager.close_driver()
