FROM pwn.red/jail
COPY --from=ubuntu / /srv
COPY cats /srv/app/run
COPY flag.txt /srv/app/flag.txt
ENV JAIL_ENV_FLAG=ctf{flag}
