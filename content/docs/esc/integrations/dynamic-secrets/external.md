---
title: external
title_tag: external Pulumi ESC provider
meta_desc: The `external` Pulumi ESC provider enables you to dynamically import values from custom secret sources.
h1: external
menu:
  esc:
    identifier: external
    parent: esc-dynamic-secrets
---

The `external` provider enables you to integrate custom secret sources with Pulumi ESC by making authenticated HTTP requests to user-controlled adapter services.

## Overview

The external provider serves as a generic escape hatch for integrating secret sources that don't have native Pulumi ESC support. Instead of waiting for a native provider implementation, you can build a custom HTTPS adapter service that:

- Authenticates requests using JWT tokens issued by Pulumi Cloud
- Receives configuration from your ESC environment
- Returns secrets back to ESC

## When to Use

Use the external provider when:

- You need to integrate a custom or proprietary secret management system
- You have specific business logic for secret fetching
- Your secret source is behind a firewall or requires custom networking

## ESC Configuration Example

```yaml
values:
  customSecrets:
    fn::open::external:
      url: https://my-adapter.example.com/fetch-secrets
      request:
        environment: production
        secretType: api-keys
      secret: true  # Optional, defaults to true
```

### Request Payload

Your adapter receives a POST request with the `request` field from your ESC configuration:

```json
{
  "environment": "production",
  "secretType": "api-keys"
}
```

### Response Payload

Your adapter returns a JSON object that becomes available under the `response` key:

```json
{
  "apiKey": "secret-api-key-value",
  "apiSecret": "secret-api-secret-value",
  "endpoint": "https://api.example.com"
}
```

In ESC, you should see output like the following:

```json
{
 "customSecrets": {
   "response": {
     "apiKey": "secret-api-key-value",
     "apiSecret": "secret-api-secret-value",
     "endpoint": "https://api.example.com"
   }
 }
}
```

You can mark the entire response as secret with `secret: true` (the default).

## Building Custom Adapters

### Requirements

Your adapter service must:

1. **Run on HTTPS** - Pulumi ESC only makes requests to `https://` URLs
2. **Accept POST requests** with `Content-Type: application/json`
3. **Validate JWT tokens** from the `Authorization: Bearer <token>` header
4. **Return JSON responses** with `Content-Type: application/json`
5. **Return HTTP 200** for successful requests (other status codes are treated as errors)

### JWT Authentication

Every request includes a JWT token in the `Authorization` header. The token is signed using RS256 and can be verified using Pulumi Cloud's public JWKS.

The JWT token includes the following claims, which you can use to make authorization decisions:

| Claim          | Description                                       | Example                                               |
|----------------|---------------------------------------------------|-------------------------------------------------------|
| `iss`          | Issuer (Pulumi Cloud URL)                         | `https://api.pulumi.com`                              |
| `sub`          | Subject (environment identity)                    | `pulumi:environments:org:acme-corp:env:prod`          |
| `aud`          | Audience (your adapter URL)                       | `https://my-adapter.example.com/fetch-secrets`        |
| `exp`          | Expiration time (Unix timestamp)                  | `1736937600`                                          |
| `iat`          | Issued at (Unix timestamp)                        | `1736933600`                                          |
| `jti`          | Unique id (to prevent replay)                     | `a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11`                |
| `org`          | Pulumi organization name                          | `acme-corp`                                           |
| `env`          | Environment name (legacy format)                  | `prod`                                                |
| `current_env`  | Current environment (fully qualified)             | `acme-corp/prod`                                      |
| `root_env`     | Root environment in import chain                  | `acme-corp/base`                                      |
| `trigger_user` | User who opened the environment                   | `alice`                                               |
| `body_hash`    | Hash of request body (for integrity)              | `sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=` |

#### Validating Requests

Your adapter should:

1. **Extract the JWT** from the `Authorization: Bearer <token>` header
2. **Verify the signature** using the public key from JWKS
3. **Validate standard claims**:
   - `aud` matches your adapter URL
   - `exp` has not passed (token not expired)
   - `iss` is your Pulumi Cloud instance
4. **Verify body integrity** by generating an [SRI hash](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) of the request body:
   - Compute SHA-256 hash of request body
   - Base64-encode the hash
   - Verify it matches the `body_hash` claim with `sha256-` prefix

The `body_hash` claim binds the JWT to the request body to prevent replay attacks where an attacker could reuse a valid JWT with a different request body.

### Example Adapter Implementation

Here's a complete adapter in Python that fetches secrets from environment variables:

```python
#!/usr/bin/env python3
"""
Example external provider adapter for Pulumi ESC.
Fetches secrets from environment variables.
"""

import hashlib
import base64
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

import jwt
from jwt import PyJWKClient

# Configuration
JWKS_URL = "https://api.pulumi.com/.well-known/jwks.json"
ADAPTER_URL = "https://my-adapter.example.com/fetch-secrets"
PORT = 8443

# Initialize JWKS client (caches keys automatically)
jwks_client = PyJWKClient(JWKS_URL)


def verify_body_hash(body: bytes, claims: dict) -> None:
    """Verify the body_hash claim matches the request body."""
    expected_hash = claims.get("body_hash")
    if not expected_hash:
        raise ValueError("Missing body_hash claim")

    # Compute SHA-256 hash in SRI format
    hash_digest = hashlib.sha256(body).digest()
    actual_hash = f"sha256-{base64.b64encode(hash_digest).decode('ascii')}"

    if actual_hash != expected_hash:
        raise ValueError(f"Body hash mismatch: expected {expected_hash}, got {actual_hash}")


class AdapterHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Extract token from Authorization header
            auth_header = self.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                self.send_error(401, "Missing or invalid Authorization header")
                return

            token = auth_header[7:]  # Remove "Bearer " prefix

            # Get signing key from JWKS and verify token
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

            # Parse request
            request = json.loads(body)
            secret_name = request.get("secretName")

            if not secret_name:
                self.send_error(400, "Missing required field: secretName")
                return

            # Fetch secret from environment variable
            secret_value = os.environ.get(secret_name)
            if not secret_value:
                self.send_error(404, f"Secret not found: {secret_name}")
                return

            # Return response
            response = {"value": secret_value}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except jwt.InvalidTokenError as e:
            self.send_error(401, f"Invalid token: {str(e)}")
        except Exception as e:
            self.send_error(400, str(e))


if __name__ == "__main__":
    # In production, use a proper HTTPS server with valid certificates
    server = HTTPServer(("", PORT), AdapterHandler)
    print(f"Adapter listening on port {PORT}")
    server.serve_forever()
```

To use this adapter:

```bash
# Install dependencies
pip install pyjwt cryptography

# Set environment variables with your secrets
export MY_API_KEY="secret-value-123"

# Run the adapter (in production, use proper HTTPS)
python adapter.py
```

ESC configuration:

```yaml
values:
  mySecrets:
    fn::open::external:
      url: https://my-adapter.example.com/fetch-secrets
      request:
        secretName: MY_API_KEY
```

## Schema Reference

### Inputs

| Property  | Type    | Description                                | Required | Default |
|-----------|---------|--------------------------------------------|----------|---------|
| `url`     | string  | HTTPS URL to your adapter service          | Yes      | -       |
| `request` | object  | Arbitrary JSON object sent to your adapter | No       | `{}`    |
| `secret`  | boolean | Whether to mark the response as secret     | No       | `true`  |

### Outputs

| Property   | Type   | Description                                 |
|------------|--------|---------------------------------------------|
| `response` | object | The JSON response from your adapter service |
