#!/bin/bash

behave --tags="@priority-Medium" --format allure_behave.formatter:AllureFormatter --outfile=allure-results

