# 营销号屏蔽数据
这个仓库包含来自B站的营销号列表，包括Markdown(`.md`)、JSON(`.json`)和YAML(`.yaml`)等格式的数据。目的是帮助用户在各种屏蔽脚本中方便地屏蔽营销号。

## 如何使用
1. 克隆仓库
```bash
git clone https://github.com/Luna-Grace/Marketing-Account-Masking.git
# 中文Git使用命令: 中文git 克隆 https://github.com/Luna-Grace/Marketing-Account-Masking.git
```
2. 将数据集成到你的屏蔽脚本中。例如在可以接受特定格式的插件上粘贴/导入列表。
3. 通过定期拉取来确保列表更新
```bash
git pull
# 中文Git使用命令: 中文git 拉取
```
> [!NOTE]  
> 我不是某个屏蔽扩展的作者，也不对相关数据负责。  

## 贡献
欢迎任何形式的贡献，包括问题报告和数据更新。请按照以下步骤进行贡献:  

1. Fork 仓库
2. 创建你的分支
```bash
git checkout -b your_branch_name
# 中文Git使用命令: 中文git 新建分支 你的分支名
```
3. 在对应的**JSON**数据上做出你的修改
> [!WARNING]  
> 由于自动流会从JSON数据来生成其他格式的数据，所以请在JSON数据中修改，否则会被自动流覆盖掉。  
4. 暂存你的更改
```bash
git add .
# 这里假设你需要暂存所有修改
```
5. 提交你的修改
```bash
git commit -m '提交消息'
# 请尽量详细的描述您的修改，如果你在拉取请求中详细的话提交信息可以简略
```
6. 推送你的更改
```bash
git push origin your_branch_name
# your_branch_name 为你的分支名
```
7. 提交 Pull Request
8. \[如果检查出错\] 请查看Action输出，如果不是在`检查 UID 格式`这步出错请@Luna-Grace

## 许可证
此仓库使用[MIT](https://github.com/Luna-Grace/Marketing-Account-Masking/blob/main/LICENSE)许可证。有关详细信息，请查看许可证文件。

## 责任说明
我不对仓库中的数据担责，也不代表所有收录的账号都是真的营销号。**如果你的账号被错误的添加进了列表，请随时参照[上面的方法](#贡献)将你的账号信息从JSON数据中移除，然后提交Pull Request**。如果你不懂得Pull Request，你可以开个Issue。**你要让我知道并了解情况我才可以做出修改！  
我不对任何账号的内容表示认可与否，也不表达对账号内容的喜爱与否，如果账号内容存在问题与本仓库无关。  
所有数据由社区提供，我不对数据的准确性等担责。  
仓库中的脚本为@Luna-Grace编写，以[MIT](https://github.com/Luna-Grace/Marketing-Account-Masking/blob/main/LICENSE)许可证开源。  
