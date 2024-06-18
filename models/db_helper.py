from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import settings

engine = create_async_engine(settings.db_url)
async_session = async_sessionmaker(engine, autocommit=False, expire_on_commit=False, autoflush=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        await session.close()
