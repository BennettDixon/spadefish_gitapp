# :shell: Flask Backend! :shell:

This backend is a flask web api running locally in a docker container.
It can be run without docker as well, but we elected to use docker for its scalability, maintainability, and rapid testing capabilities.

## :running: Getting Started

* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - Operating system used. RECOMMENDED TO USE UBUNTU 18.04!

* [Python 3.4](https://www.python.org/download/releases/3.4.0/) - Python Version Used

* [Docker 18.06.1-ce](https://docs.docker.com/engine/release-notes/) - Docker Version Used -- Not supported on Ubuntu 14.04 anymore so setup is rough, ubuntu upgrade needed for project.

* [docker-compose 1.24.0](https://github.com/docker/compose/releases) - Docker compose version used. Installs fine on ubuntu 14.04 if you can get docker working.

## :warning: Prerequisites

* Must have `git` installed

* Must have repository cloned

* Must have `python3` installed

* Must have `kivy` installed

* Must have `docker` installed

* Must have `docker-compose` installed

```
$ sudo apt-get install git
```

```
$ sudo apt-get install python3
```

```
$ sudo apt-get install python3-kivy
```

```
(WARNING NOT TESTED)
$ sudo apt-get update
$ sudo apt-get -y install docker.io
$ ln -sf /usr/bin/docker.io /usr/local/bin/docker
$ sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io
```

```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

## :blue_book: Authors
* **Bennett Dixon** - [@BennettDixon](https://github.com/BennettDixon)

## :mag: License

This project is licensed under the MIT License - see the [LICENSE.md](TODO) file for details



## :mega: Acknowledgments

* Holberton School (providing guidance)
