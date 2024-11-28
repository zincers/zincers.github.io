import os
import shutil
import frontmatter

def hexo_md_to_jekyll(
        hexo_dir: str = r"Z:\Temp\config_bak\hexo\source\_posts",
        jekyll_dir: str = "workdir"
):
    count = 0
    # 遍历指定目录及其子目录中的所有 .md 文件
    for root, dirs, files in os.walk(hexo_dir):
        for filename in files:
            count += 1
            print(f"当前所在目录是：{root}，相对路径是：{os.path.relpath(root, hexo_dir)}")
            print(f"开始处理第{count}篇文章：{filename}")
            if filename.endswith('.md'):
                source_path = os.path.join(root, filename)
                post = frontmatter.load(source_path)
                date = post["date"]
                title = post["translate_title"]

                destination_dir = jekyll_dir + os.sep + os.path.relpath(root, hexo_dir)
                os.makedirs(destination_dir, exist_ok=True)
                shutil.copy(source_path, destination_dir + os.sep+ str(date.date()) + "-" + title + ".md")
                    


if __name__ == "__main__":
    hexo_post_dir = r"Z:\Temp\config_bak\hexo\source\_posts"
    jekyll_post_dir = os.getcwd() + os.sep + '_posts'
    hexo_md_to_jekyll(hexo_dir = hexo_post_dir,jekyll_dir = jekyll_post_dir)