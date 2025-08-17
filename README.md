# MultiPosterSystem DataBuilder

## これは何？

MultiPosterSystem で使うポスターの動画データと、GroupIDのJSONデータを生成するためのスクリプトです。
GitHub Actions で動画データ・JSONデータの生成を行い、GitHub Pages にデプロイすることを想定しています。

## 使い方

1. 右上の Use this template -> Create a new repository を選択し、レポジトリを複製します。
   複製したレポジトリを、ローカル環境に clone します。
2. posters 以下に好きな名前のディレクトリを作成します。
3. 作成したディレクトリの中に、ポスターの画像を poster.png という名前で置きます。
4. 作成したディレクトリの中に、group_id という名前のファイルを作ります。
   ファイルには、ポスターに関連付けたいグループのIDを書き込みます。
5. データに含めたいポスターの数だけ、2～4の行程を繰り返します。
   この際、ポスターの順序はディレクトリ名の辞書順となることに留意してください。
6. 上記で作成したデータを全て commit し、複製したレポジトリへと push します。
7. GitHub の Setting -> Pages を開き、Build and Deployment の Source を GitHub Actions へと変更します。
8. GitHub の Actions から Build and Deploy の workflow を選択し、画面右側にある Run workflow を実行します。
9. しばらく待っていると `https://<ユーザー名>.github.io/<レポジトリ名>/` にWebページが生成されます。
   ここに、MultiPosterSystem で使うポスターの動画データと、GroupIDのJSONデータへのリンクが置いてあります。
