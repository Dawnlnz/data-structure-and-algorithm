# Git 和 GitHub 的使用

## 使用 Git 建立本地仓库

### 1、git init 

把这个目录变成 Git 可以管理的仓库

### 2、git add file-name or folder name 

把文件添加到仓库。git add 后不但可以跟单一文件，还可以跟通配符，更可以跟目录。git add . 就是把当前目录下所有未追踪的文件全部add。

### 3、git commit -m "修改说明"

把文件提交到仓库。引号内可以添加此次修改的说明。

### 4、git remote add origin git@github.com:Dawnlnz/data-structure-and-algorithm.git

关联远程仓库。

### 5、git push -u origin master

把本地国库的所有内容推送到远程仓库上。