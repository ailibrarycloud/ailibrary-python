Please note that this testing folder is currently a work in progress and unfinished.
Here is the planned structure for the testing folder:


1. Test _HTTPClient by sending real HTTP requests to the Ailibrary APIs
2. Then use a Mock object that mimics _HTTPClient to run unit tests for each resource (_Agent, _Utilities, etc) and the client object
3. Then we run the integration tests with that same Mock object
4. Finally we run our end-to-end (e2e) tests
