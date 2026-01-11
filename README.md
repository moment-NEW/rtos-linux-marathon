# RTOS & Linux Kernel Marathon
为期 365 天的系统学习 + 实战马拉松，目标：能够维护开源 RTOS、修改 Linux 内核并向社区提交可合入的补丁。

## 仓库结构
- docs/plan-365d.md：全年学习与实战计划（按月/季度/里程碑）
- docs/projects/marathon-roadmap.md：马拉松项目路线图与检查清单
- docs/logs/：周报与月报模板
- docs/context/context-journal.md：上下文记忆文档（每次汇报后更新）
- LICENSE：MIT 许可证

## 使用方式
1. 每周/周期复制 docs/logs/weekly-log-YYYY-WW.md 模板填写。
2. 关键输出更新到 roadmap 和 context-journal。
3. 需要我回顾上下文时，用 context-journal。
---
本仓库默认分支：main。
EOF

cat > docs/plan-365d.md <<'EOF'
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
EOF

cat > docs/logs/weekly-log-YYYY-WW.md <<'EOF'
# 周报模板（替换 YYYY-WW）

- 周次：YYYY-WW
- 时间范围：YYYY-MM-DD ~ YYYY-MM-DD
- 本周重点（3+1 模式中的本周定位）：
- 本周完成：
  - 代码/补丁/PR：
  - 实验/数据：
  - 阅读/学习：
- 遇到的问题 & 解决进展：
- 下周计划：
- 需要协助/决策：
- 备注（链接/日志/截图）：
EOF

cat > docs/context/context-journal.md <<'EOF'
# 上下文记忆文档
> 用于我在你每次汇报后记录上下文，便于连续对话与指导。

## 最新上下文（由助手更新）
- 日期：
- 周期/周次：
- 近期工作摘要：
- 最新产出（PR/补丁/实验）：
- 未决问题/阻塞：
- 下一步计划：

## 历史记录（由助手追加，倒序）
- YYYY-MM-DD 周次：摘要 / 产出 / 问题 / 下一步
EOF

cat > docs/projects/marathon-roadmap.md <<'EOF'
# 马拉松项目路线与检查清单
> 从 RTOS 驱动 → RTOS tickless/功耗 → Linux 字符驱动 → 内核小特性/修复。

## 里程碑与检查项
- M1：RTOS 环境跑通
  - [ ] STM32 + RTOS 基本示例运行
  - [ ] QEMU + initramfs Linux 启动
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