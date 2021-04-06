This is the software stack enviroment used to generate the documentation:

/net/project/ukmo/scitools/opt_scitools/environments/default/2021_03_18-1

To create the sphinx sources when new packages/modules are added/removed, run the following commands:

rm -r source/aoc
sphinx-apidoc -o source/aoc/ ../ '../day_*/Python/test*'

To create the html:

make html
