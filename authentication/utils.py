import base64
import hashlib
import secrets


def generate_pkce_pair() -> tuple[str, str]:
    """
    Genera un par `code_verifier` y `code_challenge` para el flujo PKCE de OAuth 2.0.

    El `code_verifier` es una cadena aleatoria criptográficamente segura (como un secreto temporal).
    El `code_challenge` es su versión hasheada (SHA-256 + Base64 URL-safe), lista para enviar
    al servidor de autorización.

    Esto protege el flujo de autorización contra ataques de interceptación, cumpliendo con el
    estándar PKCE (RFC 7636).

    Returns:
        tuple[str, str]: Par (code_verifier, code_challenge), donde:
            - code_verifier: La cadena secreta original (43-128 caracteres alfanuméricos + '-._~')
            - code_challenge: Su versión hasheada en Base64 URL-safe sin padding

    Referencias:
        - [RFC 7636 - PKCE](https://datatracker.ietf.org/doc/html/rfc7636)
    """
    code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(64)).rstrip(b'=').decode()
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b'=').decode()

    return code_verifier, code_challenge
