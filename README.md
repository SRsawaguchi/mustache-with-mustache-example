# MustacheでMustacheを作る
MustacheでMustacheを作るサンプルです。  

## ツール
- [asdf](https://asdf-vm.com/)
  - Pythonのバージョン管理に利用

## 初期化
```
python -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## テンプレート
`values.yaml`など、このスクリプトで埋め込む場合は {? ?} で囲む。  
:bulb: HTMLエスケープしない場合は`{{? ?}}`で囲む
:bulb: テンプレートファイルの先頭の`{{={? ?}=}}`を変えればこのデリミタは変更できる。部分的に変更することもできる。([ドキュメント参照](https://mustache.github.io/mustache.5.html))  

:bulb: `{{ }}`で囲まれたものは無視され、処理後もそのまま残る。`{? ?}`で囲まれた部分のみ、このスクリプトで展開される。  
```html
{{={? ?}=}}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ page_title }}</title>
</head>
<body>
    <main>
        {? content ?}
    </main>
    <footer>
        <div class="copyright">{{ copyright }}</div>
    </footer>
</body>
</html>
```

## 実行
```sh
python ./main.py -t ./template.html -v ./values.yaml
```

| オプション | 説明 | デフォルト |
| --- | --- | --- |
| -t, --template | テンプレートファイル | ./template.html |
| -v, --values | 埋め込む値が書いてあるyamlファイル | ./values.yaml |
