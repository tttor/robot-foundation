# py: python

## best practice
* standard modules: https://pymotw.com/3/
* py style: https://www.python.org/dev/peps/pep-0008/
* refactoring: https://martinfowler.com/books/refactoring.html
* code analyzer
  * https://pypi.org/project/pylint/
  * http://pylint-messages.wikidot.com/

## python3
* `sudo apt install python3-pip`
* `sudo apt install python3-dev`
* `sudo apt-get install python3-tk`
* `sudo pip3 install -U numpy`
* `sudo pip3 install -U pyaml`
* `sudo pip3 install -U matplotlib`
* `sudo update-alternatives --config python3` # switch between the two python versions for python3

## python virtual env
* `sudo apt-get install python-virtualenv`
* `virtualenv --system-site-packages -p python3 <targetDirectory>`

## misc
* ipynb to py: https://stackoverflow.com/questions/37797709/convert-json-ipython-notebook-ipynb-to-py-file
  * `jupyter nbconvert --to script 'my-notebook.ipynb'`
* https://stackoverflow.com/questions/13520876/how-can-i-make-multiple-empty-lists-in-python
  * `lists = [[] for _ in range(n)]`
  * NOT: `lists = [[]] * 5`
* https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
* https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
* https://stackoverflow.com/questions/222877/what-does-super-do-in-python
* https://stackoverflow.com/questions/15719172/overload-operator-in-python
* https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
* https://stackoverflow.com/questions/4015417/python-class-inherits-object
* https://stackoverflow.com/questions/4780088/what-does-preceding-a-string-literal-with-r-mean
* https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
* https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists
* https://stackoverflow.com/questions/400739/what-does-asterisk-mean-in-python
