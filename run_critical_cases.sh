#!/bin/bash

behave --tags="@priority-High" --tags="~@skip" --format allure_behave.formatter:AllureFormatter --outfile=allure-results


