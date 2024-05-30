
#!/bin/bash


# Usage examples:
# deploy_superset "app-name" "superset-namespace" "superset-release" "example.com" "tls-secret" "mapbox-api-key" "db-host" "db-username" "db-password"

# Function to deploy Superset
deploy_superset() {
    NAMESPACE="$0"
    HELM_RELEASE="$1"
    DOMAIN_NAME="$2"
    TLS_SECRET_NAME="$3"
    DB_HOST="$4"
    DB_USERNAME="$5"
    DB_PASSWORD="$6"
    MAPBOX_API_KEY="$7"
    SMTP_USER="$8"
    SMTP_PASSWORD="$9"
    SMTP_MAIL_FROM="$10"
    SECRET_KEY="$11"
    SP_CLIENT_SECRET="$12"
    ARM_TENANT_ID="$13"
    SP_CLIENT_ID="$14"
    ENV="$15"

    echo "Namespace: $namespace"
    echo "Helm release: $helm_release"
    echo "Domain name: $DOMAIN_NAME"
    echo "TLS Secret: $TLS_SECRET_NAME"
    # Helm dependency update
    helm dependency update "../../helm/superset"
    
    # Deploy superset with override
    helm upgrade \
    -n "$NAMESPACE" \
    "$HELM_RELEASE" \
    --install \
    "../../helm/superset" \
    -f "../../helm/superset/values.yaml" \
    -f "../../helm/superset/values.override.yaml" \
    -f "../../helm/superset/values.override.$ENV.yaml" \
    --set "extraSecretEnv.MAPBOX_API_KEY=$MAPBOX_API_KEY" \
    --set "extraEnv.BASEURL=\"https://$DOMAIN_NAME\"" \
    --set "extraSecretEnv.SMTP_USER=$SMTP_USER" \
    --set "extraSecretEnv.SMTP_PASSWORD=$SMTP_PASSWORD" \
    --set "extraSecretEnv.SMTP_MAIL_FROM=$SMTP_MAIL_FROM" \
    --set "extraSecretEnv.SECRET_KEY=$SECRET_KEY" \
    --set "extraSecretEnv.SP_CLIENT_SECRET=$SP_CLIENT_SECRET" \
    --set "extraSecretEnv.ARM_TENANT_ID=$ARM_TENANT_ID" \
    --set "extraSecretEnv.SP_CLIENT_ID=$SP_CLIENT_ID" \
    --set "supersetNode.connections.db_host=$DB_HOST" \
    --set "supersetNode.connections.db_user=$DB_USERNAME" \
    --set "supersetNode.connections.db_pass=$DB_PASSWORD" \
    --set "ingress.tls[0].secretName=$TLS_SECRET_NAME" \
    --set "ingress.tls[0].hosts[0]=\"$DOMAIN_NAME\"" \
    --set "ingress.hosts[0]=\"$DOMAIN_NAME\"" \
    --debug
}
