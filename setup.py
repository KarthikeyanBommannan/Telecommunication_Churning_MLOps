import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "TELCO_CHURN_MLOPS"
AUTHOR_USER_NAME = "karthikeyanbommannan"   
SRC_REPO = "Telco Churn MLOps"
AUTHOR_EMAIL = "karthibommannan@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "python package for the telco churn project with mlfow implementation related library",
    long_description = "text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url ={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
    
)






