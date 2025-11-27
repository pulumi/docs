---
title: external
title_tag: external Pulumi ESC Rotator
meta_desc: The `external` rotator enables you to rotate credentials using a custom adapter service. 
h1: external
menu:
  esc:
    identifier: external-rotator
    parent: esc-rotated-secrets
---

The `external` rotator enables you to rotate secrets with custom logic using Pulumi ESC by making authenticated HTTPS requests to user-controlled adapter services.

## Overview

The external rotator allows you to implement custom secret rotation logic without waiting for a native rotator implementation. Your adapter service:

- Authenticates requests using JWT tokens issued by Pulumi Cloud (see [JWT Authentication](/docs/esc/integrations/dynamic-secrets/external/#jwt-authentication))
- Receives the current state from previous rotations
- Generates new credentials or rotates existing ones
- Returns the new state to be stored in ESC

## When to Use

Use the external rotator when:

- You need to rotate credentials for a custom or proprietary system.

## ESC Configuration Example

```yaml
values:
  rotatedCredentials:
    fn::rotate::external:
      inputs:
        url: https://my-adapter.example.com/rotate-credentials
        request:
          service: database
          environment: production
```

### Request Payload (First Rotation)

On the first rotation, your adapter receives `null` for the state:

```json
{
  "request": {
    "service": "database",
    "environment": "production"
  },
  "state": null
}
```

### Request Payload (Subsequent Rotations)

On subsequent rotations, your adapter receives the current state from the previous rotation:

```json
{
  "request": {
    "service": "database",
    "environment": "production"
  },
  "state": {
    "username": "user_20250115",
    "password": "previous-password-123",
    "rotatedAt": "2025-01-15T10:00:00Z"
  }
}
```

### Response Payload

Your adapter returns a JSON object that becomes the new state:

```json
{
  "username": "user_20250116",
  "password": "newly-rotated-password-456",
  "rotatedAt": "2025-01-16T10:00:00Z"
}
```

In ESC, this is stored as the current state and automatically marked as secret.
On the next rotation, this entire object is passed as the `state` field in the request.

When opening the environment after rotation, you should see output like this:

```json
{
  "rotatedCredentials": {
    "current": {
      "username": "user_20250116",
      "password": "newly-rotated-password-456",
      "rotatedAt": "2025-01-16T10:00:00Z"
    }
  }
}
```

## Building Custom Rotators

### Requirements

Your rotator adapter must meet the [same requirements as an external provider adapter](/docs/esc/integrations/dynamic-secrets/external#requirements).

### State Management

The key difference from the provider is state management:

- **First rotation**: `state` is `null` - your adapter should create initial credentials
- **Subsequent rotations**: `state` contains the `current` value from the previous rotation
- **Response**: Your entire response becomes the new `current` state, marked as secret

#### Recommended: Dual-secret strategy

**We strongly recommend implementing a dual-secret rotation strategy** to ensure zero-downtime credential rotations. This pattern maintains two active secrets: one currently in use by applications, and one that can be safely rotated.

**Why dual-secret rotation?**

Without dual secrets, rotation creates a race condition:

1. Your adapter rotates the credential (e.g., regenerates an API key)
2. Applications using the old credential start failing immediately
3. Applications must fetch new configuration before they can reconnect

With dual secrets, you eliminate this window of failure:

1. Applications always use the `current` secret
2. During rotation, the adapter rotates the inactive secret
3. Applications continue using the current secret (unaffected by rotation)
4. On the next config fetch, applications seamlessly switch to the newly rotated secret

**How to implement:**

The exact implementation depends on your credential system:

- **API keys with multiple active keys**: Create two keys, rotate the inactive one
- **Database passwords without multi-password support**: Create two user accounts (see [mysql rotator](/docs/esc/integrations/rotated-secrets/mysql/) for an example)
- **Service tokens with versioning**: Maintain two versions, rotate the older one

**Implementation pattern:**

Store identifiers for both secrets in your `request` configuration, and track which one is current in state:

```yaml
values:
  apiCredentials:
    fn::rotate::external:
      inputs:
        url: https://my-adapter.example.com/rotate
        request:
          service: my-service
          keys:
            key1: "prod-key-1"
            key2: "prod-key-2"
```

```python
def rotate(request, state):
    keys = request["keys"]  # {"key1": "prod-key-1", "key2": "prod-key-2"}

    if state is None:
        # First rotation: create both secrets, return key1 as current
        create_secret(keys["key1"])
        create_secret(keys["key2"])

        return {
            "keyId": keys["key1"],
            "secret": get_secret_value(keys["key1"]),
            "rotatedAt": now()
        }

    # Determine which secret to rotate (the inactive one)
    current_key = state["keyId"]
    next_key = keys["key2"] if current_key == keys["key1"] else keys["key1"]

    # Rotate the inactive secret
    new_secret = rotate_secret(next_key)

    # Return the newly rotated secret as current
    return {
        "keyId": next_key,
        "secret": new_secret,
        "rotatedAt": now()
    }
```

**ESC output:**

After rotation, applications see only the current secret:

```json
{
  "apiCredentials": {
    "current": {
      "keyId": "prod-key-2",
      "secret": "newly-rotated-secret-value",
      "rotatedAt": "2025-01-16T10:00:00Z"
    }
  }
}
```

Your application should always use `apiCredentials.current`. After rotation, `current` contains the newly rotated secret, while the previous secret remains valid until the next rotation.

**Important:** Configure your rotation schedule to be less frequent than your application's configuration refresh interval. For example, if your app fetches configuration every 5 minutes, rotate no more than once per hour.

### Example Rotator Implementation

Here's a complete rotator in Python that generates rotating API keys:

```python
#!/usr/bin/env python3
"""
Example external rotator adapter for Pulumi ESC.
Rotates API keys with timestamp-based rotation tracking.
"""

import hashlib
import base64
import json
import secrets
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler

import jwt
from jwt import PyJWKClient

# Configuration
JWKS_URL = "https://api.pulumi.com/.well-known/jwks.json"
ADAPTER_URL = "https://my-adapter.example.com/rotate-credentials"
PORT = 8443

# Initialize JWKS client (caches keys automatically)
jwks_client = PyJWKClient(JWKS_URL)


def verify_body_hash(body: bytes, claims: dict) -> None:
    """Verify the body_hash claim matches the request body."""
    expected_hash = claims.get("body_hash")
    if not expected_hash:
        raise ValueError("Missing body_hash claim")

    hash_digest = hashlib.sha256(body).digest()
    actual_hash = f"sha256-{base64.b64encode(hash_digest).decode('ascii')}"

    if actual_hash != expected_hash:
        raise ValueError(f"Body hash mismatch")


def generate_api_key(service: str) -> str:
    """Generate a new API key for the service."""
    # In production, this would call your actual rotation logic
    # (e.g., call an API, update a database, etc.)
    random_bytes = secrets.token_bytes(32)
    return f"{service}_{base64.urlsafe_b64encode(random_bytes).decode('ascii').rstrip('=')}"


class RotatorHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Extract and verify JWT token
            auth_header = self.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                self.send_error(401, "Missing or invalid Authorization header")
                return

            token = auth_header[7:]

            # Verify token using JWKS
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            claims = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=ADAPTER_URL,
                options={"verify_exp": True}
            )

            # Read and verify request body
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            verify_body_hash(body, claims)

            # Parse rotation request
            rotation_request = json.loads(body)
            request_config = rotation_request.get("request", {})
            current_state = rotation_request.get("state")  # None on first rotation

            service = request_config.get("service")
            if not service:
                self.send_error(400, "Missing required field: service")
                return

            # Log rotation event
            if current_state is None:
                print(f"First rotation for service: {service}")
            else:
                print(f"Rotating credentials for service: {service}")
                print(f"Previous key: {current_state.get('apiKey', 'N/A')[:20]}...")

            # Generate new credentials
            new_api_key = generate_api_key(service)
            new_state = {
                "apiKey": new_api_key,
                "rotatedAt": datetime.now(timezone.utc).isoformat(),
                "service": service,
            }

            # In production, you might:
            # 1. Update your service with the new credentials
            # 2. Keep old credentials valid for a grace period
            # 3. Verify the new credentials work before returning

            # Return new state
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(new_state).encode())

        except jwt.InvalidTokenError as e:
            self.send_error(401, f"Invalid token: {str(e)}")
        except Exception as e:
            self.send_error(400, str(e))


if __name__ == "__main__":
    # In production, use a proper HTTPS server with valid certificates
    server = HTTPServer(("", PORT), RotatorHandler)
    print(f"Rotator adapter listening on port {PORT}")
    server.serve_forever()
```

To use this rotator:

```bash
# Install dependencies
pip install pyjwt cryptography

# Run the rotator (in production, use proper HTTPS)
python rotator.py
```

ESC configuration:

```yaml
values:
  apiCredentials:
    fn::rotate::external:
      inputs:
        url: https://my-adapter.example.com/rotate-credentials
        request:
          service: my-api
```

After running `esc env rotate`, the environment will contain:

```yaml
apiCredentials:
  current:
    apiKey: "my-api_gK7jP9mN4qR8tX2vY5zW..."
    rotatedAt: "2025-01-16T10:00:00Z"
    service: "my-api"
```

## Schema Reference

### Inputs

| Property  | Type   | Description                                                | Required | Default |
|-----------|--------|------------------------------------------------------------|----------|---------|
| `url`     | string | HTTPS URL to your rotator adapter service                  | Yes      | -       |
| `request` | object | [Rotate only] - Arbitrary JSON object sent to your adapter | No       | `{}`    |

### State (Optional)

You can optionally provide initial state in your ESC environment:

```yaml
values:
  rotatedCredentials:
    fn::rotate::external:
      inputs:
        url: https://my-adapter.example.com/rotate
        request:
          service: api
      state:
        current:
          apiKey: existing-key-123
          rotatedAt: "2025-01-01T00:00:00Z"
```

If no state is provided, the rotator passes `"state": null` on the first rotation.

### Outputs

| Property  | Type   | Description                                           |
|-----------|--------|-------------------------------------------------------|
| `current` | object | The JSON response from your adapter, marked as secret |
