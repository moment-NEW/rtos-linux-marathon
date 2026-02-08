# 365 天学习与实战计划
> 目标：一年内完成从 RTOS 驱动到 Linux 内核小特性/修复的连续产物链，能向社区提交可合入的补丁。

## 季度目标
- Q1（M1-M3）：RTOS 基础与驱动；完成 1 个新外设驱动 PR。
- Q2（M4-M6）：RTOS tickless/功耗；完成 1 个 tickless/功耗优化 PR；启动 Linux 内核构建与最小字符驱动。
- Q3（M7-M9）：同步/调度/内存；提交调度或 mm 相关的小补丁（统计/tracepoint/文档/边界检查）。
- Q4 (M10-M12)：观测/性能/安全/社区投稿；完成一次社区可合入补丁并力争 Ack/Reviewed-by。

## 月度概览（细化版）
> 在原有时间线上进行 Lab 任务填充，针对无硬件期柔性调整。

- **M1：环境与工具**（git/交叉编译/QEMU）
  - *Lab 1 (进行中)*：BSP 基础设施 - 解决 SConscript 自动拉取、H7 时钟树与 AXI SRAM 存储布局配置。
- **M2：RTOS 调度与 Linux 基础**（**补强期**）
  - RTOS：读上下文切换代码，测量 `PendSV` 延迟。
  - *Lab 4 (Windows 用户必修)*：Linux 系统的“五脏六腑” - 练习手动挂载磁盘镜像、Systemd 服务管理，用 `strace` 追踪系统调用，理解“一切皆文件”。
- **M3：RTOS 驱动开发**
  - *Lab 2*：完成一个 SPI/I2C 传感器驱动（如 BMI088），提交 RT-Thread 官方 PR 并处理 review。
- **M4：RTOS 功耗优化与 Linux 启动**
  - RTOS：实现 tickless 机制。
  - Linux：QEMU 启动自编内核，手动配置 initramfs。
- **M5：Linux 内核模块 (LKM) 基础**
  - *Lab 5*：编写 `/proc` 或 `/sys` 接口模块，实现内核与用户态通信，理解 `file_operations`。
- **M6：Linux 字符驱动与观测**
  - *Lab 6*：编写一个具备 `read/write/ioctl` 的字符驱动，并使用 `ftrace/perf` 观测其执行耗时。
- **M7：锁与同步**
  - 在字符驱动中引入并发，实验 `mutex/spinlock` 的竞争情况，增加调试 tracepoint。
- **M8：调度子系统研究**
  - 增加调度统计统计/阈值，通过 `debugfs` 输出。
- **M9：内存管理与健壮性**
  - 实验伙伴系统/slab 逻辑，使用 KASAN/Kmemleak 定位伪造的内存泄露。
- **M10：性能优化实战**
  - 使用 `bpftrace` 编写内核探测脚本，完成一份 QEMU 环境下的 IO/调度性能小结。
- **M11：安全与防护补丁**
  - 研究 `refcount` 或边界检查，尝试提交一个内核文档或代码风格修复补丁。
- **M12：社区投稿与综合复盘**
  - 选定真实问题（如 syzbot 汇报），尝试提交并进入邮件列表流程。

## 关键路径（给 Windows 用户的 Linux 学习建议）
1. **环境**：Windows 宿主机 + WSL2 (日常开发) + QEMU (内核实验)。尽量用 VS Code Remote 连接 QEMU 里的 Linux 系统。
2. **心智模型**：从“一切皆对象/API (Windows)”转向“一切皆文件 (Linux)”。
3. **重点学习**：
    - **VFS (虚拟文件系统)**：明白为什么 `cat /proc/cpuinfo` 能看到硬件信息。
    - **Process Management**：明白 `fork()` 和 `exec()` 与 Windows 创建进程的区别。
    - **Memory Mapping**：理解 `mmap` 与物理内存的映射关系。

## 里程碑
1) M1：RTOS 环境跑通；最小 Demo
2) M2：RTOS 新外设驱动 PR
3) M3：RTOS tickless/功耗优化 PR + 数据
4) M4-M6：Linux 字符驱动 + tracepoint，QEMU 验证
5) M7-M9：调度/内存小改或文档/健壮性补丁
6) M10-M12：社区可合入补丁，争取 Ack/Reviewed-by

## 周节奏（3+1）
- 周1：读代码/文档 + 最小实验
- 周2：实现/修改 + 自测
- 周3：清理 + 工具检查 + 补丁/PR
- 周4：复盘与文档，回应 review

## 量化指标
- 6 大里程碑完成；社区提交 ≥3（RTOS ≥2，Linux ≥1），力争 ≥1 Ack/Reviewed-by
- 月度笔记 ≥12，季度总结 ≥4
- 能用 ftrace/perf/bpftrace 定位一次延迟/bug；能用 git bisect 定位一次回归