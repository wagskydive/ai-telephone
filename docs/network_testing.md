# Network Failure Testing

The automated test suite includes a scenario that mimics a dropped connection to
 the API server. Run this test with:

```bash
pytest -k network_failure -q
```

The test patches `requests.post` to raise a `ConnectionError` and verifies that
`handle_call` exits gracefully without raising an exception. Use this pattern to
audit other components under unreliable network conditions.

