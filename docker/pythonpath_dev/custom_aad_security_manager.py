import logging
from superset.security import SupersetSecurityManager

logger = logging.getLogger()

class CustomAadSecurityManager(SupersetSecurityManager):
    #@appbuilder.sm.oauth_user_info_getter
    def oauth_user_info(
        sm: SupersetSecurityManager,
        provider: str,
        response=None,
    ) : #-> Dict[str, Any]:
        if provider == "azure":
            me = sm._decode_and_validate_azure_jwt(response["id_token"])
            name = (me.get("name", "notFound notFound")).split(" ")
            return {
                # To keep backward compatibility with previous versions
                # of FAB, we use upn if available, otherwise we use email
                "email": me["upn"] if "upn" in me else me["email"],
                "name": name,
                "first_name": name[0],
                "last_name":" ".join(name[1:]),
                "username": me["oid"],
                "role_keys": me.get("roles", []),
            }
        return {}