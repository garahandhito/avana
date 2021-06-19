# avana
Avana Sr. QA Engineer Test submission by Gara Handhito

In order to run the test, these are the required set up in your local machine:

1. Make sure latest python is installed in your machine. Download python here https://www.python.org/downloads/ if python is not yet installed in your machine.
2. Don't forget to add the directory of installed python into your PATH environment variable in order to run properly.
3. Download/clone this repository and place it in any directory that you want.
4. Open your terminal/command prompt and create virtual environment inside the local repository that you have just created, using this command `python3 -m venv /path/to/new/virtual/environment`.
5. Inside your terminal, change directory to that local repository of yours, then activate virtual environment using this command `venv\Scripts\activate`.
3. Install python selenium into your virtual environment using `pip install -U selenium`.
4. Install pytest into your virtual environment using `pip install -U pytest`.
5. Install pytest-html into your virtual environment using `pip install pytest-html`.
6. Download chromedriver from here https://chromedriver.chromium.org/ and extract the downloaded package.
7. Create a directory named `drivers` inside `tests` directory. The executable path of the chromedriver.exe should be `./tests/drivers/chromedriver.exe`.

After all requirements are met, to run the test:
1. Open your terminal/command prompt and change directory to your local repository and activate the virtual environment.
2. Run the test with this command `python -m pytest tests/login_and_post_test.py`.
3. After the test is finish running, you can check the generated html report under `reports` directory.
