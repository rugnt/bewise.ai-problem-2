import os

from envparse import Env

env = Env()

TEMPLATES_URL = os.path.join(os.getcwd(), 'templates')
MEDIA_URL = os.path.join(os.getcwd(), 'media')

USERNAME_POSTGRESQL = env.str("POSTGRES_USER", default="postgres")
PASSWORD_POSTGRESQL = env.str("POSTGRES_PASSWORD", default="postgres")
DATABASE_POSTGRESQL = env.str("POSTGRES_DB", default="testcase2")
PORT_POSTGRESQL = env.str("PORT_POSTGRESQL", default=5432)
DATABASE_HOST = env.str("DATABASE_HOST", default="0.0.0.0")

DATABASE_URL = f"postgresql+asyncpg://{USERNAME_POSTGRESQL}:{PASSWORD_POSTGRESQL}" \
                       f"@{DATABASE_HOST}:{PORT_POSTGRESQL}/{DATABASE_POSTGRESQL}"

ALEMBIC_DATABASE_URL = f"postgresql://{USERNAME_POSTGRESQL}:{PASSWORD_POSTGRESQL}" \
                               f"@{DATABASE_HOST}:{PORT_POSTGRESQL}/{DATABASE_POSTGRESQL}"

APP_PORT = env.int("APP_PORT", default=8000)
