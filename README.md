# Portfolio
Full stack django application

---
## Initial settings to run the project locally
### git clone
To run this project locally, start by going to the [source](https://github.com/JoGorska/portfolio.git) of the project and use git clone command.


### venv
You can use any virtual enviroment tool to run this project locally. I used venv.

#### Create venv
```
python3 -m venv /path/to/new/virtual/environment
```
activate venv, the name of venv is shown in brackets before the path
```
source /path/to/venv/bin/activate

```
command to deactivate
```
deactivate
```
#### install requirements
Once venv is active:

```
pip3 install  -r requirements.txt
```
to update local requirements
```
pip3 freeze > requirements.txt --local
```