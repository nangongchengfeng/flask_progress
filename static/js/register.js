function validateEmail() {
    var email = document.getElementById("email").value;
    var error = document.getElementById("error");

    // 正则表达式验证邮件地址是否符合标准
    var emailRegex = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/
    if (!emailRegex.test(email)) {
        error.innerHTML = "请输入有效的邮件地址";
        return false;
    }

    // 验证邮件地址是否为空
    if (email == "") {
        error.innerHTML = "邮件地址不能为空";
        return false;
    }

    // 验证通过，清空错误提示信息
    error.innerHTML = "";
    return true;
}


function bindEmailCaptchaClick() {
    $("#captcha-btn").click(function (event) {
        // $this：代表的是当前按钮的jquery对象
        var $this = $(this);
        // 阻止默认的事件
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            // http://127.0.0.1:500
            // /auth/captcha/email?email=xx@qq.com
            url: "/auth/captcha/email?email=" + email,
            method: "GET",
            success: function (result) {
                var code = result['code'];
                if (code == 200) {
                    var countdown = 60;
                    // 开始倒计时之前，就取消按钮的点击事件
                    $this.off("click");
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        // 倒计时结束的时候执行
                        if (countdown <= 0) {
                            // 清掉定时器
                            clearInterval(timer);
                            // 将按钮的文字重新修改回来
                            $this.text("获取验证码");
                            // 重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    // alert("邮箱验证码发送成功！");
                } else {
                    alert(result['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
}


// 整个网页都加载完毕后再执行的
$(function () {

    bindEmailCaptchaClick();
});