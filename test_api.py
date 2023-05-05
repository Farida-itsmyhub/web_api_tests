import pytest
import requests
from context.ApiTestContext import ApiTestContext


class TestApi(ApiTestContext):
    @pytest.mark.parametrize("method, params", [(ApiTestContext.users_url, {'page': '2'})])
    def test_api_get_list_users_method(self, method, params):
        response = requests.get("{}{}".format(self.base_url, method), params=params)
        assert response.status_code == 200

        response = response.json()

        assert response == self.expected_result_get_list_users

    @pytest.mark.parametrize("method", [f'{ApiTestContext.users_url}/2'])
    def test_api_get_single_users_2_method(self, method):
        response = requests.get("{}{}".format(self.base_url, method))
        assert response.status_code == 200

        response = response.json()
        assert response == self.expected_result_single_users_2

    @pytest.mark.parametrize("method", [f'{ApiTestContext.users_url}/23'])
    def test_api_get_single_user_not_found_method(self, method):
        response = requests.get("{}{}".format(self.base_url, method))
        assert response.status_code == 404

        response = response.json()
        assert response == {}

    @pytest.mark.parametrize("method", [ApiTestContext.unknown_url])
    def test_api_get_list_users_unknown_method(self, method):
        response = requests.get("{}{}".format(self.base_url, method))
        assert response.status_code == 200

        response = response.json()
        assert response == self.expected_result_list_users_unknown

    @pytest.mark.parametrize("method", [f'{ApiTestContext.unknown_url}/2'])
    def test_api_get_single_unknown_method(self, method):
        response = requests.get("{}{}".format(self.base_url, method))
        assert response.status_code == 200

        response = response.json()
        assert response == self.expected_result_single_unknown

    @pytest.mark.parametrize("method", [f'{ApiTestContext.unknown_url}/23'])
    def test_api_get_single_unknown_not_found_method(self, method):
        response = requests.get("{}{}".format(self.base_url, method))
        assert response.status_code == 404

        response = response.json()
        assert response == {}

    @pytest.mark.parametrize("method, data", [(ApiTestContext.users_url, {'name': "morpheus", "job": "leader"})])
    def test_api_post_create_user_method(self, method, data):
        response = requests.post("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 201

        response = response.json()
        assert response['name'] == "morpheus"
        assert response['job'] == "leader"

    @pytest.mark.parametrize("method, data", [(f'{ApiTestContext.users_url}/2', {'name': "morpheus", "job": "zion resident"})])
    def test_api_put_user_method(self, method, data):
        response = requests.put("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 200

        response = response.json()
        assert response['name'] == "morpheus"
        assert response['job'] == "zion resident"

    @pytest.mark.parametrize("method, params", [(f'{ApiTestContext.users_url}/2', {'name': "morpheus", "job": "zion resident"})])
    def test_api_patch_user_method(self, method, params):
        response = requests.patch("{}{}".format(self.base_url, method), params=params)
        assert response.status_code == 200

        response = response.json()
        assert 'updatedAt' in response

    @pytest.mark.parametrize("method", [f'{ApiTestContext.users_url}/2'])
    def test_api_delete_user_method(self, method):
        response = requests.delete("{}{}".format(self.base_url, method))
        assert response.status_code == 204

    @pytest.mark.parametrize("method, data", [(ApiTestContext.register_url, {"email": "eve.holt@reqres.in", "password": "pistol"})])
    def test_api_post_register_successful_method(self, method, data):
        response = requests.post("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 200

        response = response.json()
        assert response['token'] == self.expected_result_register_successful['token']

    @pytest.mark.parametrize("method, data", [(ApiTestContext.register_url, {"email": "sydney@fife"})])
    def test_api_post_register_unsuccessful_method(self, method, data):
        response = requests.post("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 400

        response = response.json()
        assert response == self.expected_result_register_unsuccessful

    @pytest.mark.parametrize("method, data", [(ApiTestContext.login_url, {"email": "eve.holt@reqres.in", "password": "cityslicka"})])
    def test_api_post_login_successful_method(self, method, data):
        response = requests.post("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 200

        response = response.json()
        assert response == self.expected_result_login_successful

    @pytest.mark.parametrize("method, data", [(ApiTestContext.login_url, {"email": "peter@klaven"})])
    def test_api_post_login_unsuccessful_method(self, method, data):
        response = requests.post("{}{}".format(self.base_url, method), data=data)
        assert response.status_code == 400

        response = response.json()
        assert response == self.expected_result_login_unsuccessful

    @pytest.mark.parametrize("method, params", [(ApiTestContext.users_url, {'delay': '3'})])
    def test_api_get_delay_response_method(self, method, params):
        response = requests.get("{}{}".format(self.base_url, method), params=params)
        assert response.status_code == 200

        response = response.json()
        assert response == self.expected_result_delay_response
