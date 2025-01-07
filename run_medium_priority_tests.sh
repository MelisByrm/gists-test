#!/bin/bash

behave --tags="@priority-Medium" --tags="~@skip" \
       --format behave_html_formatter:HTMLFormatter \
       --outfile reports/medium_report.html

