from pathlib import Path

# 1. Створення .gitignore
gitignore_content = """.idea/
.venv/
__pycache__/
"""
Path(".gitignore").write_text(gitignore_content)

# 2. Перейменування main.py на 1.py
main_file = Path("main.py")
if main_file.exists():
    main_file.rename("1.py")

# 3. Створення файлів 2.py, 3.py, 4.py
for i in range(2, 5):
    Path(f"{i}.py").touch()