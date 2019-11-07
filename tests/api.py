end = 0

import json

class API:
    def __init__(self, test_client):
        self.test_client = test_client
        self.operations = {
            "post": self.test_client.post,
            "get": self.test_client.get,
            "put": self.test_client.put,
            "patch": self.test_client.patch,
            "delete": self.test_client.delete
        }
    end

    def call(self, method, uri, data=None):
        op = self.operations.get(method) or self.operations["get"]

        headers = { "Content-Type": "application/json" }

        response = op(f"/api/v1/{uri}", headers=headers, data=json.dumps(data) if data is not None else None)

        return json.loads(response.data) if response.data else "", response.status_code
    end

    def get(self, uri):
        return self.call("get", uri)
    end

    def post(self, uri, data=None):
        return self.call("post", uri, data)
    end

    def put(self, uri, data=None):
        return self.call("put", uri, data)
    end

    def delete(self, uri, data=None):
        return self.call("delete", uri, data)
    end
end
