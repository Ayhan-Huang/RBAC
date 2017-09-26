from django.test import TestCase

# Create your tests here.

all_menu_dict = {
    1: {'id': 1, 'caption': '用户管理', 'parent_id': None, "children": [], "status": False, "open": False},
    2: {'id': 2, 'caption': '订单管理', 'parent_id': None, "children": [], "status": False, "open": False},
    3: {'id': 3, 'caption': '其他', 'parent_id': None, "children": [], "status": False, "open": False},
    4: {'id': 4, 'caption': '退货', 'parent_id': 2, "children": [], "status": True, "open": False},
    5: {'id': 5, 'caption': '换货', 'parent_id': 2, "children": [], "status": False, "open": False}
}

permisson_url = [
    {'title': '权限1', 'url': '/test/', 'menu_id': 1},
    {'title': '权限2', 'url': '/test/', 'menu_id': 1},
    {'title': '权限3', 'url': '/login', 'menu_id': 4},
    {'title': '权限4', 'url': '/test/', 'menu_id': 5}
]

request_rul = '/login'
import re

for url in permisson_url:
    # 添加两个状态：显示 和 展开
    url['status'] = True
    pattern = url['url']
    if re.match(pattern, request_rul):
        url['open'] = True
    else:
        url['open'] = False

    # 将url添加到菜单下
    all_menu_dict[url['menu_id']]["children"].append(url)

    # 显示菜单：url 的菜单及上层菜单 status: true
    pid = url['menu_id']
    while pid:
        all_menu_dict[pid]['status'] = True
        pid = all_menu_dict[pid]['parent_id']

    # 展开url上层菜单：url['open'] = True, 其菜单及其父菜单open = True
    if url['open']:
        ppid = url['menu_id']
        while ppid:
            all_menu_dict[ppid]['open'] = True
            ppid = all_menu_dict[ppid]['parent_id']





print(all_menu_dict)
    
    