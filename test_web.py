from selenium.webdriver.common.by import By
import pytest
import json
from context.WebTestContext import WebTestContext


class TestApi(WebTestContext):
    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[1]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_get_list_users_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_get_list_users

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[2]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_get_single_users_2_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_single_users_2

    @pytest.mark.parametrize("method, url, response_status", [
                            ('//*[@id="console"]/div[1]/ul/li[3]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span')])
    def test_web_get_single_user_not_found_method(self, method, url, response_status):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text

        response_status = json.loads(response_status)

        assert response_status == 404

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[4]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_get_list_users_unknown_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_list_users_unknown

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[5]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_get_single_unknown_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_single_unknown

    @pytest.mark.parametrize("method, url, response_status", [
                            ('//*[@id="console"]/div[1]/ul/li[6]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span')])
    def test_web_get_single_user_not_found_method(self, method, url, response_status):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text

        response_status = json.loads(response_status)

        assert response_status == 404

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[7]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_post_create_user_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 201
        assert response_body['name'] == "morpheus"
        assert response_body['job'] == "leader"

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[8]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_put_user_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body['name'] == "morpheus"
        assert response_body['job'] == "zion resident"

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[9]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_patch_user_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert 'updatedAt' in response_body

    @pytest.mark.parametrize("method, url, response_status", [
                            ('//*[@id="console"]/div[1]/ul/li[10]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span')])
    def test_web_delete_user_method(self, method, url, response_status):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text

        response_status = json.loads(response_status)

        assert response_status == 204

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[11]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_post_register_successful_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert self.expected_result_register_successful['token'] == response_body['token']

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[12]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_post_register_unsuccessful_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 400
        assert response_body == self.expected_result_register_unsuccessful

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[13]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_post_login_successful_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_login_successful

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[14]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_post_login_unsuccessful_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element('xpath', method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 400
        assert response_body == self.expected_result_login_unsuccessful

    @pytest.mark.parametrize("method, url, response_status, response_body", [
                            ('//*[@id="console"]/div[1]/ul/li[15]',
                             WebTestContext.base_url,
                             '//*[@id="console"]/div[2]/div[2]/p/strong/span',
                             '//*[@id="console"]/div[2]/div[2]/pre')])
    def test_web_get_delay_response_method(self, method, url, response_status, response_body):
        self.driver.get(url=url)

        self.driver.find_element(By.XPATH, method)
        response_status = self.driver.find_element('xpath', response_status).text
        response_body = self.driver.find_element('xpath', response_body).text

        response_status = json.loads(response_status)
        response_body = json.loads(response_body)

        assert response_status == 200
        assert response_body == self.expected_result_delay_response
