end = 0

import json

def call(test_client, method, uri, data=None):
    operations = {
        "post": test_client.post,
        "get": test_client.get
    }

    op = operations[method]

    headers = { "content-type": "application/json" }

    response = op(f"/api/v1/{uri}", headers=headers, data=json.dumps(data) if data else None)

    return json.loads(response.data), response.status_code
end
