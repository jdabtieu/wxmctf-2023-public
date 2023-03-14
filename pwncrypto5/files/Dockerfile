FROM pwn.red/jail
COPY --from=ubuntu:20.04 / /srv
COPY vuln /srv/app/run
COPY flag.txt /srv/app/flag.txt
