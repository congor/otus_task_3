# Console analysis application for the most frequent matches among the most frequent words for applications with open code

This is a tutorial work for the third task in the OTUS “Python web-developer” course.
Links to a task:
- https://gist.github.com/Melevir/5754a1b553eb11839238e43734d0eb79
- https://gist.github.com/Melevir/cd9f3f3935f9dfe34d78ae9b18f8e2b9

# Usage objective

The application analyzes, shows and saves to file, how frequently the most common words in code's parts repeat in a projects set.
For example, the result `('take', 5) 2` shows the word `take` was found `5` times inside each project for all `2` projects.
Next opportunities are available:
- code language: `python`;
- projects locations: local drives(for instance `sda1/projects/1` for the *nix-based OS or `C:\\projects\1` for the Windows OS), github.com-repositories(for instance `"https://github.com/congor/otus_task_1"`) ; 
- part of speach: `NN` - nouns and `VB` - verbs (for python);
- places for searching: `funtions` - functions names, `variables` - variables names;
- saving files format: `json`, `csv`.

# Main features:

- A programming language is Python 3.
- A settings file format is 'json'.
- Due to this application is for console usage, results are outputted to console in the form of column, where every string has a construction has mentioned in `Usage objective`.
- Results files are being saved in the path `code_analyzer/results` with a proper extensions.
- Due to parts of speech  is based on `nltk`-library algorithm, some words having different parts of speech may be recognized as not a required part of speech.
- The application considers a context of using every word in required places for searching and that way determines a proper part of speech that has been applied in these names and takes words have been used only in a part of speech.

# User guide

1. Clone or download with extracting this application.
2. Install required libraries:
```bash
$ pip install requiremets.txt
```
4. If there is a requirement, change settings in the settings file. It is located in the path `code_analyzer/settings/settings.json`.
- A formats for each settings have been mentioned in `Usage objective`.
- The default settings file has next structure and settings:
```
{
"code_language": "python",
"part_of_speech": "VB",
"searching_place": "functions",
"projects": [".", "https://github.com/congor/otus_task_1"],
"saving_format": "json"
}
```
3. Make sure that the folder `test_data` is not located inside the same folder where the main application file `code_analyzer.py` is. Otherwise the internal test mode will be launched.
5. Open console and from the folder `code_analyzer` launch the application file:
```bash
$ pyhon3 code_analyzer.py
```
6. Take results in console and the file with results in `code_analyzer/results`.

# Testing options

1. For internal testing put the folder `test_data` to inside the folder where the application file `code_analyzer.py` is and launch this application the same way has pointed above.