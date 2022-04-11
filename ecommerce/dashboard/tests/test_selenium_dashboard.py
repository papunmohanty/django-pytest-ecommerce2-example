import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from django.contrib.auth.models import User


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server, db_fixture_setup, chrome_browser_instance
):
    # user = User.objects.get(id=1)
    # print(f"Username: {user.username}")
    # print(f"Password: {user.password}")

    browser = chrome_browser_instance

    browser.get((f"{live_server.url}/admin/login"))
    # browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
