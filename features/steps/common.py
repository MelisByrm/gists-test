import random

from behave import given, when, then
from behave.runner import Context

from data.test_data import TEST_GIST_IDs


@given('I have {validation_type} Github API Gist token')
def given_valid_token(context:Context, validation_type: str) -> None:
    context.access_token = context.api.set_access_token(validation_type)


@then('Response status should be {status}')
def check_response_status(context: Context, status: str) -> None:
    if not context.response.status_code == int(status):
        raise ValueError(
            f'Response status returned : {context.response.status_code},\n'
            f'Expected :{status}, Request id to debug: {context.request_correlation_id}'
        )


@then('Response should contain {data}')
def check_response_for_specific_data(context: Context, data: str) -> None:
    assert data in context.response.json(), (f'{data} is not in the response,\n'
                                             f'Request id to debug: {context.request_correlation_id}')


@then('Error message should contain {message_content}')
def check_error_message(context: Context, message_content: str) -> None:
    message_from_response = context.response.json()['message']
    if message_content not in message_from_response:
        case_exception_detail = f'Error message returned as: {message_from_response}\nExpected error message : {message_content}'
        context.api.show_failure_detail(case_exception_detail)



@when('I retrieve the gist')
@when('I get gist by id')
@when('I get gist with id')
@when('I try to retrieve non-existing gist id')
def get_created_gist(context: Context) -> None:
    gist_id = (
        context.gist_id if 'by id' in context.current_step
        else random.choice(TEST_GIST_IDs) if 'with id' in context.current_step
        else 'not-existing-id2346' if 'non-existing' in context.current_step
        else context.response.json()['id']
    )
    context.response = context.api.get_gist(gist_id)
    if 'negative' not in context.scenario.tags:
        context.execute_steps('then Response status should be 200')


@when('I get the list of public gists')
def get_public_gists(context: Context) -> None:
    context.response = context.api.send_req_to_gists_api('public-gists')

