# Week 08 – completed Python inputs and test report

## What I completed

- Filled every `# your code here` exercise/challenge cell in the four walkthrough notebooks:
  - `01 - Calling a Web API/W08T01_walkthrough.ipynb`
  - `02 - Reading Files from the Web/W08T02_walkthrough.ipynb`
  - `03 - Light Regex/W08T03_walkthrough.ipynb`
  - `04 - From Functions to a Class/W08T04_walkthrough.ipynb`
- Added safe handling for the optional Kaggle download cell. It now explains what to install/configure instead of stopping the whole notebook when Kaggle is not set up.
- Corrected the machine-specific macOS CSV path in Topic 2 to use the `target` Path variable created earlier. This works on Windows too.
- Corrected the `github_rest_api` variable spelling in Topic 1.
- Made the live GitHub regex example continue safely when an internet request fails.
- Added `LAB/fetch_data.py`, a ready-to-copy Week 8 lab script using the COVID-19 API and the same columns already specified in the lab notebook. Copy it into the root of your own `CST1510_CW2` project folder as `fetch_data.py`.

## Test results

- All four completed walkthrough notebooks: **PASS**. Every code cell executed without a Python exception. API and CSV responses were simulated for testing because this execution environment could not resolve external internet hosts.
- All 11 Python scripts in the project: **PASS** for syntax checks.
- All 11 Python scripts: **PASS** when executed with simulated API responses where network access was required.
- The new `LAB/fetch_data.py`: **PASS**. Tested with 55 simulated country records; it produced 55 rows and 8 columns with no missing values.
- Offline examples (regex, class/object example, nested JSON and tidying): **PASS** when run directly.

## Important before you run it on your PC

1. Install the required packages in the VS Code terminal:
   `python -m pip install requests pandas`
2. For the lab, copy `LAB/fetch_data.py` into your own `CST1510_CW2` folder.
3. In the lab notebook, set `MY_FOLDER` to the full path of your own `CST1510_CW2` folder if it is not detected automatically.
4. Run `python fetch_data.py` from the `CST1510_CW2` terminal. This final live API run needs an internet connection.
5. Kaggle is optional. Its section needs a Kaggle account, API token and `kagglehub` package; all other exercises can run without it.

**Note:** A successful simulated test confirms the Python logic and expected data handling. It does not guarantee that a public API will be online or return the same data when you run it later.
