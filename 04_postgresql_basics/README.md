# Running PostgreSQL using Docker
 
### PostgreSQL image pull
```docker
docker pull postgres
```
 
### Environment variables
```docker
docker run postgres
 
[-] Error: Database is uninitialized and superuser password is not specified.
You must specify POSTGRES_PASSWORD to a non-empty value for the superuser.
For example, "-e POSTGRES_PASSWORD=password" on "docker run".
```
 
```docker
docker run -e POSTGRES_PASSWORD=password postgres
 
[+] database system is ready to accept connections
```
 
### See running container logs
Display all logs generated to this point
```bash
docker logs "container name"
```
 
Stream logs in real time
```bash
docker logs -f "container name"
docker logs --follow "container name"
```
 
### Execute db commands inside the postgres container
The interactive terminal can be enabled using  `--it`
Specify the PostgreSQL username using `-U`
 
```bash
docker exec --it "container name" psql -U "postgres"
psql (15.2 (Debian 15.2-1))
Type "help" for help.

postgres=# \l
postgres=# create database postgres2025;
CREATE DATABASE
postgres=# \l
postgres=# exit
```

List all databases - `\l`

### Set the container name

```docker
docker run --name postgres2025 -e POSTGRES_PASSWORD=password postgres
```

Enable detached mode using `-d`
```docker
docker run -d --name postgres2025-detached -e POSTGRES_PASSWORD=password postgres
```

### Docker volumes
Data is lost when restarting or removing a container.
A volume is essentially a folder (in physical file system), mounted into the virtual file system of Docker (container). Data is then automatically replicated.

PostgreSQL container data storage directory: `/var/lib/postgres/data` 

There are 3 types of docker volumes:
- Host volumes
    * User sets the location of the volume folder on the host system
    * ```docker run -v /user/some/path/data:/var/lib/postgres/data ```
- Anonymous volumes
    * For each container, a folder is generated and mounted, automatically by Docker 
    * ```docker run -v /var/lib/postgres/data ```
- Named volumes
    * You can reference the volume by name, no need to know the exact path 
    * ```docker run -v name:/var/lib/postgres/data ```
    * `Named volumes` should be used in production 

```bash
docker run --name postgres-with-volume -e POSTGRES_PASSWORD=password -v /Users/user/docker/volumes/postgres/data:/var/lib/postgres/data postgres

docker exec -it postgres-with-volume psql -U postgres
postgres=# \l
postgres=# create database postgres2025;
CREATE DATABASE
postgres=# \l
postgres=# exit
```

Example using anonymous volumes
```bash
docker run --name postgres-anonymous-volume -e POSTGRES_PASSWORD=password -v /var/lib/postgres/data postgres

docker exec -it postgres-anonymous-volume psql -U postgres
```

Example using named volumes
```bash
docker run --name postgres-named-volume -d -e POSTGRES_PASSWORD=password -v named_volume:/var/lib/postgres/data postgres

docker exec -it postgres-named-volume psql -U postgres
```
