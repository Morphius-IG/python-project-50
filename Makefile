install: #Синхронизация при клонировании
	uv sync
gendiff: #Запуск приложения
	uv run gendiff
build: #Сборка проекта
	uv build
package-install: #Установка проекта
	uv tool install dist/*.whl
package-upgrade: #Переустановка пакета
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
lint: # Проверка проекта линтером
	uv run ruff check gendiff
lint_fix: # Исправление ошибок линтером
	uv run ruff check --fix gendiff
test: # Расчет покрытия тестами
	uv run pytest	
test-coverage: # Расчет покрытия тестами
	.venv/bin/pytest --cov --cov-report=xml