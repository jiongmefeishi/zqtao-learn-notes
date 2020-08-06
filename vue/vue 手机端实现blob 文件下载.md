# vue 手机端实现blob 文件下载

需求：实现点击，请求下载后端返回的文件

![1590992480322](C:\Users\tao\AppData\Roaming\Typora\typora-user-images\1590992480322.png)

标签书写

```
<a class="opt"
	@click="downFile(f.path,f.FILE_NAME)"
>下载</a>
```

注意：其中path 表示文件地址（注意，这是后端给你规定的地址，如下，后端返回的路径）,不是下载路径，不需要自己进行下载。

![1590992607341](C:\Users\tao\AppData\Roaming\Typora\typora-user-images\1590992607341.png)

具体实现

```
<script>

  export default {
    name: "progress",
    data() {
      return {

      }
    },


    methods: {
      // 文件下载
      downFile(fPath, fName) {
        console.log(fPath)
        // 获取原来信息
        let that = this
        $.ajax({
          url: '/tonglu_secondphase/upload/downloadfile', /*接口域名地址*/
          type: 'get',
          data: {
            path: fPath,
            fileName: fName
          },
          responseType: 'blob',// 表明返回服务器返回的数据类型
          success: function (res) {
            console.log(res)
            const data = res // 这里填内容的字符串
            const blob = new Blob([data], {type: "text/plain"})
            const link = document.createElement("a")
            link.href = URL.createObjectURL(blob)
            link.download = fName // 这里填保存成的文件名
            link.click()
            URL.revokeObjectURL(link.href)
          }
        })
      },

      

    }
  }
</script>
```

适用于后台返回的是纯文本

![1590992956519](C:\Users\tao\AppData\Roaming\Typora\typora-user-images\1590992956519.png)