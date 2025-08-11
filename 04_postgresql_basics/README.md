# Running PostgreSQL using Docker
 
### PostgreSQL image pull
```docker
docker pull postgres
```
 
### Environment variables
```bash
docker run postgres
 
[-] Error: Database is uninitialized and superuser password is not specified.
You must specify POSTGRES_PASSWORD to a non-empty value for the superuser.
For example, "-e POSTGRES_PASSWORD=password" on "docker run".
```
 
```bash
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

```bash
docker run --name postgres2025 -e POSTGRES_PASSWORD=password postgres
```

Enable detached mode using `-d`
```bash
docker run -d --name postgres2025-detached -e POSTGRES_PASSWORD=password postgres
```

