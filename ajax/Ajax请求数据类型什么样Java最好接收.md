# Ajax请求数据类型什么样Java最好接收

## 1.发送的数据对应后台的实体类

后台存在实体类 `Armin`

```java
/**
 * 管理员实体
 */
public class Admin {
    private Integer id;
    private String password;
    private String userName;
    private String email;
}
```



```
var id = 1;
var username = "pc";
var password = "123";
var email = "4533@qq.com";
```

Ajax请求数据格式

第一种，直接写在data{}

```
$.ajax({
    "url": "admin/save.json",
    "type": "post",
    "data": {
        "id": id,
        "username": username,
        "password": password,
        "email": email,
    },
    "dataType": "json",
    "success": function (res) {},
    "error": function (res) {}
});
```

第二种，提前封装成对象, 其实是一样的

```
var admin = {
    "id": id,
    "username": username,
    "password": password,
    "email": email
}

$.ajax({
    "url": "role/save.json",
    "type": "post",
    "data": admin,
    "dataType": "json",
    "success": function (res) {},
    "error": function (res) {}
});
```

此时java接收数据方式，直接参数中对应实体类

```
saveAdmin(Admin admin){}
```

## 2.发送的数据没有对应实体类，且不存在数组

例如：根据id删除一条数据，这个时候后台不需要使用整个实体类来接收，浪费内存。

```
$.ajax({
    "url": "admin/remove.json",
    "type": "post",
    "data": {
        "id": 2,
    },
    "dataType": "json",
    "success": function (res) {},
    "error": function (res) {}
});
```

java接收使用@RequestParam() 注解

```
removeAdmin(@RequestParam("id") Integer id)
```

## 3.发送的数据是一个数组

如果发送的数据是一个**数组**，后端也没有准备响应的接收实体，为了方便接收，将数据转为JSON字符串，再进行发送,

同时在Ajax请求中**需要指定字符集**

```
var adminIdList = [1,2,3,4]

// 将数组转为JSON字符串
var requestBody = JSON.stringify(adminIdList)
```

Ajax发送格式

```
$.ajax({
    "url": "admin/remove/array.json",
    "type": "post",
    // 数组形式，后端也没有准备响应的接收实体，那么就采用JSON字符串形式传递
    // 同样，后端也需要使用@RequestBody List<Integer> roleIdList 进行接收
    "data": requestBody,
    "dataType": "json",
    // 传入的是JSON 字符串，需要指定字符集
    "contentType": "application/json;charset=UTF-8",
    "success": function (res) { },
    "error": function (res) { }
});
```

java接收使用 @RequestBody 注解 进行标注

```
removeByAdminIdArray(@RequestBody List<Integer> adminIdList)
```

## 4.发送的数据既有数组又有单个字段

发送的数据既有数组又有单个字段，方法类似第三种情况，这里采用所有属性数组化，把不是数组的单个属性看做是数组

```
var adminIdList = [1,2,3,4]
var authId = 2

// 都转化为数组
var requestBody = {
	"adminIdList": adminIdList,
	"authId":[authId]
}

// 将数组转为JSON字符串
var requestBody = JSON.stringify(adminIdList)
```

为了服务器端handler方法能够统一使用List<Integer>方式接收数据，authId也存入数组

后端使用 **Map<String, List<Integer>>** 就可以轻松接收数据

```
method(@RequestBody Map<String, List<Integer>> map);
```

