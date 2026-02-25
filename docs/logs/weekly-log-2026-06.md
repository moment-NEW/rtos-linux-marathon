
- 周次：W5
- 时间范围：2026-2-18 ~ 2026-2-25
- 本周重点（3+1 模式中的本周定位）：
- 本周完成：
  - 代码/补丁/PR：无
  - 实验/数据：无
  - 阅读/学习：哈工大李治军操作系统

- 遇到的问题 & 解决进展：主要集中在后几天，因此略过D1,D2.D3  
D4:开始看哈工大操作系统课程的bootsect部分。  
D5:收尾看完了哈工大操作系统课程的操作系统bootsect部分。  
D6:收尾看完了setup部分，开始看起操作系统启动。 过程笔记详见我的博客。 
D7:今天延续完成了昨天未能正常编译运行的bootsect.bin，发现了问题是：
使用gcc/as编译为.o后进行ld链接，这个流程本身没有问题，但是因为产生的是elf文件，其存在elf头等数据，并不是真的512字节的引导扇区。而QEMU的指令只会读取512扇区，因此读到了不完整不正常的指令。（RaptorMini真好用吧）所以应该使用`objcopy -O binary bootsect.tmp bootsect.bin`指令完成清理，再`qemu-system-i386 -fda bootsect.bin`运行。然后，继续看哈工大的教程。
- 下周计划：从下周开始恢复记录和实际工作
- 需要协助/决策：暂无
- 备注（链接/日志/截图）：  
【【哈工大】操作系统 李治军（全32讲）】 https://www.bilibili.com/video/BV19r4y1b7Aw/?p=3&share_source=copy_web&vd_source=8b034ca64cb8bbbd15b0969aebfe1501
C/C++内嵌汇编，AT&T汇编语法
https://blog.csdn.net/linweieran/article/details/102719005


在我们这类 boot‑sector 场景中用到的那条命令：


objcopy -R .pdr -R .comment -R .note -S -O binary bootsect.tmp bootsect.bin
大致做了下面几件事：

-O binary
把输入文件从 ELF（有头、节表、符号表、重定位记录）转成“纯二进制流”。
结果文件中没有任何元数据，只有程序代码/数据按它的装载地址顺序排列。

-R <section>
删除指定的节。我们去掉 .pdr、.comment、.note 这类只包含调试信息
或编译器注释的节，减少输出体积。

-S / --strip-all
丢弃所有符号表、重定位信息等调试符号，即便是 .symtab、.strtab 也全
被扔掉。

自动 pad/truncate 到合适长度
当输出格式是 binary 时，objcopy 会把所有节按其 链接地址 放好，
然后用零字节填充相邻地址间的空隙，最后把文件长度截断到最高地址。
如果你链接时用了 -Ttext 0 并在源里确保在 510 处有 dw 0xaa55 加上
times 510-($-$$) db 0，那么输出自然就是恰好 512 字节，末尾有那个启动签名。