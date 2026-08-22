{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Warning:** On a fresh installation the **first user to sign up becomes the administrator**, including the SAML administrator. Create the account you intend to own the organization before sharing the console URL. Enabling SAML does not by itself close email and password signup — set `PULUMI_DISABLE_EMAIL_SIGNUP` on the API container to do that, since hiding the option in the console leaves the underlying handler active.{{ with $inner }} {{ . }}{{ end }}
