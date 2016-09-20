# HW2 - Ian Stuart

## Assignment 1

The most time consuming part of this assignment was parsing through the structure of the JSON response received from the call to the MTA API. The JSON included list or array-like structures nested within the typical dictionary-like structure of a JSON file. Once I familiarized myself with this structure, it was just a matter of identifying the specific keys or items within it that represented the values requested in the output format.

This was also an introduction to the sys python module, which was required to return the values input by the user in the terminal and run the script using those values.

All work on this assignment was my own.

## Assignment 2

Much of the setup for this task was already accomplished in Assignment 1. The primary additions here are incorporating way to handle the situation where no "Onward Call" data is present, and writing the data to a csv file. This step involved adding a header row to the output.

All work on this assignment was my own.

## Assignment 3

This assignment required tracking down a dataset that could be plotted as requested. In my case, the resulting plot isn't useful for much, but creating it did force me to go through the steps of finding the data and doing some basic manipulation.

I received a tip from Shay Lehmann regarding the actual location of the data, which is buried in a subfolder of the path that is given on the Data Hub site.

## Extra Credit

I had some issues formatting the tick labels for the 'Date' axis. I was unable to find cohesive documentation to help me solve this problem. Documentation on plotting in general uses many different approaches, so it can be difficult to identify a preferred method or even a baseline sequence for plot construction.
