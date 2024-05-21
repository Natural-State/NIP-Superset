# Local Deployment

## Docker

1) Verify the image you want to use and modify its tag in docker compose file

2) Rename docker/.env_local_example to .env_local and fill in the needed values

3) docker compose up

TODO

## Helm
Requirements:
* [Rancher Desktop](https://docs.rancherdesktop.io/getting-started/installation/)
* [helm](https://helm.sh/docs/intro/install/)

1) Verify the image you want to use and modify its information in values.override.yaml

2) Rename helm/.env_example to helm/.env and fill in the needed values

3) Export local variable environement 

``` bash
export $(grep -v '^#' ./helm/.env | xargs)
```

4) Update helm dependencies
``` bash
helm dependency update "./helm/superset"
```

5) Create a namespace: 
``` bash
kubectl create namespace $NAMESPACE
```

6) Deploy superset with local postgres db, you can add the option `--dry-run` to see check the configuration first
``` bash
helm upgrade \
    -n "$NAMESPACE" \
    "$HELM_RELEASE" \
    --install \
    "./helm/superset" \
    -f "./helm/superset/values.yaml" \
    -f "./helm/superset/values.override.yaml" \
    -f "./helm/superset/values.override.local.yaml" \
    --set "extraEnv.BASEURL=http://$DOMAIN_NAME" \
    --set "extraSecretEnv.SECRET_KEY=$SECRET_KEY" \
    --set "extraSecretEnv.SP_CLIENT_SECRET=$SP_CLIENT_SECRET" \
    --set "extraSecretEnv.ARM_TENANT_ID=$ARM_TENANT_ID" \
    --set "extraSecretEnv.SP_CLIENT_ID=$SP_CLIENT_ID" \
    --set "global.postgresql.auth.postgresPassword=superset" \
    --debug
```

7) In a new terminal: check the list of pods and run Direct 
``` bash
kubectl get pods -n $NAMESPACE
```
.....NIP-Superset % kubectl get pods -n $NAMESPACE
NAME                                        READY   STATUS    RESTARTS   AGE
superset-release-traefik-84bc8fc6c8-f4skd   1/1     Running   0          44s
superset-release-postgresql-0               1/1     Running   0          43s
superset-release-redis-master-0             1/1     Running   0          44s
superset-release-6486799596-rt5xg           0/1     Running   0          44s
superset-release-init-db-v2lzl              1/1     Running   0          42s
superset-release-worker-6f76ffcd46-9v8n7    1/1     Running   0          44s

8) Tunnel one pod's port into your localhost
``` bash
kubectl port-forward superset-release-6486799596-rt5xg 8088:8088 --namespace $NAMESPACE
``` 

Notes:
* You can clean up the local namespace by running:
``` bash
kubectl delete all --all -n $NAMESPACE 
```

