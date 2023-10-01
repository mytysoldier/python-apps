## 作成ステップ
* .protoファイルを編集する
* `python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. example.proto`
` コマンドを実行
* クライアント、サービスクラスを実装
* 実行