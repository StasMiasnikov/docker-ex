### Instructions

#### Start the deployment

* Clone this repo ```git clone https://github.com/StasMiasnikov/docker-ex.git```
* Open work folder ```cd docker-ex/src```
* Run start cmd ```docker compose up --build```

#### Run tests

* Open test folder ```cd docker-ex/test```
* Install needed dependencies ```pip install -r reqirements.txt```
* Run the tests ```pytest -v```

#### Build

* Open Jenkins in Browser ```http://localhost:8080/job/curl-build```
* Build the job
* After success build check build logs \ stages and
  artifacts ```http://localhost:8080/blue/organizations/jenkins/curl-build/detail/curl-build/1/pipeline```

#### Rerun CMD

```shell
docker compose rm --volumes -f && docker volume prune --all --force  && docker compose up --build --force-recreate --remove-orphans --renew-anon-volumes --always-recreate-deps
```

### Cleanup

```shell
docker compose rm --volumes -f && docker volume prune --all --force
```
