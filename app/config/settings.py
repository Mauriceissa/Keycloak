from fetch_secret import access_secret_version
from certificates import save_certificate_as_temp_file


class Config:
    """
    Config class to store configuration variables like token expiration and database information.
    These can be set as environment variables or hardcoded for local development.
    """

    # DB variables
    PROJECT_ID = "insert project id"
    DATASET_ID = "insert dataset id"
    TABLE_ID = "insert table id"

    DEBUG = True

    # keycloak
    KEYCLOAK_SERVER_URL = "insert VM pub ip adress"
    KEYCLOAK_REALM = "lkeycloak realm"
    KEYCLOAK_CLIENT_ID = access_secret_version(PROJECT_ID, "Keycloak_client_id")
    KEYCLOAK_CLIENT_SECRET = access_secret_version(PROJECT_ID, "Keycloak_client_secret")
    KEYCLOAK_ADMIN_USER = "admin username"
    KEYCLOAK_ADMIN_PASSWORD = access_secret_version(
        PROJECT_ID, "Keycloak_admin_password"
    )

    # certs

    KEYCLOAK_CERT_PATH = save_certificate_as_temp_file(
        access_secret_version(PROJECT_ID, "server_cert")
    )
