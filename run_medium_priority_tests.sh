#!/bin/bash

behave --tags="@priority-Medium" --tags="~@skip" --format allure_behave.formatter:AllureFormatter --outfile=allure-results

