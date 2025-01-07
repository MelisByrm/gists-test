# gists-test

A boilerplate for automated testing of **GitHub Gists** critical functionality using **Behave** and **Python**. This project focuses on testing key scenarios for creating and retrieving Gists, ensuring reliability and robustness in critical areas of functionality.

---

## Setup Requirements

### Tools and Languages Used
- **Python**  
- **Behave**  
- **Docker**  

### Python Version
- Python 3.11 and above  

### Installation
Use `pip` to set up the required dependencies:  
```bash
pip install -r requirements.txt
```

## Environment Variables

Three secrets are required for running the tests:

- **`VALID_GIST_TOKEN`**: A valid token with Gist read/write permissions.  
- **`INVALID_GIST_TOKEN`**:  A completely invalid or dummy token.
- **`WITHOUT_PERMISSION_GIST_TOKEN`**: A valid token without Gist permissions.  

These can be set up in a `.env` file or added to your CI/CD pipeline secrets.


## Running Tests

### Locally

#### Run Specific Tags
To run tests based on tags, use:  
```bash
behave --tags="@priority:High" --tags="~@skip" <path_of_feature_file>
```

Replace `@priority:High` with your desired tag and `@skip` with the tag to exclude.

#### Run All Tests
If you want to run all tests, simply execute:

```bash
behave features
```

## In CI/CD
The tests are configured to run automatically based on the following triggers:

##### Scheduled Runs

**`@priority:High`** tagged tests every 3 hours (Monday to Friday).
Medium-priority tests every **6 hours** (Monday to Friday).
Push and Pull Request Events
Tests are executed for changes to the main branch or for opened PRs targeting main.
Refer to the CI workflow for details:


```yaml
on:
  schedule:
    - cron: "0 */3 * * 1-5"  # High-priority tests
    - cron: "0 */6 * * 1-5"  # Medium-priority tests

  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```



## Features

**`Automated Testing`**: Fully automated scenarios for creating and retrieving Gists.

**`CI/CD Integration`**: Tests run automatically on schedule, push, and pull request events.

**`Tag-Based Execution`**: Flexibility to run specific tagged scenarios locally or in CI/CD.


## Known Limitations/Future Enhancements

#### Expanded Test Cases: 
Additional functionality like updating and deleting Gists can be automated in the future.

#### Advanced Reporting: 
Tools like Allure or Pytest HTML can be integrated for detailed test reporting.