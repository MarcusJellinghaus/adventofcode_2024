@echo off
REM Create the .vscode folder if it doesn't exist
if not exist .vscode mkdir .vscode

REM Create and initialize extensions.json
echo { > .vscode\extensions.json
echo   "recommendations": [ >> .vscode\extensions.json

REM Get the list of installed extensions and format them as JSON
for /f "delims=" %%E in ('code --list-extensions') do (
    echo     "%%E", >> .vscode\extensions.json
)

REM Remove the last comma (creates a temp file for safety)
powershell -Command "(gc .vscode\extensions.json) -replace ',\s*\]', ']' | sc .vscode\extensions_tmp.json"
move /y .vscode\extensions_tmp.json .vscode\extensions.json >nul

REM Finalize the JSON structure
echo   ]
echo } >> .vscode\extensions.json

REM Success message
echo extensions.json has been created successfully in the .vscode folder!
pause
