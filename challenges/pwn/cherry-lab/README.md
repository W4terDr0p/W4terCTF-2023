# Cherry Lab

**Author:** Xia0o0o0o

**Difficulty:** Hard

**Category:** Pwn

## 题目描述

Scientific computation with JavaScript, the future of scientific computing. Try it with CherryLab now!

## 题目解析

**暴露端口：`70`**

简单观察 patch 就能找到引入的问题

```diff
diff --git a/jerry-core/ecma/operations/ecma-dataview-object.c b/jerry-core/ecma/operations/ecma-dataview-object.c
index db2ae0a6..21591e85 100644
--- a/jerry-core/ecma/operations/ecma-dataview-object.c
+++ b/jerry-core/ecma/operations/ecma-dataview-object.c
@@ -321,7 +321,7 @@ ecma_op_dataview_get_set_view_value (ecma_value_t view, /**< the operation's 'vi
   uint8_t element_size = (uint8_t) (1 << (ecma_typedarray_helper_get_shift_size (id)));

   /* GetViewValue 10., SetViewValue 12. */
-  if (get_index + element_size > (ecma_number_t) view_size)
+  if (get_index >= (ecma_number_t) view_size * element_size)
   {
     ecma_free_value (value_to_set);
     return ecma_raise_range_error (ECMA_ERR_START_OFFSET_IS_OUTSIDE_THE_BOUNDS_OF_THE_BUFFER);
```

`DataView` 的 `get` 和 `set` 方法在读取和写入时都会调用 `ecma_op_dataview_get_set_view_value`，这个函数会检查读取或写入的字节数是否超出了 `DataView` 的大小，但是这里的判断条件有问题，应该采用 byte offset 来判断位置，但是实际上使用了 element offset 导致可以读取或写入超出 `DataView` 的大小的数据。利用这个问题可以实现越界读写。
