#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试Python 3.11兼容性
"""

import sys

def test_imports():
    """测试所有必需的导入"""
    print(f"Python版本: {sys.version}")
    print(f"Python版本信息: {sys.version_info}")
    
    try:
        # 测试标准库导入
        from os import scandir
        print("✓ os.scandir 导入成功")
        
        # 测试click
        import click
        print(f"✓ click {click.__version__} 导入成功")
        
        # 测试docx
        from docx import Document
        print("✓ python-docx 导入成功")
        
        # 测试importlib.resources
        if sys.version_info >= (3, 9):
            from importlib.resources import files
            print("✓ importlib.resources.files 导入成功 (Python 3.9+)")
        else:
            from importlib.resources import path
            print("✓ importlib.resources.path 导入成功 (Python 3.7-3.8)")
        
        # 测试主模块
        from sccg.sccg import CodeFinder, CodeWriter, main
        print("✓ sccg模块导入成功")
        
        print("\n所有导入测试通过！")
        return True
        
    except ImportError as e:
        print(f"\n✗ 导入失败: {e}")
        return False

if __name__ == '__main__':
    success = test_imports()
    sys.exit(0 if success else 1)
