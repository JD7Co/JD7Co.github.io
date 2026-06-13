Backend (FastAPI)

Новые endpoints (реферальная система и аналитика):

- GET /partners
  - Возвращает список партнёров (поля: id, name, commission_percent, referral_url, partner_code)

- POST /partners/{partner_id}/click
  - Регистрирует клик по реферальной ссылке. Увеличивает счётчик clicks.

- POST /partners/{partner_id}/conversion
  - Тело: { "amount_usd": float }
  - Регистрирует конверсию/покупку. Увеличивает conversions и суммирует revenue_usd.

- GET /partners/{partner_id}/reports
  - Возвращает базовый отчет: clicks, conversions, revenue_usd, estimated_commission_usd

- POST /partners/register
  - Простейшая регистрация партнёра (для demo). Генерирует partner_id, partner_code и placeholder referral_url.

Публичные реферальные ссылки в partners_db — placeholder вида https://provider.com/?ref=JD7CO_{PROVIDER}. Если вы хотите хранить реальные реферальные ссылки как секреты, перенесите их в .env или секреты CI/CD и используйте redirect-ендпоинт который выполнит переадресацию на реальный URL.

Запуск как раньше: uvicorn main:app --reload --host 0.0.0.0 --port 8000
