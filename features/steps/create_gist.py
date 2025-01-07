
from behave import when, then
from behave.runner import Context


@when('I create a {gist_type} gist containing {file_types} type files')
@when('I create a {gist_type} gist containing {file_types} type files with {description} as description')
def create_a_gist(
    context:Context,
    gist_type: str,
    file_types: str,
    description: str = None,
) -> None:
    files = file_types.split(',')
    gist_files = context.api.prepare_gist_files(files)
    context.is_public = False if 'private' in gist_type else True
    context.gist_body = context.api.prepare_gist_body(
        gist_files,
        context.is_public,
        description if description else None,
    )
    context.response, context.request_correlation_id= context.api.create_new_gist(context.gist_body)

@then('Gist data should be in the response')
def check_response_for_gist_data(context: Context) -> None:
    context.execute_steps(
        f"""
        then Response should contain id
        and Response should contain description
        and Response should contain files
        """
    )

@then('Created gist details should match the original input')
def check_created_gist_details(context: Context) -> None:
    original_input = context.gist_body
    created_gist = context.response.json()
    assert context.is_public == context.gist_body['public'], 'Gist type created as incorrect'
    assert created_gist['description'] == original_input['description'], (f'Gist descriptions does not match\n'
                                                                          f'Original description: {original_input['description']}, Created description: {created_gist['description']}')
    original_files = original_input['files']
    created_files = created_gist['files']
    compare_files(created_files, original_files)


@when('I select a random public gist and go to its detail')
def select_gist_go_to_its_detail(context: Context) -> None:
    public_gists = context.response.json()
    public_gist_ids = []
    for gist in public_gists:
        public_gist_ids.append(gist['id'])
    context.gist_id = str(context.api.select_random_item_form_list(public_gist_ids, 1)[0])
    context.execute_steps('when I get gist by id')


def compare_files(created_files, original_files):
    filtered_created_files = {
        file_name: {'content': file_data['content']}
        for file_name, file_data in created_files.items()
    }

    if filtered_created_files != original_files:
        for file_name in original_files:
            if original_files[file_name] != filtered_created_files.get(file_name):
                print(f'Difference in file: {file_name}')
                print(f'Original: {original_files[file_name]}')
                print(f'Created: {filtered_created_files.get(file_name)}')
        raise AssertionError('Files do not match!')

