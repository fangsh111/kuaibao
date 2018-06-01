$.getJSON('/'
                , function(data) {                    // 从Flask返回的数据
                    alert(data.url)                   // 浏览器弹窗显示 后端返回的dict["a"]的值，此次是1
            }
          )
);