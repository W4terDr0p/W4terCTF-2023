# W4ter Disk

**Author:** GZTime

**Difficulty:** Medium

**Category:** Misc

## 题目描述

2023 年 3 月 31 日半夜，暴雨。

GZTime 发现已经跑了一整天的 python 脚本挂了，满眼所见皆为 IO Error。

「坏了！我还得靠这玩意交作业！」他想，之后赶忙去检查了一下硬盘的情况——看起来数据都正常，只是大概由于暴雨的缘故（bushi）关于 RAID 的元信息全不见了——

而 GZTime 也忘记了当初组 RAID 的时候的各项参数……一番搜索，恢复数据似乎得花不少钱，但是他听说这里似乎在做什么安全相关的东西——或许你能帮上忙？

## 题目解析

attachment: [w4ter-disk.7z](https://nas.gzti.me/Misc/Assets/w4ter-disk.7z)

一道 RAID 恢复题，给出了一个 128MB 的硬盘镜像，要求恢复出原始的数据。

由于借鉴 hackergame，此处不再赘述 RAID 0 的恢复过程，而说一些恢复 RAID 后可能会踩的坑（设计）……

1. `sudo losetup -fP ./disk.img` 强制扫描并加载分区，这样才能看到 `/dev/loop0p1` 这样的分区设备
2. `sudo mount /dev/loop0p1 /mnt` 将分区挂载到 `/mnt` 下，但是这里设置了 btrfs 的默认子卷，所以要加上 `-o subvol=@data` 参数和 `-o subvol=@secret` 参数才能正常提取题目所需的数据
