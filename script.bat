@echo off
set "CurDir="
for %%a in ("%cd%") do set "CurDir=%%~nxa"
if NOT "%CurDir%" == "assignment1" exit

if exist %CD%"/src/test/testcases/" (
    echo "Cleaning testcases"
	rmdir /Q /S %CD%"/src/test/testcases/"
)
    echo "Creating testcases"
    mkdir %CD%"/src/test/testcases"


if exist %CD%"/src/test/solutions/" (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%"/src/test/solutions/"
)
    echo "Creating solutions"
    mkdir %CD%"/src/test/solutions"


if exist %CD%"/test/solutions/" (
    echo "Copying solution sample"
    robocopy  %CD%"\test\solutions" %CD%"\src\test\solutionsSample" /move
)

if exist %CD%\test\check.py (
    echo "Copying check.py"
    robocopy  %CD%"\test" %CD%"\src" check.py /move
)

cd src

echo "Cleaning and Generatting..."
python run.py clean
python run.py gen

echo.
echo "=============================================="
echo "Testing Lexer..."
python run.py test LexerSuite

echo.
echo "=============================================="
echo "Testing Parser..."
python run.py test ParserSuite

if exist %CD%"/test/solutionsSample/" (
    echo.
    echo "=============================================="
    echo "Checking solution..."
    echo.
    python check.py

    start check.txt
)

::pause >nul