# px-locust

## Change Locust number of users and hatch rate
```
kubectl exec <locust pod name> -- ./locust_updater.sh <number of users> <hatch rate>
```

## Set host address with the environment variable FRONTEND_ADDR:
```
export FRONTEND_ADDR="<address to host>"
```
To set up the host you don't need to add 'http://', that part of the address is already added by the service running Locust.
