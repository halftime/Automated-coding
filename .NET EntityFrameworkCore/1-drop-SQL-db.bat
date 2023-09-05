rem Set MSSQLLocalDB name to drop
set sqlDBName=SQLDatbaseNameHere

rem CD to SSMS folder
cd "%ProgramFiles(x86)%\Microsoft SQL Server Management Studio 19\Common7\IDE"

rem command to drop database
sqlcmd -S "(LocalDb)\MSSQLLocalDB" -Q "DROP DATABASE %sqlDBName%;"

echo Database %sqlDBName% dropped
pause
