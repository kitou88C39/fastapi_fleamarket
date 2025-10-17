import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

# 1. 独自のメタデータオブジェクトをインポートします
#    プロジェクトの基盤となるモデルが定義されている場所です
from app.models import Base  # 例: 'app.models'からBaseをインポート

# alembic.iniから設定をロードします
config = context.config

# ロギングを設定します
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 2. ターゲットのメタデータを設定します
#    Alembicが既存のDBスキーマと比較する対象です
target_metadata = Base.metadata

# 設定ファイルからデータベースURLを取得します
# 'sqlalchemy.url' キーは alembic.ini ファイルで設定されている必要があります
DB_URL = config.get_main_option("sqlalchemy.url")


def run_migrations_offline() -> None:
    """オフラインモードでマイグレーションを実行します。

    DBに接続せず、生成されたSQLをファイルに出力する場合に使用します。
    """
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    """オンラインモードでマイグレーションを実行します。"""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """非同期（Async）接続を使用してオンラインモードでマイグレーションを実行します。
    
    FastAPIやモダンなPythonアプリケーションではこちらを使用することが推奨されます。
    """
    # 接続文字列を非同期ドライバー（例: postgresql+asyncpg）に変換します
    async_db_url = DB_URL.replace("postgresql", "postgresql+asyncpg") 

    connectable = create_async_engine(
        async_db_url,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # 非同期接続でトランザクションを実行するためにrun_syncを使用します
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    # オンラインモードの場合、非同期関数をイベントループで実行します
    async