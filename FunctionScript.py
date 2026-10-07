import sys
import os
#https://github.com/FSweb-2026/FunctionScript 
    

def a():
    pass
import re

VAR = {}
def scope(int1,int2):
    return range(int1,int2)
# 全局函数库
FUN = {}
import json

def JAR_LIST(A,T):
        if T == True:
            OutPut(list(A))
        else:
            list(A)

def JAR_DICTIONARY(B,F):
        if F == True:
            OutPut(dict(B))
        else:
            dict(B)

def JAR_NUMBERS(number,t):
        if t == True:
            OutPut(int(number))
        else:
            int(number)

def JAR_DECIMALL(numbers,s):
        if s == True:
            OutPut(float(numbers))
        else:
            float(numbers)

def JAR_STRS(Strs,T_f):
        if T_f == True:
            OutPut(str(Strs))
        else:
            str(Strs)


#===========list===================
def ADD_LISTS(lists,DS):
    lists.append(DS)
    OutPut(lists)
        
def MOVE_LISTS(lists,DS):
    lists.pop(DS)
    OutPut(lists)

def CHANGE_LISTS(LISTS,DS,ints):
    LISTS[ints] = DS
    OutPut(LISTS)

def FIND_LISTS(lists,ints,l):
    if l == True:
        OutPut(lists[ints])
    else:
        lists[ints]
#+=======================================
#============dict===================
    
def ADD_DICTIONARY(dicts,keys,values):
    dicts[keys] = values

def MOVE_DICTIONARY(dicts,keys):
    dicts.pop(keys)

def CHANGE_DICTIONARY(dicts,keys,values):
    dicts[keys] = values

def FIND_DICTIONARY(dicts,keys):
    OutPut(dicts[keys])
#==========================================
def STRS_FIND(STR,INT,T_F):
    if T_F == True:
        OutPut(STR[INT])
    else:
        STR[INT]

def STRS_FINDMANY(STR,INT1,INT2,t_f):
    if t_f == True:
        OutPut(STR[INT1:INT2])
    else:
        STR[INT1:INT2]

def FILE_READ(file):
    a = open(file=file,mode='r',encoding='utf-8')
    print(a.read())
    a.close 
def FILE_WRITE(file,str):
    a = open(file=file,mode='w',encoding='utf-8')
    a.write(str)
    a.close 
def STRSLIST(strss,strs,stre):
    print(str(strss)+str(strs)+str(stre))

def CHANGESTRS(strs,mode):
    OutPut(strs.encode(mode))

def RETURESTRS(strs,mode):
    OutPut(strs.decode(mode))

def TAKE(dx):
    __import__(dx)

#==================================================================================================
'''
root = None
code_box = None
output_box = None
_running = False
_wait_input = False
_input_buf = ""
'''
#====================================GUI===============================================================#

import tkinter as tk
from tkinter import filedialog
import re

# ========== 全局变量 ==========

# ========== 安全输入函数 ==========
'''
def IPT(prompt=""):
    global _wait_input, _input_buf
    
    if not root_exists:
        return ""

    try:
        output_box.config(state=tk.NORMAL)
        output_box.insert(tk.END, prompt)
        output_box.see(tk.END)
        output_box.focus()
    except:
        return ""

    _wait_input = True
    _input_buf = ""

    def temp_enter(e):
        global _input_buf, _wait_input
        try:
            _input_buf = output_box.get("insert linestart", "insert").strip()
        except:
            _input_buf = ""
        _wait_input = False
        return "break"

    output_box.bind("<Return>", temp_enter)

    while _wait_input and _running and root_exists:
        try:
            root.update_idletasks()
            root.update()
        except:
            break

    output_box.unbind("<Return>")

    try:
        output_box.insert(tk.END, "\n")
        output_box.config(state=tk.DISABLED)
    except:
        pass

    return _input_buf
'''
#======================================================
'''
def OutPut(*args, sep=' ', end='\n'):

    global output_box
    if output_box is None:
        return
    try:
        text = sep.join(map(str, args)) + end
        output_box.config(state=tk.NORMAL)
        output_box.insert(tk.END, text)
        output_box.see(tk.END)
        output_box.config(state=tk.DISABLED)
    except Exception:
        pass
'''
# ========== 窗口关闭 ==========




