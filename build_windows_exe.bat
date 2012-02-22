..\pyinstaller-1.5.1\Makespec.py -F -w --icon=resource/image/LotRLCG.ico Launcher.py
..\pyinstaller-1.5.1\Build.py Launcher.spec
rmdir /s /q build
move dist\*.exe .
rmdir dist

del Launcher.spec
del warnLauncher.txt
del *.log

echo Launcher.exe built
pause