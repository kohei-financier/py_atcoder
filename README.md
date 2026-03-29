## Atcoder ABCのPythonテンプレート

# コンテストディレクトリ作成
acc new abc321

# テスト実行
cd abc321/a
uv run oj test -c "python main.py"

# 提出
acc submit main.py -- --guess-python-interpreter pypy