### 3. run_code 里面，执行 exec 前加

## 修复 2：OutPut 函数，增

## 修复 2：OutPut 函数，增加空判断（防止 output_box 是 None 调用.config）   

## 修复 2：OutPut 函数，增加空判断（防止 output_box 是 None 调用.config）

# ========== 主窗口 ==========

# 1.读取json

root = tk.Tk()


root.title('FunctionScript')
root.geometry('1100x800')


code_box = tk.Text(root, font=("Menlo",12))
code_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)


def syntax_highlight():
    print("=====高亮执行====")
    import os, json, re
    base_dir = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(base_dir, "syntax.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    theme = data["theme"]
    patterns = data["patterns"]

    # 【放进函数内部！每次先重新配置所有tag颜色！】
    for tag_name, opt in theme.items():
        code_box.tag_config(tag_name, foreground=opt["foreground"])

    # 清除旧标记
    for tname in theme.keys():
        code_box.tag_remove(tname, "1.0", tk.END)

    # 逐行扫描
    end_line = int(code_box.index(tk.END).split(".")[0])
    for line_no in range(1, end_line + 1):
        line_start = f"{line_no}.0"
        line_end = f"{line_no}.0 lineend"
        line_text = code_box.get(line_start, line_end)

        for item in patterns:
            tag = item["tag"]
            raw_re = item["regex"]
            pat = re.compile(raw_re, re.DOTALL)
            for m in pat.finditer(line_text):
                c1 = m.start()
                c2 = m.end()
                idx1 = f"{line_no}.{c1}"
                idx2 = f"{line_no}.{c2}"
                print(f"MATCH L{line_no} [{idx1} {idx2}] word={m.group()} tag={tag}")
                code_box.tag_add(tag, idx1, idx2)


### 配套说明

root.rowconfigure(3, weight=4)
root.rowconfigure(0, weight=0)
root.columnconfigure(0, weight=1)
root.config(bg="#4E4E4E")
frame_btn = tk.Frame(root, bg="#8e8e8e")
frame_btn.grid(row=0, column=0, sticky="w", padx=10, pady=5)

from tkinter import ttk

style = ttk.Style()
style.theme_use("classic")  # 切换到classic主题，这个主题允许改按钮背景

    # 自定义按钮样式
style.configure("MyBtn.TButton",
    background="#0a0a0aac",
    foreground="#100F0F",
    padding=6
)

#ttk.Button(frame_btn, text="run", width=8, command=run_code).grid(row=0, column=0, padx=3)
#ttk.Button(frame_btn, text="save", width=8, command=save_file).grid(row=0, column=1, padx=3)
#ttk.Button(frame_btn, text="open", width=8, command=open_file_wrapper).grid(row=0, column=2, padx=3)

    # ========== 代码框 ==========
code_box = tk.Text(root,bg="#555555",fg='#ffffff', font=("黑体", 14), wrap=tk.NONE)
code_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

sx = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=code_box.xview)
sx.grid(row=2, column=0, sticky="ew", padx=10)
sy = tk.Scrollbar(root, orient=tk.VERTICAL, command=code_box.yview)
sy.grid(row=1, column=1, sticky="ns")
code_box.config(xscrollcommand=sx.set, yscrollcommand=sy.set)
    

    # ========== 输出框 ==========
output_box = tk.Text(root,bg="#484646",fg='#FFFFFF', font=("黑体", 12), wrap=tk.NONE, state=tk.DISABLED)
output_box.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

osy = tk.Scrollbar(root, orient=tk.VERTICAL, command=output_box.yview)
osy.grid(row=3, column=1, sticky="ns")
output_box.config(yscrollcommand=osy.set)

root.rowconfigure(1, weight=0)  # 代码框
root.rowconfigure(1, weight=0)  # 输出框





# ========== 按钮 ==========
'''
frame_btn = tk.Frame(root)
frame_btn.grid(row=0, column=0, sticky="w", padx=10, pady=5)
'''

