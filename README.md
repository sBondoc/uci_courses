# UCI Courses

This repository contains part of my HackUCI 2019 project, PetrPlanner (private repository), a utility for planning out graduation course paths for UCI students. Included is the code that parses through the HTML of the pages containing information about courses on the [UCI course catalogue](https://catalogue.uci.edu/) in order to generate a list of `Course` and `Department` objects used in other parts of the project.

The purpose of including only these parts of the project is to focus on demonstrating organizational, string processing, and HTML parsing skills.

The file `uci_courses.py` is meant to be imported and used to access a list of `Course` and `Department` objects (defined in `classes.py`) that refer to the courses and departments available at UCI, respectively. The file `courses_generate.py` creates these lists by parsing through strings in the HTML files of pages from the domain [catalogue.uci.edu](https://catalogue.uci.edu/) using the default `urllib` and `html` packages and converting them to objects more easily readable and usable by PetrPlanner.
