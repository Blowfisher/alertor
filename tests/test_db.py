import pytest
import sqlite3
from bambo.db import get_db

def test_get_close(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raise(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)    
    
def test_init_db_command(runner,monkeypatch):
    class Recorder(object):
        called = False
    
    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('bambo.db.init_db',fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialzed' in result.output
    assert Recorder.called
