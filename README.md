*This project has been created as part of the 42 curriculum by hwakatsu.*

# FuncMage

## Description / 説明

### English
FuncMage is a Python functional-programming project from the 42 curriculum. Its goal is to practice core functional concepts in Python through five small exercises: lambda expressions, higher-order functions, closures, `functools`, and decorators.

This repository is organized by exercise:

- `ex0/lambda_spells.py`: lambda expressions with sorting, filtering, mapping, and statistics
- `ex1/higher_magic.py`: higher-order functions and function composition
- `ex2/scope_mysteries.py`: closures, lexical scoping, and persistent state
- `ex3/functools_artifacts.py`: `reduce`, `partial`, `lru_cache`, and `singledispatch`
- `ex4/decorator_mastery.py`: decorators, retry logic, validation, and `@staticmethod`

### 日本語
FuncMage は、42 カリキュラムの Python 関数型プログラミング課題です。目的は、5 つの小さな演習を通して、lambda 式、高階関数、クロージャ、`functools`、デコレータといった主要な関数型プログラミングの考え方を実践的に学ぶことです。

このリポジトリは exercise ごとに構成されています。

- `ex0/lambda_spells.py`: lambda を使った並び替え、絞り込み、変換、統計計算
- `ex1/higher_magic.py`: 高階関数と関数合成
- `ex2/scope_mysteries.py`: クロージャ、レキシカルスコープ、状態保持
- `ex3/functools_artifacts.py`: `reduce`、`partial`、`lru_cache`、`singledispatch`
- `ex4/decorator_mastery.py`: デコレータ、リトライ処理、バリデーション、`@staticmethod`

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- No external dependencies

Run each exercise from the repository root:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

Optional style check:

```bash
flake8 ex0 ex1 ex2 ex3 ex4
```

There is no installation step. Clone the repository and run the files directly with Python.

### 日本語

必要環境:

- Python 3.10 以上
- 外部ライブラリ不要

リポジトリのルートで、各 exercise は次のように実行できます。

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

任意でコーディング規約チェックを行う場合:

```bash
flake8 ex0 ex1 ex2 ex3 ex4
```

インストール作業は不要です。リポジトリを取得したら、そのまま Python で各ファイルを実行できます。

## Features / 主な内容

### English

- Anonymous functions with `lambda`
- Function composition and higher-order design
- Closures with private persistent state
- Functional utilities from `functools`
- Reusable decorators and static methods

### 日本語

- `lambda` による無名関数
- 関数合成と高階関数の設計
- プライベートな状態を保持するクロージャ
- `functools` の主要ユーティリティ
- 再利用可能なデコレータと static method

## Resources / 参考資料

### English

Classic references related to the topic:

- [Python Documentation: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python Documentation: functools](https://docs.python.org/3/library/functools.html)
- [Python Documentation: Higher-order functions](https://docs.python.org/3/library/functions.html)
- [PEP 8](https://peps.python.org/pep-0008/)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support only.
- It helped structure this README, improve wording, and summarize the project requirements in both English and Japanese.
- The project code should still be reviewed, understood, and defended manually during peer evaluation.

### 日本語

この課題に関連する代表的な参考資料:

- [Python Documentation: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Python Documentation: functools](https://docs.python.org/3/library/functools.html)
- [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [PEP 8](https://peps.python.org/pep-0008/)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助のみに使用しました。
- README の構成整理、英語と日本語の表現調整、要件の要約に利用しました。
- 実装内容については、最終的に自分で確認し、理解し、peer review で説明できる状態にする前提です。

## More Information / 補足

### English
This project is meant to demonstrate understanding of functional programming patterns clearly and simply, rather than building a large application.

### 日本語
このプロジェクトの目的は大規模なアプリケーション開発ではなく、関数型プログラミングの考え方を明確かつシンプルに示すことです。
