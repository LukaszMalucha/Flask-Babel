## Flask Babel

##### Prepare .pot file
pybabel extract -F babel.cfg -o messages.pot --input-dirs=.

<br>

##### Translate to language
pybabel init -i messages.pot -d translations -l pl

<br>

##### Compile
pybabel compile -d translations

##### Update
pybabel update -i messages.pot -d translations

