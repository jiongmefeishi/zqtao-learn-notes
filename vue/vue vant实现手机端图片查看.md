# vue vant实现手机端图片查看

需求：实现手机端点击查看图片，再次点击关闭图片。



点击查看，出发查看图片事件。

![1590991341199](C:\Users\tao\AppData\Roaming\Typora\typora-user-images\1590991341199.png)



标签样式

```
<b class="opt" @click="imgView(testUrl)">查看</b>
<img src="" hidden alt="">
```

vue 事件方法

首先需要在标签所在的vue页面中导入 `ImagePreview` 模块

```
 import {ImagePreview} from 'vant';
```



具体实现

```
<script>

  import {ImagePreview} from 'vant';

  export default {
    name: "progress",
    data() {
      return {
      	// 需要显示的图片路径
        testUrl: "https://img.yzcdn.cn/vant/apple-2.jpg",
      }
    },

    methods: {
    
      // 查看图片，imgPath 图片路径
      imgView(imgPath) {
        var flist = [] // 因为images 是一个集合，所以将要显示的图片存放进集合中
        flist.push(imgPath)
        ImagePreview({
          images: flist,
          showIndex: true,
          loop: false,
          startPosition: 0
        })
      },
      
      
      
    }
  }
</script>
```

效果，点击查看

![1590991763614](C:\Users\tao\AppData\Roaming\Typora\typora-user-images\1590991763614.png)