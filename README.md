# Wellcome to osereum

It is the most popular and original osereum python script. The code is exceptionally portable and has been used successfully on a very broad range of ubuntu systems and hardware.

## Contact

[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/osereum-github/)
[![GitHub Issues](https://img.shields.io/badge/open%20issues-0-yellow.svg)](https://github.com/omgbbqhaxx/osereum/issues)

- Chat in [osereum-github channel on Gitter](https://gitter.im/osereum-github).
- Report bugs, issues or feature requests using [GitHub issues](issues/new).



## Getting Started

The osereum Documentation site hosts the **[osereum homepage](http://osereum.com/)**, which
has a Quick Start section.

Operating system | Status
---------------- | ----------
Ubuntu and macOS | [![TravisCI](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://travis-ci.org/osereum/osereum-github)
Windows          | [![AppVeyor](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://ci.appveyor.com/project/osereum/osereum-github)


```shell
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install vim -y && sudo apt-get install python-dev -y && sudo apt-get install libevent-dev -y &&  sudo apt-get install python-virtualenv -y && apt-get install git -y
```



## Install python last version..

```shell
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo apt-get install python3.4
sudo apt-get install python3-pip
pip install --upgrade virtualenv
```

## Other configurations..

```shell
virtualenv -p python3 venv
pip install -r requirements.txt
pipenv install requests
```


## After clone our project.

```shell
export DJANGO_SETTINGS_MODULE=osereum.settings
```




## Circus: A Process & Socket Manager configurations
The simplest way to install it is to use pip, a tool for installing and managing Python packages:
```shell
pip install circus
pip install circus-web
pip install chaussette
```

example.ini
```shell
[watcher:startserver]
cmd = /opt/venv/bin/gunicorn_start
numprocesses = 1
[watcher:starttcpconnections]
cmd = python /opt/venv/osereum/server.py
numprocesses = 1
```

The file is then passed to circusd:
```shell
circusd example.ini
```

You can exist from program if already running.
```shell
circusctl quit --waiting
```

# REST APIs

## GET Endpoints
 * `http://osereum.com/api/v1/createnewwallet/` - allows to create new wallet and private key.

 * `http://osereum.com/api/v1/alltransactions/` - allows to get all transactions from database.

 * `http://osereum.com/api/v1/gettransaction/$transactionID` - allows to get transaction details.

 * `http://osereum.com/api/v1/getwalletfrompkey/$publicKey` - allows to create new wallet and private key.

 * `http://osereum.com/api/v1/getpublickeyfromprikey/$privateKEY` - allows to get public key from private key.

 * `http://osereum.com/api/v1/getbalance/$wallet` - allows to get last balance from wallet.

 *  `http://osereum.com/api/v1/getwalletdetails/$wallet` - allows to get all wallet history.





## POST Endpoints
  * `http://osereum.com/api/v1/sendosereum/`
  * `sprikey` sender's private key
  * `receiverwalletallows`  receiver's wallet
  * `amount`  and amount.
  ___


## Donations
  * Project Osereum wallet : `OSR9b38133cea9c1b19ae0803baf7932d5`

## License

[![License](https://img.shields.io/github/license/ethereum/cpp-ethereum.svg)](LICENSE) [![Join the chat at https://gitter.im/osereum/Lobby](https://badges.gitter.im/osereum/Lobby.svg)](https://gitter.im/osereum/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

All contributions are made under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html). See [LICENSE](LICENSE).