def parse_blocks(src):
    text = src
    pos = 0
    output = []
    # 块开始标记：捕获所有块头部
    block_start_pat = re.compile(
        r"""(?mx)
        (JudgeIf:\[.*?\]\()
        |(JudgeElse\()
        |(loop\|.*?\|.*?\()
        |(cycle\[.*?\]\()
        |(define\s+\w+:.*?\()
        |(use\s+\w+\(.*?\)\s*;\s*end)
        """
    )
    while pos < len(text):
        m = block_start_pat.search(text, pos)
        if not m:
            output.append(text[pos:])
            break

        output.append(text[pos:m.start()])
        head_raw = m.group(0)
        pos = m.end()

        stack = 1
        end_pos = None
        i = pos

        # 向前扫描，维护栈，找到真正匹配的 );end
        while i < len(text):
            # 遇到新的块开头，栈+1
            sub_m = block_start_pat.match(text, i)
            if sub_m:
                stack += 1
                i = sub_m.end()
                continue
            # 遇到结束标记 );end
            if text.startswith(");end", i):
                stack -= 1
                if stack == 0:
                    end_pos = i
                    break
                i += 5
                continue
            i += 1

        if end_pos is None:
            # 找不到闭合，原样输出原文，保留错误给用户看
            output.append(head_raw)
            output.append(text[pos:])
            break

        body = text[pos:end_pos]
        pos = end_pos + 5

        # --------翻译头部为Python代码--------
        out_head = ""
        # JudgeIf:[cond](
        if head_raw.startswith("JudgeIf:["):
            cond = re.match(r"JudgeIf:\[(.*?)\]\(", head_raw).group(1)
            out_head = f"if {cond}:\n"
        # JudgeElse(
        elif head_raw.startswith("JudgeElse("):
            out_head = "else:\n"
        # loop|var|iterable(
        elif head_raw.startswith("loop|"):
            g = re.match(r"loop\|(.*?)\|(.*?)\(", head_raw)
            v = g.group(1).strip()
            it = g.group(2).strip()
            out_head = f"for {v} in {it}:\n"
        # cycle[cond](
        elif head_raw.startswith("cycle["):
            cond = re.match(r"cycle\[(.*?)\]\(", head_raw).group(1)
            out_head = f"while {cond}:\n"
        # define name:param(
        elif head_raw.startswith("define "):
            g = re.match(r"define (\w+):(.*?)\(", head_raw)
            fname = g.group(1).strip()
            args = g.group(2).strip()
            # 处理 None 无参，规避Python关键字
            if args == "None":
                args = ""
            out_head = f"def {fname}({args}):\n"
        # use xxx(...);end 单行调用
        elif head_raw.startswith("use "):
            g = re.match(r"use (\w+)\((.*?)\)\s*;\s*end", head_raw)
            funcname = g.group(1)
            argpart = g.group(2)
            output.append(f"{funcname}({argpart})")
            continue

        # 给body整体增加一层缩进
        indented_raw = "\n".join("    " + line for line in body.splitlines())
        raw_body = dedent_text(body)
        # 2.递归解析不带用户缩进的干净文本
        parsed_body = parse_blocks(raw_body)

        # 3.解析完成后统一加4空格
        lines = parsed_body.splitlines()
        indented_lines = []
        for ln in lines:
            if ln.strip() == "":
                indented_lines.append("")
            else:
                indented_lines.append("    " + ln)
        indented_body = "\n".join(indented_lines)
        output.append(out_head + indented_body)
    return "".join(output)
def dedent_text(text):
    """移除文本块整体公共前置缩进，把用户手写的空格删掉"""
    lines = text.splitlines()
    # 过滤掉空行，找非空行的最小缩进
    non_blank = [l for l in lines if l.strip()]
    if not non_blank:
        return text
    min_indent = min(len(l) - len(l.lstrip()) for l in non_blank)
    out = []
    for line in lines:
        if line.strip():
            out.append(line[min_indent:])
        else:
            out.append("")
    return "\n".join(out)

