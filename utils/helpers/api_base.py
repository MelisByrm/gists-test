import os
import uuid
import random
from typing import Any

import requests
from requests import Response
from requests.exceptions import Timeout

from data.constants import BASE_URL, APIs
from data.params import default_headers
from data.test_data import FILES_BY_TYPE

class APIBase:
    def set_access_token(self, validation_type: str) -> str:
        self.access_token = None if 'no' in validation_type else os.getenv(
            f'{validation_type.upper()}_GIST_TOKEN'
        )
        return self.access_token

    def prepare_gist_files(self, files: list[str]) -> dict[str, Any]:
        gist_files = {}
        for file in files:
            gist_files.update(FILES_BY_TYPE.get(file))
        return  gist_files

    def create_new_gist(
            self,
            gist_body: dict[str,Any],
    ) -> tuple[Response, str]:
        self.request_correlation_id = str(uuid.uuid4())
        headers = {**default_headers}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        try:
            response = requests.post(
                url= BASE_URL,
                headers=headers,
                json= gist_body,
                timeout=60
            )
            if response.status_code == 500:
                raise requests.exceptions.HTTPError(f'Server error 500 returned while creating a gist\n'
                                                    f'Request id for log/debug : {self.request_correlation_id}')
            return response, self.request_correlation_id
        except Timeout:
            raise TimeoutError(f'It took more than 60s to get create a gist.\n'
                                f'Request id for log/debug : {self.request_correlation_id}')


    def prepare_gist_body(
        self,
        files: dict[str, Any],
        is_public: bool,
        description: str = None,
    ) -> dict[str, Any]:
        gist_request_body = {
            'description': description if description else 'Private Test Gist',
            'public': is_public,
            'files': files,
        }
        return gist_request_body


    def get_gist(self, gist_id: str) -> int:
        self.request_correlation_id = str(uuid.uuid4())
        headers = {**default_headers}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        try:
            response = requests.get(
                url=f'{BASE_URL}/{gist_id}',
                headers=headers,
                timeout=60
            )
            if response.status_code == 500:
                raise requests.exceptions.HTTPError(f'Server error 500 returned while getting gist_id: {gist_id}\n'
                                                    f'Request id for log/debug : {self.request_correlation_id}')
            return response
        except Timeout:
            raise TimeoutError(f'It took more than 60s to get the gist: {gist_id}\n'
                                f'Request id for log/debug : {self.request_correlation_id}')



    def send_req_to_gists_api(self, api: str) -> Response:
        self.request_correlation_id = str(uuid.uuid4())
        headers = {**default_headers}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        try:
            response = requests.get(
                url= f'{BASE_URL}{APIs.get(api)}',
                headers= headers,
            )
            if response.status_code == 500:
                raise requests.exceptions.HTTPError(f'Server error 500 returned from: {api}\n'
                                                    f'Request id for log/debug : {self.request_correlation_id}')
            return response
        except Timeout:
            raise TimeoutError(f'Response took more than 60s from: {api}\n'
                                f'Request id for log/debug : {self.request_correlation_id}')


    def select_random_item_form_list(
            self,
            items: list[Any],
            choice_count: int
    ) -> list[Any]:
        selected_items = random.sample(items, choice_count)
        return selected_items


    def check_list_for_an_item(
            self,
            item_to_check: Any,
            list_to_check: list[Any],
    ) -> bool:
        result = True if item_to_check in list_to_check else False
        return result

    def show_failure_detail(self, case_exception_detail: str) -> None:
        raise Exception(f'Request id : {self.request_correlation_id}\n'
                        f'Failure detail : {case_exception_detail}'
                        )