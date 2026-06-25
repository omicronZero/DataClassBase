# Content

The template sets up a simple continuous integration-pipeline for Python 3.14.

For every push and pull request, linting, format checking, static type checking, and tests are invoked:
* Ruff: Linting, Formatting
* MyPy: Code checking
* Tests: PyTest (with coverage)

The test summary and coverage are reported as an artifact.

For every push and pull request to the main/master and dev branches, a documentation is built using sphinx and deployed
to a respective separate branch "gh-docs-<dev/main/master>".

# Setting up the project

* Either set up an environment with Python 3.14 or change the respective version strings (Look for regex: "3\.?14")
  where adequate
* On your repository under Settings/Branches, check that merging only passes if all checks from linting, tests, etc.
  pass

# License (MIT-0)

Copyright 2026 Josef Mayr

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
