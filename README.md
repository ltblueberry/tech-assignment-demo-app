# tech-assignment-demo-app
Demo application for devops/platform/infrastructure technical assignments to work with as an example.

The application simply returns the name of the host where it is running.

## Requirements
- **Python 3** >=3.8.2
- **virtenv** (Python 3 module) - for local environment 

## Virtul environment

```
python3 -m venv virtenv
source ./virtenv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run the application localy
```
python application.py
```

## Check the application
```
curl http://localhost:5000
```