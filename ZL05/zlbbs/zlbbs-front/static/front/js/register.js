var RegisterHandler = function () {
    
}

RegisterHandler.prototype.listenSendCaptchaEvent = function () {
    var callback = function (event) {
        // 原生的JS对象：this => jQuery对象
        var $this = $(this);
        // 阻止默认的点击事件
        event.preventDefault();
        var email = $("input[name='email']").val();
        var reg = /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/;
        if(!email || !reg.test(email))
        {
            alert('请输入正确的邮箱！');
            return;
        }
        zlajax.get({
            url: '/email/captcha?email=' + email,
            success: function (result) {
                if(result['code'] == 200)
                {
                    console.log('邮件发送成功！')
                    // 取消按钮的点击事件
                    $this.off('click')
                    // 添加禁用状态
                    $this.attr('disable', 'disable')
                    // 开始倒计时
                    var countdown = 5;
                    var interval = setInterval(function () {
                        if(countdown > 0)
                        {
                            $this.text(countdown)
                        }
                        else
                        {
                            $this.text('发送验证码')
                            $this.attr('disabled', false)
                            $this.on('click', callback)
                            // 清理定时器
                            clearInterval(interval)
                        }
                        countdown--;
                    }, 1000)
                }else{
                    var message = result['message']
                    alert(message)
                }
            }
        })
    }
    $('#email-captcha-btn').on('click', callback)
}

RegisterHandler.prototype.listenGraphCaptchaEvent = function () {
    $('#captcha-img').on('click', function () {
        console.log('dianji')
        var $this = $(this);
        var src = $this.attr('src');
        // 防止在 两次url相同的情况下， 不会重新发送请求，导致图形验证码不会更新
        let new_src = zlparam.setParam(src, 'sign', Math.random())
        $.attr('src', new_src);
    })
}

RegisterHandler.prototype.run = function () {
    this.listenSendCaptchaEvent();
    this.listenGraphCaptchaEvent();
}

// JQuery(function () {})
$(function () {
    var handler = new RegisterHandler();
    handler.run();
})
