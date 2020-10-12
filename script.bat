@echo off
set "CurDir="
for %%a in ("%cd%") do set "CurDir=%%~nxa"
if "%CurDir%" == "assignment1" cd src

echo %CD%

if exist %CD%"/test/testcases/" (
    echo "Cleaning testcases"
	rmdir /Q /S %CD%"/test/testcases/"
    echo "Creating testcases"
    mkdir %CD%"/test/testcases"
)

if exist %CD%"/test/solutions/" (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%"/test/solutions/"
    echo "Creating solutions"
    mkdir %CD%"/test/solutions"
)


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

pause >nul