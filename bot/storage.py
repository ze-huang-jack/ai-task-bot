from __future__ import annotations
from sqlmodel import SQLModel, Session, create_engine, select
from models.task import Task

# SQLite 数据库 —— 本地文件
engine = create_engine("sqlite:///tasks.db")

# 初始化数据库
def init_db():
    SQLModel.metadata.create_all(engine)

# 保存任务
def save_task(text: str, category: str, next_action: str):
    task = Task(text=text, category=category, next_action=next_action)
    with Session(engine) as session:
        session.add(task)
        session.commit()

# 查询所有任务
def list_tasks():
    with Session(engine) as session:
        statement = select(Task).order_by(Task.id.desc())
        results = session.exec(statement).all()
        return results
