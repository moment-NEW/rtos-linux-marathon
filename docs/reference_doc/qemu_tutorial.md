# QEMU 入门与使用指南

本文件为学习者提供一个简明的 QEMU 使用教程，适合做操作系统开发、引导扇区实验以及嵌入式系统模拟。

---

## 1. 什么是 QEMU

QEMU 是一个开源的机器模拟器和虚拟化工具，能够模拟多种 CPU 架构和外设。它可以将一个操作系统或程序运行在虚拟硬件上，而不需要真实设备。

## 2. 安装

- **Windows**：
  - 下载官方二进制： https://qemu.weilnetz.de/ 
  - 或使用 MSYS2/Chocolatey：
    ```powershell
    choco install qemu
    ```
- **Linux**（Debian/Ubuntu）：
  ```bash
  sudo apt install qemu-system-x86
  ```
- **macOS**（Homebrew）：
  ```bash
  brew install qemu
  ```

## 3. 常用命令结构

```bash
qemu-system-<arch> [options]
```

其中 `<arch>` 常见的有 `i386`、`x86_64`、`arm`, `aarch64` 等。

主要设备选项：
- `-fda <file>`   : 指定软盘映像
- `-hda <file>`   : 指定硬盘映像
- `-cdrom <file>` : 指定光盘映像
- `-m <size>`     : 设置内存大小，例如 `-m 512`
- `-serial stdio` : 将串口输出重定向到当前终端
- `-net nic -net user` : 启用用户态网络
- `-S -gdb tcp::1234` : 启动时等待 GDB 连接

更多参数参考官方文档： https://www.qemu.org/docs/ .

## 4. 第一个实验：启动一个软盘映像

1. 编写简单的引导代码并生成二进制：
   ```bash
   echo -e "BITS 16\norg 0x7c00\nmov ah,0x0e\nmov al,'A'\nint 0x10\nhlt\ntimes 510-($-$$) db 0\nDW 0xAA55" > boot.asm
   nasm -f bin boot.asm -o boot.bin
   ```
2. 创建软盘映像并写入引导扇区：
   ```bash
   dd if=boot.bin of=floppy.img bs=512 count=1 conv=notrunc
   ```
3. 用 QEMU 启动：
   ```bash
   qemu-system-i386 -fda floppy.img -serial stdio
   ```
   如果屏幕出现字母 `A`，说明引导扇区成功运行。

## 5. 示例：编译并运行李治军课程的 bootsect

1. 获取课程的实验代码模板，通常包含 `bootsect.S`、`Makefile` 等。
2. 编译：
   ```bash
   nasm -f bin bootsect.S -o bootsect.bin
   dd if=bootsect.bin of=floppy.img bs=512 count=1 conv=notrunc
   qemu-system-i386 -fda floppy.img -serial stdio
   ```
3. 修改 `bootsect.S`，观察启动行为变化。

## 6. 调试技巧

- **串口输出**：使用 `-serial stdio` 或 `-serial file:/path/log.txt`。
- **GDB 远程调试**：
  ```bash
  qemu-system-i386 -fda floppy.img -S -gdb tcp::1234
  # 然后在另一个终端
  gdb -ex "target remote :1234" /path/to/binary
  ```
- **快照与镜像**：
  ```bash
  qemu-img create -f qcow2 disk.qcow2 10M
  qemu-system-i386 -hda disk.qcow2 -snapshot
  ```

## 7. 进阶功能

- 模拟多核：`-smp 2`。
- 指定 CPU 型号：`-cpu qemu64`、`-cpu host`。
- 添加设备：`-device e1000`、`-device usb-mouse`。
- 使用 PCI 热插拔等。

## 8. 参考资料

- 官方文档：https://www.qemu.org/docs/
- 中文教程：搜索 “QEMU 简明教程”、“QEMU 入门” 等
- 项目实战：xv6、OS/161、bootsector.io 等开源教学操作系统

---

> 这份说明可作为仓库中 `reference_doc` 的快速参考，方便查阅 QEMU 使用方法。欢迎补充更新内容。