#!/bin/bash

behave --tags="@priority-Medium" --tags="~@skip" --format html --outfile=reports/medium_report.html

