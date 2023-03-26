!!!!!!!!!!!!!!! backup
this information how to setap a runable docker postgres container and how to use it
save to knowledge base !!!
include readme from setup

the docker-compose file is working but i do not know
where the persistend data is saved
I have to change this so i can decide where the data lives

start docker-compose
docker-compose up -d

connect to postgres:
psql -h localhost -p 5432 -U postgres

maby set postgres user
POSTGRES_USER=postgres

delete all docker images
docker system prune
docker rmi $(docker images -a -q)
