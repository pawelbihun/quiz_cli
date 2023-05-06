# Quiz in CLI

## A brief description
The script that loads a JSON file with the appropriate structure and based on it
runs a quiz that has a question and 4 possible answers. After going through all the questions
it is displayed how many questions the player answered correctly and the questions where are displayed
a mistake has been made along with information about the correct answer.
The project includes a sample exam for the ISTQB Foundation Level certificate
downloaded from [SJSI](https://https://sjsi.org/ist-qb/do-pobrania/) website.


## Lessons Learned

- Object-oriented programming in Python 
- Loading and using JSON file in Python scripts
- Working with virtual environment and Git
- Creating basic unit tests with the Pytest framework
- Using Pylint for enforcing the best coding standard

## Run Locally

Clone the project

```bash
  git clone https://github.com/pawelbihun/quiz_cli.git
```

Go to the project directory

```bash
  cd quiz_cli
```

Create virtual environment, e.g. venv

```bash
  python3 -m venv venv
```
Activate venv

```bash
  source venv/bin/activate
```
Install dependencies

```bash
  python3 -m pip install -r requirements.txt
```
Run quiz
```bash
  python3 main.py
```

## 🚀 About Me
I'm a software tester. More information on the [Linkedin](https://linkedin.com/in/pawel-bihun) profile.