# Courses App

**(Optional) In case the blog post is already published, please add: [Read the blog post here](https://configcat.com/blog/)**

This is a companion repository to the article "Announcing Official OpenFeature for Support". It contains a simple Python FastAPI app that returns a list of courses from its `/courses` route. The app was built to demonstrate how to integrate OpenFeature into an existing app that uses [ConfigCat](https://configcat.com).

## Build & Run

This repository has two Python files:
- `main.py`: uses only ConfigCat for feature flag evaluation
- `cc-openfeature.py`: uses OpenFeature + ConfigCat for feature flag evaluation.

Follow the steps in the upcoming sections to run any of the two files.

### Prerequisites

- A ConfigCat account
- Python v3.9+
- Git v2.33+
- A tool to make HTTP requests (curl, Postman, Thunder client, etc)
- Intermediate knowledge of Python and FastAPI and basic knowledge of Git

1. Clone the repository using any of the options available on the repository's page.

2. Navigate to the directory.
`cd openfeature-python-sample` 

3. Create a virtual environment with `venv`:
```
python -m venv .venv
```

4. Activate the virtual environment:
```
# PowerShell
.venv\Scripts\Activate.ps1

# Linux, macOS
source .venv/bin/activate
```

5. Install the dependencies:
`pip install -r requirements.txt`

6. Create a `.env` file and add a variable to store your ConfigCat SDK key:
```
CONFIGCAT_SDK_KEY="YOUR-SDK-KEY
```

7. Run the app.
```
# For ConfigCat only

fastapi dev main.py

OR

# For ConfigCat + OpenFeature

fastapi dev cc-openfeature.py
```

## Learn more

- [ConfigCat OpenFeature Provider for Python](https://configcat.com/docs/sdk-reference/openfeature/python/) - Read the providers documentation. 
- [OpenFeature Python SDK](https://openfeature.dev/docs/reference/technologies/server/python) - Learn more about OpenFeature's Python SDK.
- [ConfigCat OpenFeature Providers](https://configcat.com/docs/sdk-reference/openfeature/overview/) - Check out the available OpenFeature providers.
- [OpenFeature](https://openfeature.dev/) - Learn more about OpenFeature.


[**ConfigCat**](https://configcat.com) supports many other frameworks and languages. Check out the full list of supported SDKs [here](https://configcat.com/docs/sdk-reference/overview/).

You can also explore other code samples for various languages, frameworks, and topics in [ConfigCat labs](https://github.com/configcat-labs) on GitHub.

Keep up with ConfigCat on [X](https://x.com/configcat), [Facebook](https://www.facebook.com/configcat), [LinkedIn](https://www.linkedin.com/company/configcat/), and [GitHub](https://github.com/configcat).

## Author

[Zayyad](https://github.com/Z-MS)

## Contributions

Contributions are welcome!