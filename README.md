python 3.9


```bash
pip install fastapi==0.78.0 "uvicorn[standard]==0.17.6"

pip install aiosqlite==0.17.0

pip install sqlalchemy==1.4.36

pip install alembic==1.7.7

alembic init --template async alembic

alembic revision --autogenerate -m "First migration"

alembic upgrade head

```
