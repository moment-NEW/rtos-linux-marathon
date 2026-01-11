# 365 天学习与实战计划
> 目标：一年内完成从 RTOS 驱动到 Linux 内核小特性/修复的连续产物链，能向社区提交可合入的补丁。

## 季度目标
- Q1（M1-M3）：RTOS 基础与驱动；完成 1 个新外设驱动 PR。
- Q2（M4-M6）：RTOS tickless/功耗；完成 1 个 tickless/功耗优化 PR；启动 Linux 内核构建与最小字符驱动。
- Q3（M7-M9）：同步/调度/内存；提交调度或 mm 相关的小补丁（统计/tracepoint/文档/边界检查）。
- Q4 (M10-M12)：观测/性能/安全/社区投稿；完成一次社区可合入补丁并力争 Ack/Reviewed-by。

## 月度概览（精简版）
- M1：环境与工具（git bisect/format-patch/send-email，交叉编译，QEMU+initramfs，STM32 RTOS demo）
- M2：RTOS 调度/中断/延迟测量，读上下文切换代码
- M3：RTOS 驱动开发（I2C/SPI 传感器或 Flash），提交 PR
- M4：RTOS tickless/功耗优化，延迟/功耗对比，提交 PR/报告
- M5：Linux 构建与最小补丁（文档/拼写），QEMU 启动自编内核
- M6：Linux 字符驱动 + tracepoint，QEMU 验证
- M7：锁与同步（spin/mutex/RCU/atomic），增加统计或调试 tracepoint
- M8：调度/实时（CFS/RT），增加统计/阈值或 tracepoint
- M9：内存管理（伙伴/slab/缺页），KASAN/Kmemleak 实验，小补丁
- M10：观测与性能（ftrace/perf/bpftrace），脚本合集 + 性能小结
- M11：安全与健壮性（refcount/边界检查/KASAN/KCSAN），修复或防护补丁
- M12：社区投稿与综合（syzbot/真实问题），完成可合入补丁并复盘

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