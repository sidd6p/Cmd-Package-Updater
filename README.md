
# __SDK for dependencies check__

#### CMD based tool for verifying if the dependencies in the ```package.json``` file for Js based project is greater than or equal to the given inputs



## Directory stracture

dyte-vit-2022-sidd6p

    │   CHANGELOG.md
    │   LICENSE.txt
    │   README.md
    │
    ├───.github
    │       .keep
    │
    └───app
        ├───input.csv
        ├───readFile.py
        ├───repo.py
        ├───run.py
        ├───showTable.py
        ├───utils.py
        ├───__init__.py
## Run Locally

- [Deployment Video](https://youtu.be/AL4ydKZyoLo)


Clone the project

```bash
  git clone https://github.com/dyte-submissions/dyte-vit-2022-sidd6p.git
```

Go to the dyte-vit-2022-sidd6p directory
```bash
  cd dyte-vit-2022-sidd6p
```

Go to the app directory
```bash
  cd app
```


Install dependencies

```bash
  pip install -r requirements.txt
```

run the project

```bash
  python run.py -i input.csv axios@0.23.0
```



## Feature

- Take ```.csv``` file as input with repo url in it
- Search for the given repo using the url only
- Check for the given dependecy with the given input(dependecy)
- Show result 
    - If repo dependecy version is less, then False
    - Else True

    
## Tech & Tool

__Language__: [Python 3.10.1](https://www.python.org/)

__IDE__: [VS Code](https://code.visualstudio.com/)

__API__: [GitHub Api](https://api.github.com/)

## Authors

- [@sidd6p](https://github.com/sidd6p)
## Refrence

[Problem Statement ](https://dyte.notion.site/SDK-Tooling-Challenge-bdeecebf2cbf4afab3cb297e3c6a29d7)

[GitHub Api](https://docs.github.com/en/rest)


## Upcoming Feature

### Update

- Pull request using ```-u``` or ```--update``` cmd to update the un-updated dependencies 