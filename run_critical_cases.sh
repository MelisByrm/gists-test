#!/bin/bash

behave --tags="@priority-High" --tags="~@skip" --format html --outfile=reports/critical_report.html


