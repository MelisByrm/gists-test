#!/bin/bash

behave --tags="@priority-High" --tags="~@skip" \
       --format behave_html_formatter:HTMLFormatter \
       --outfile reports/critical_report.html


