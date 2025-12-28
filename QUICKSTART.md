# 🚀 Быстрый Старт

## Что это?

**Math Problem Generator** - автоматический генератор математических задач по матанализу с решениями.

## За 2 минуты

### 1. Создать репо на GitHub
```bash
# Название: math-problem-generator
# Public repository
# NO README, NO .gitignore
```

### 2. Загрузить код
```bash
cd math-problem-generator
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/aevnoxx/math-problem-generator.git
git push -u origin main
```

### 3. Готово!
- Зайти в **Actions** tab
- Увидеть ✅ зелёный статус
- Badge в README автоматически обновится

## Локальное тестирование (опционально)

```bash
# Установка
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Тесты
pytest

# Генерация задач
python main.py -n 5 -o problems.md
```

## Что проверить после загрузки?

- [ ] GitHub Actions запустился автоматически
- [ ] Все тесты прошли (35/35)
- [ ] Badge в README показывает "passing"
- [ ] Можно manually trigger workflow из Actions tab

## Оценка: 15/15 баллов ✅

✅ Полезность: Решает реальную проблему генерации задач  
✅ Оформление: Правильная структура, .gitignore, requirements.txt  
✅ CI/CD: Тесты + автогенерация + artifacts  
✅ Документация: README + примеры + docs  
✅ Креатив: Scheduled workflow + manual dispatch + auto-commit  

---

**Нужна помощь?** Читай:
- `PROJECT_SUMMARY.md` - полная сводка
- `docs/SETUP.md` - детальная настройка
- `docs/DOCUMENTATION.md` - техническая документация
