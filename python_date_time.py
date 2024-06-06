"""
A date in python ia not a data type of its own, but we can,
import a  module named datetime to work with dates as date object
"""

import datetime

currentDateTime = datetime.datetime.now()
print(currentDateTime)
print(currentDateTime.strftime("%A"))
print(currentDateTime.strftime("%D"))
print(currentDateTime.strftime("%m"))
