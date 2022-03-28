var RegisterHandler = function () {
    
}

RegisterHandler.prototype.listenSendCaptchaEvent = function () {
    $('#email-captcha-btn').on('click', function (event) {
        // 原生的JS对象：this => jQuery对象
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
                }else{
                    var message = result['message']
                    alert(message)
                }
            }
        })
    })
}

RegisterHandler.prototype.run = function () {
    this.listenSendCaptchaEvent();
}

// JQuery(function () {})
$(function () {
    var handler = new RegisterHandler();
    handler.run();
})
