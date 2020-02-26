#To Deploy

This may not be the best way to do this, I'm just learning and documenting as I go.

Once you have cloned this repository, you need to create a directory called `database-data` in this directory. This will persist the data that will be put into the postgres container. :

```
$ cd Learning/postgres_go/python/
$ mkdir database-data/
```

You will then need to create the python image which will be spun up by `docker-compose.yml`. :

```
$ docker build -t runenv python_image/
```

This builds an python image with backage installed via `pip`. Once built, you can confirm the image exists via :

```
$ docker images
REPOSITORY  TAG       IMAGE ID       CREATED         SIZE
runenv      latest    76d8f3b10efa   8 minutes ago   1.18GB
```

I have created a Docker compose file which direcs Docker to spin up two images. One is the postgres database and the other is the `runenv` we just created which we will go into and run code. Normally one would have the `runenv` run code upon deployment but this just runs `bash -c "sleep infinity"` which allows us to go into the container to run code - if a container has nothing to run it usually exits, i.e. is destroyed.

To spin us the database and run environment, run:

```
$ docker-compose up -d
Creating network "python_default" with the default driver
Creating my_postgres ... done
Creating runenv      ... done
```

Now go into the `runenv` container:

```
$ docker exec -it runenv /bin/bash
```

Run the code:
```
# cd /work/
# python get_data.py
(you should see data)
```

Tada!

Exit:

```
# exit
```

Tear down:

```
$ docker-compose down
```

Remove `runenv` image:

```
$ docker image rm runenv
```