def scan_user_raw_code(raw_text):
    # Python原生关键字黑名单
    python_keywords = {
        "None","and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else",
        "except", "finally", "for", "from", "global", "if", "in",
        "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    }
    # Python原生内置函数黑名单，在这里继续追加
    python_builtin_names = {
        "abs","all","any","bin","bool","bytearray","bytes","callable","chr",
        "compile","complex","delattr","dict","dir","divmod","enumerate","eval",
        "exec","filter","float","format","frozenset","getattr","globals","hasattr",
        "hash","help","hex","id","input","int","isinstance","issubclass","iter",
        "len","list","locals","map","max","memoryview","min","next","object","oct",
        "open","ord","pow","print","property","range","repr","reversed","round",
        "set","setattr","slice","sorted","str","sum","super","tuple","type",
        "vars","zip","__import__"
    }

    # 合并两套黑名单
    all_forbidden = python_keywords | python_builtin_names
    pattern = r"\b(" + "|".join(re.escape(w) for w in all_forbidden) + r")\b"

    match = re.search(pattern, raw_text)
    if match:
        bad_word = match.group(1)
    return True
def run_code():
  
   
    if code_box is None:
        return
    src = code_box.get("1.0", tk.END)
    scan_user_raw_code(src)

# 把原始文本赋值给code，后面所有正则操作基于code
    code = src      
    ###########################################################################
    # ✅【核心：你的自定义注释！】自动删除 <...> 内容，不执行、不显示
    ###########################################################################
    code = re.sub(r'<.*?>', '', code, flags=re.DOTALL)
    code = parse_blocks(code)


    code = re.sub(r'define (\w+) = (.+)',r'\1 = \2',code)
    code = re.sub(r'^(\s+)define (\w+) = (.+)',r'\1\2 = \3',code)


    code = re.sub(r'take (\w+)',r'global \1',code)
    code = re.sub(r'^(\s+)take (\w+)',r'\1global \2',code)

    code = re.sub(r'put (\w+)',r'nonlocal \1',code)
    code = re.sub(r'^(\s+)put (\w+)',r'\1nonlocal \2',code)

    code = re.sub(r'(\w+)\>\>(\w+)',r'\1 == \2',code)
    code = re.sub(r'^(\s+)(\w+)\>\>(\w+)',r'\1\2 == \3',code)

    code = re.sub(r'(\w+)\\\\(\w+)',r'\1 != \2',code)
    code = re.sub(r'^(\s+)(\w+)\\\\(\w+)',r'\1\2 != \3',code)
    
    code = re.sub(r'(\w+)\|(\w+)',r'\1 and \2',code)
    code = re.sub(r'^(\s+)(\w+)\|(\w+)',r'\1\2 and \3',code)

    code = re.sub(r'(\w+)\\(\w+)',r'\1 or \2',code)
    code = re.sub(r'^(\s*)(\w+)\\(\w+)',r'\1\2 or \3',code)

    code = re.sub(r'(\w+)\+\|\=(\w+)',r'\1 += \2',code)
    code = re.sub(r'^(\s*)(\w+)\+\|\=(\w+)',r'\1\2 += \3',code)


    code = re.sub(r'\|\|skip\|\|',r'continue',code)
    code = re.sub(r'^(\s+)\|\|skip\|\|',r'\1continue',code)

    code = re.sub(r'\|\|stop\|\|',r'break',code)
    code = re.sub(r'^(\s+)\|\|stop\|\|',r'\1break',code)
 

    
    
    # 预编译
    '''
    
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.config(state=tk.DISABLED)
    _running = True 

    run_env = globals().copy()
    run_env['input'] = IPT
    run_env['print'] = OutPut
    '''
   
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.config(state=tk.DISABLED)

    _running = True

    
    # ========= 这里把 output_box 放进执行环境 =========


    exec_env = {
        "OutPut": OutPut,
        "IPT": IPT,
        "output_box": output_box
        
    }
    
    err_msg = ""
    try:
        exec(code, exec_env)
    except Exception as e:
        err_msg = f"error:{e}"
    
    if err_msg != "":
        output_box.config(state=tk.NORMAL)
        output_box.insert(tk.END, err_msg + "\n")
        output_box.config(state=tk.DISABLED)
    

    _wait_input = False
    _running = False
   
ttk.Button(frame_btn, text="run", width=8, command=run_code).grid(row=0, column=0, padx=3)
def save_file():
    import json
    path = filedialog.asksaveasfilename(
        title="保存FS脚本",
        defaultextension=".fs",
        filetypes=[("FS源文件", "*.fs"), ("所有文件", "*.*")]
    )
    # 用户点取消，path是空字符串，直接返回
    if not path:
        return

    # ✅mac最重要兜底：强制确保后缀是.fs，无视对话框行为
    import os
    base, ext = os.path.splitext(path)
    path = base + ".fs"

    code_text = code_box.get("1.0", "end-1c")
    data = {"source": code_text}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
   
ttk.Button(frame_btn, text="save", width=8, command=save_file).grid(row=0, column=1, padx=3)

from tkinter import filedialog
def open_file_wrapper():
    p = filedialog.askopenfilename(filetypes=[("FS脚本","*.fs")])
    if p:
        open_file(p)
# ========= 你的原有 open_file 函数，原样不动，不要修改 =========
def open_file(filepath):
    with open(filepath,"r",encoding="utf-8") as f:
        data = json.load(f)
    raw_code = data["source"]
    code_box.delete("1.0", tk.END)
    code_box.insert("1.0", raw_code)

ttk.Button(frame_btn, text="open", width=8, command=open_file_wrapper).grid(row=0, column=2, padx=3)


#============================================
# 计算当前行缩进层级
def get_indent_level(line):
    space_num = len(line) - len(line.lstrip(" "))
    return space_num // 4

# 回车：括号结尾自动锁定缩进
def brace_lock_indent(event):
    pos = code_box.index(tk.INSERT)
    line_num = pos.split(".")[0]
    # 获取整行内容
    full_line = code_box.get(f"{line_num}.0", f"{line_num}.end")
    pure_line = full_line.strip()
    now_lv = get_indent_level(full_line)
    # 左括号结尾 → 下一行加缩进
    if pure_line.endswith("("):
        next_lv = now_lv + 1
    # 右括号开头
    elif pure_line.startswith(")") or pure_line == ")":
        next_lv = now_lv - 1
        if next_lv < 0:
            next_lv = 0
    # 普通行保持同级
    else:
        next_lv = now_lv
    # 插入换行 + 对应缩进空格
    code_box.insert(tk.INSERT, "\n" + "    " * next_lv)
    return "break"

# Shift+Tab手动退缩进
def back_indent(event):
    line_num = code_box.index(tk.INSERT).split(".")[0]
    start = f"{line_num}.0"
    end = f"{line_num}.4"
    if code_box.get(start, end) == "    ":
        code_box.delete(start, end)
    return "break"

# Tab按下插入4空格
def tab_insert_4space(event):
    code_box.insert(tk.INSERT, "    ")
    return "break"

# 全部绑定
code_box.bind("<Return>", brace_lock_indent)
code_box.bind("<Shift-Tab>", back_indent)
code_box.bind("<Tab>", tab_insert_4space)





def OutPut(text_arg):
   
    if output_box is None:
        print("【DEBUG】output_box是空！")
        return
    content = str(text_arg)
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, content + "\n")
    output_box.config(state=tk.DISABLED)
    output_box.see(tk.END)
    root.update()

