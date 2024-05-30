from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import tkinter as tk

# 准备报告和专家 ID 列表
baogao_id = 879916
zhuanjia_id_list = [_ for _ in range(40000,50000)]  # 备选专家 ID 列表

def creat_message_win(text):
    root = tk.Tk()
    root.geometry("500x150")
    label = tk.Label(root, text=text)
    label.pack(pady=10)
    button1 = tk.Button(root, text="确定", command=root.quit)
    button1.pack(side=tk.BOTTOM, pady=5)
    root.mainloop()
    root.destroy()


# 创建一个新的Tkinter窗口
root = tk.Tk()
# 将窗口隐藏，因为我们只需要输入框
root.withdraw()


creat_message_win('请使用秘书账号进行登陆，随后点击一下培养管理即可。(请在20s内完成)')

# 创建WebDriver实例，这里以Chrome为例
driver = webdriver.Chrome()

# 打开登录页面
login_url = 'https://sep.ucas.ac.cn/'
driver.get(login_url)

# 等待页面加载完成
time.sleep(20)  # 等待足够长的时间确保页面及其JavaScript加载完成


# 构建匹配的专家 URL
def construct_url(baogao_id, zhuanjia_id):
    return f"https://py.ucas.ac.cn/zh-cn/Pingyue/ChakanEmaillog?baogao_id={baogao_id}&zhuanjia_id={zhuanjia_id}&nid=1"

# 匹配的专家 ID 列表
matched_experts = []


# 遍历专家 ID 列表
for zhuanjia_id in zhuanjia_id_list:
    url = construct_url(baogao_id, zhuanjia_id)
    driver.get(url)

    # 等待页面加载并检查当前页面 URL
    try:
        # 使用显式等待
        WebDriverWait(driver, 0.7).until_not(
            lambda driver: driver.current_url.startswith("https://py.ucas.ac.cn/zh-cn/home/sorry")
        )
        matched_experts.append(zhuanjia_id)
        print(f"Match found for zhuanjia_id {zhuanjia_id}")
    except TimeoutException:
        continue

# 关闭浏览器
driver.quit()

# 保存匹配的专家 ID 到文件
with open('matched_experts.txt', 'w') as file:
    for expert_id in matched_experts:
        file.write(f"{expert_id}\n")

print("Matching completed. See matched_experts.txt for results.")
