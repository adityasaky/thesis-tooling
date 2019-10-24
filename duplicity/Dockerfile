FROM archlinux/base

LABEL maintainer="Aditya Saky <aditya@saky.in>"

RUN pacman-key --refresh

RUN pacman -Syyu --noconfirm duplicity 

COPY duplicity-repository-backup.sh /

ENTRYPOINT /duplicity-repository-backup.sh
