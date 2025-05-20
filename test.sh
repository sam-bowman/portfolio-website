rm -r ./src/portfolio_website.tests/TestResults
dotnet test ./src/portfolio_website.sln --logger "trx;logfilename=testResults.trx" --collect "XPlat Code Coverage"