# Пути
LOCALES_DIR = locales
POT_FILE = $(LOCALES_DIR)/messages.pot
BABEL_CFG = babel.cfg

# Команда: make update
# Извлекает строки и обновляет .po
update:
	@echo "🔍 Извлечение сообщений в $(POT_FILE)..."
	pybabel extract -F $(BABEL_CFG) -o $(POT_FILE) .
	@echo "♻️  Обновление .po файлов..."
	pybabel update -i $(POT_FILE) -d $(LOCALES_DIR)
	@echo "✅ Обновление завершено. Внесите переводы в .po вручную."

# Команда: make compile
# Компилирует .po → .mo
compile:
	@echo "🛠 Компиляция переводов .po → .mo..."
	pybabel compile -d $(LOCALES_DIR)
	@echo "✅ Компиляция завершена."

# Команда: make init LANG=xx
# Инициализирует новый язык
init:
ifndef LANG
	$(error ❌ Укажи язык: make init LANG=de)
endif
	@echo "🌐 Инициализация перевода для языка '$(LANG)'..."
	pybabel init -i $(POT_FILE) -d $(LOCALES_DIR) -l $(LANG)
	@echo "✅ Добавлен locales/$(LANG)/LC_MESSAGES/messages.po — переведи и сделай 'make compile'"
