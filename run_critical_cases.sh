#!/bin/bash

behave --tags="@priority-High" --tags="~@skip" --format html --outfile critical_report.html


