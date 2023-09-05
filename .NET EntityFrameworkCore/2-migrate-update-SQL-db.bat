rem configure variable to EFModel Folder
set EFModelPath=Z:\PathTo\DotnetProject\ModelFolder\

rem configure variable EFModel subfolder containing migrations
set EFModelMigrationsPath=Migrations


rem Cleanup migrations \Migrations\ subfolder
del "%EFModelPath%%EFModelMigrationsPath%\*.cs" /Q

rem CD back to \EFModel\ main project folder
cd "%EFModelPath%"

rem dotnet command to make migration
dotnet ef migrations add autoMigration

rem dotnet command to update database
dotnet ef database update

rem Cleanup EFModel\Migrations\ folder
del "%EFModelPath%%EFModelMigrationsPath%\*.cs" /Q

echo Migrating, db update and cleanup. Done
pause
