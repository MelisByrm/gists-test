from behave import then
from behave.runner import Context

@then('No private gist should appear on public gists list')
def ensure_private_gists_not_exists_in_public_list(context: Context) -> None:
    public_gists = context.response.json()
    listed_gist_types = []
    for gist in public_gists:
        listed_gist_types.append(gist['public'])
    result = context.api.check_list_for_an_item(
        item_to_check= False,
        list_to_check = listed_gist_types
    )
    if result:
        case_exception_detail = 'Private gist found in public gists.'
        context.api.show_failure_detail(case_exception_detail)

@then('Gists should be listed')
def check_if_public_gists_listed(context: Context) -> None:
    if not len(context.response.json()) > 0:
        case_exception_detail = 'Gists not returned.'
        context.api.show_failure_detail(case_exception_detail)

@when('I get the list of {type} gists')
def get_public_gists(context: Context, type: str) -> None:
    context.response = context.api.send_req_to_gists_api(f'{type}-gists')