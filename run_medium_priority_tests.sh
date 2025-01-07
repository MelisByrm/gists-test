#!/bin/bash

behave --tags="@priority-Medium" --tags="~@skip" --format html --outfile medium_report.html