def IPT(prompt=""):
    global _wait_input, _input_buf, root, output_box, _running
    if root is None or output_box is None:
        return ""
    try:
        if not root.winfo_exists():
            return ""
    except tk.TclError:
        return ""
    
    if root is None or output_box is None or not root.winfo_exists():
        return ""

    # 写入提示文本
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, prompt)
    output_box.see(tk.END)
    output_box.focus_set()

    _wait_input = True
    _input_buf = ""

    def on_enter(event):
        
        try:
            _input_buf = output_box.get("insert linestart", "insert").strip()
        except:
            _input_buf = ""
        _wait_input = False
        output_box.unbind("<Return>", on_enter_id)
        output_box.config(state=tk.NORMAL)
        output_box.insert(tk.END, "\n")
        output_box.config(state=tk.DISABLED)
        return "break"

    on_enter_id = output_box.bind("<Return>", on_enter)
    # 不再写while循环！！！
    # 等待事件，tkinter主循环正常跑，红叉随时可以关闭窗口
    root.wait_variable(tk.BooleanVar(value=True))
    return _input_buf

def on_modified(event):
    code_box.edit_modified(False)
    syntax_highlight()

code_box.bind("<<Modified>>", on_modified)
code_box.bind("<<Paste>>", lambda e:syntax_highlight())
code_box.bind("<KeyRelease>", lambda e:syntax_highlight())

# 启动渲染一次
syntax_highlight()



tk.mainloop()

