This is the software stack enviroment used to generate the documentation:

# Get the SSS env which has the sphinx napoleon extension
module load scitools/default-2021_03_18-1

To create the sphinx sources when new packages/modules are added/removed, run the following commands:

cd 2020/doc
rm -r source/aoc  # May be a null op - depending on whether autogen contents present
sphinx-apidoc -o source/aoc/ ../ '../day_*/Python/test*'

To create the html:

make html
gio open build/html/index.html
