# OnspringAPILibraryPython

This library builds on the Python Requests library to further abstract requests and make working with the Onspring API more accessible via Python. It provides a simplified path for Onspring customers to integrate with an organization's OnSpring instance.

## Installation

To install and use the library, clone this repo and reference two main files, the onspring_api_library_v2.py file and client_code_examples.py.

_Important_

- The onspring_api_library.py contains a class for all of the requests. The requests are built using a seris of constructors and then utillized via a series of prebuilt methods. This allows the developer to make requests using much less syntax.
- What must be obtained prior to the utilization of this library is an API key from an Onspring instance.

## Obtaining an API Key

Interacting with the Onspring API requires a generated key. Keys can be generated by an Onspring user who has been granted the appropriate permissions. This typically an admin user. To generate a key:

1. In Onspring, navigate to Administration> Security> API Keys.
2. On the list page, select to create a new key or click on an existing one.
3. On the details page, expand the **Developer Information** section. Copy the **X-ApiKey Header**.

_Important_

- The API Key must also have a status of enabled within the Onspring interface. This option can be found within the details page for the particular API Key.
- Each API Key within Onspring is associated with a role for security measures. The permissions given to the associated role will determine what request types can be made. If a particular request is made and the API Key does not have sufficient permissions assigned, an error will be returned.

## Initial Setup and Coding Examples

This library requires two python dependencies before getting started, **requests** and **json**. Both can be obtained via a common pyhton package manager such as pip.

Once the appriate packages have been installed, everything needed to begin can be found in the client_code_examples.py file. Although a basic understanding of Onspring and its data input requirements is not entirely required, it is greatly recommended. Also, access to an Onspring instance is beneficial for data validation.

To get started:

1. Create a .py file.
2. Import **requests** and the _OnSpring_ class from the onpsring_api_library_v2.py file.
3. You will the then need to build an Onspring object to make API calls. Its constructor will requires two inputs:

   - The Onspring API base URL which is https://api.onspring.com/
   - The generated API key from the Onspring instance.

It will look something like this:

```python
import requests

from onspring_api_library_v2 import Onspring

api = Onspring('https://api.onspring.com/','This is where you would insert your api key')
```

Once the Onspring object is built, you can then append calls to it and make standard rest API calls to gather data from an Onspring instance. For a full list of API calls and assistance determining which values to pass as parameters, please counsult the [Onspring v2 API Administrator Guide](https://software.onspring.com/hubfs/Training/Admin%20Guide%20-%20v2%20API.pdf). All examples in pythonic syntax are listed in the client_code_examples.py file and can be copied and pasted into the project you are working on.

Now, let's take a look at a couple of examples. To provide a conceptual framwork for interacting with the Onapring API, the basic structure within Onspring consists of a series of interelated databases (in Onspring, these are called apps) and within those databases, each row represents a record (each column is a field and each row is a record).
