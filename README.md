# PySide6_project_template

[![Github Actions Workflow](https://github.com/DiogoCarapito/PySide6_project_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/PySide6_project_template/actions/workflows/main.yaml)

PySide6_project_template

Python version: 3.12

## cheat sheet

### setup

copy all files (folders, hidden and non-hidden files) to the higher directory
usefull if you clone the repo into your desired directory
ignore if clone and after change the name of the directory

```bash
mv PySide6_project_template/{*,.*} . && rm -r PySide6_project_template/
```

```bash
python3.12 -m venv .venv
```

activate venv mac/linux

```bash
source .venv/bin/activate
```

activate venv windows (powershell)

```bash
.venv\Scripts\activate
```

### build

#### nuitka

macos/linux (macos not working/linux not tested)

```bash
nuitka --onefile --standalone --enable-plugin=pyside6 --output-filename=Pyside6_app --noinclude-qt-plugins=iconengines --macos-app-icon=assets/logo/logo.icns --include-data-dir=assets=assets --include-data-dir=data=data main.py
```

windows

```bash
nuitka --onefile --standalone --enable-plugin=pyside6 --windows-console-mode=disable --output-filename=Pyside6_app --windows-icon-from-ico=assets/logo/logo.ico --include-data-dir=assets=assets --include-data-dir=data=data main.py
```

#### pyinstaller

macos/linux

```bash
pyinstaller --name Pyside6_app --onefile --windowed --icon=assets/logo/logo.icns --add-data=assets:assets --add-data=data:data main.py
```

windows

```bash
pyinstaller --name Pyside6_app --onefile --windowed --icon=assets/logo/logo.ico --add-data "assets;assets" --add-data "data;data" main.py
```
