import os
import subprocess
import sys
import time

YML_PATH = os.path.join(os.path.dirname(__file__), ".github", "workflows", "ci.yml")

def run_ci():
    print("=" * 60)
    print("GitHub Actions Runner - Локальная эмуляция CI/CD")
    print(f"Конфигурация: {YML_PATH}")
    print("=" * 60)

    if not os.path.exists(YML_PATH):
        print(f"Файл {YML_PATH} не найден!")
        return 1

    with open(YML_PATH, "r", encoding="utf-8") as f:
        txt = f.read()

    print("[Шаг 1] Проверка синтаксиса workflow...")
    if "on:" in txt and "jobs:" in txt and "steps:" in txt:
        print("  -> YAML валиден.")
    else:
        print("  -> Ошибка синтаксиса YAML!")
        return 1

    print("\n[Шаг 2] Настройка окружения (ubuntu-latest, python 3)...")
    time.sleep(0.3)
    print("  -> Окружение готово.")

    print("\n[Шаг 3] actions/checkout@v4...")
    time.sleep(0.3)
    print("  -> Репозиторий готов к тестам.")

    print("\n[Шаг 4] Прогон тестов: pytest tests/ -v...")
    cur_dir = os.path.dirname(__file__)
    cmd = [sys.executable, "-m", "pytest", "tests", "-v"]
    p = subprocess.run(cmd, cwd=cur_dir, capture_output=True, text=True)
    print(p.stdout)
    if p.stderr:
        print(p.stderr)

    if p.returncode == 0:
        print("\n" + "=" * 60)
        print("СТАТУС CI: SUCCESS (Все тесты успешно пройдены!)")
        print("=" * 60)
        return 0
    else:
        print("\nСТАТУС CI: FAILED (Есть упавшие тесты).")
        return 1

if __name__ == "__main__":
    sys.exit(run_ci())
