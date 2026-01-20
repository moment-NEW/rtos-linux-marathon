# 马拉松项目路线与检查清单
> 从 RTOS 驱动 → RTOS tickless/功耗 → Linux 字符驱动 → 内核小特性/修复。

## 里程碑与检查项
- M1：RTOS 环境跑通
  - [-] STM32 + RTOS 基本示例运行
  - [-] QEMU + initramfs Linux 启动
- M2：RTOS 新外设驱动 PR
  - [ ] 选定设备（I2C/SPI）
  - [ ] 驱动实现与示例任务
  - [ ] CI 通过 & PR 提交
- M3：RTOS tickless/功耗优化
  - [ ] 启用/改进 tickless
  - [ ] 延迟/功耗对比数据
  - [ ] PR/文档提交
- M4：Linux 字符驱动 + tracepoint
  - [ ] QEMU 环境 + 自编内核
  - [ ] 字符驱动 (open/read/write/ioctl)
  - [ ] tracepoint 可被 perf/bpftrace 观测
- M5：调度/内存/同步相关小改
  - [ ] 选择子系统（sched/mm/locking/trace）
  - [ ] 补丁（统计/tracepoint/文档/健壮性）
  - [ ] 工具验证（checkpatch/lockdep/KASAN 等）
- M6：社区可合入补丁
  - [ ] 选定真实问题或 syzbot/文档任务
  - [ ] 邮件列表流程（cover letter, v1/v2）
  - [ ] 获得 Ack/Reviewed-by（尽力而为）

## 观测与验证
- 必备：checkpatch/sparse/smatch/clang -Wall -Wextra -Werror；ftrace/perf/bpftrace 一次观测；git bisect 一次定位
- 性能/功耗：RTOS tickless 前后数据；Linux 侧一次性能或延迟小结

## 文档与输出
- [ ] 周报（logs/weekly-log-YYYY-WW.md）
- [ ] 月/季总结（logs 目录追加）
- [ ] 关键实验/数据附 PR 或独立 md

## 当前进度（W1 2026-01-20）
- 已完成：Linux源码下载与编译（bzImage生成）、Busybox编译学习。
- 进行中：RT-Thread STM32H723VGTx BSP开发（时钟树配置，准备SPI/BMI088驱动）。
- 里程碑进展：M1 RTOS环境（STM32 BSP进行中）、M4 Linux字符驱动（QEMU环境准备中）。