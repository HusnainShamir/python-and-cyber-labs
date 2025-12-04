:loop
git add .
git commit -m "Auto update"
git push
timeout /t 30 >nul
goto loop
