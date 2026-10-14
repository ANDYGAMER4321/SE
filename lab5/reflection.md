# Lab 5 Reflection

## 1. What did the static-analysis tools find?

Pylint pointed out naming, docstring and return-value issues, along with the shared default dictionary and file encoding. Flake8 found formatting problems. Bandit warned about the shell command, the host address and the password string. When I ran the demo, I also noticed that changing the thermostat affected other devices because they shared the same settings dictionary.

## 2. How do Pylint, Flake8, and Bandit differ?

Pylint checks general code quality and possible bugs. Flake8 mainly checks style and formatting. Bandit looks for common security risks. They check different things, so using all three helped me find more issues.

## 3. Which changes mattered most, and why?

The main security fix was changing `run_scene` so it checks the scene path and runs the command without `shell=True`. I also changed the host to `127.0.0.1` and removed the unused password. For the device logic, I gave each device its own settings dictionary and added checks for missing devices. This stopped the settings bug and made the program safer.

## 4. What are the limitations of static analysis?

Static analysis does not prove that a program works in every situation. It can give warnings that need to be checked, and it may miss bugs that show up only when the program runs. I noticed the shared-settings bug by running the demo. The tools are useful, but testing the program and checking its output are still important.
