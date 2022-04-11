pytest_plugins = [
    "ecommerce.tests.fixtures",  # This fixtures has to load before another plugins to populate data in test database.
    "ecommerce.tests.selenium"
]