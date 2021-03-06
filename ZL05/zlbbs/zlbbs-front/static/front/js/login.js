var LoginHadler = function () {

}
LoginHadler.prototype.listenSubmitEvent = function () {
    $('#submit-btn').on('click', function (event) {
        event.preventDefault()
        var email = $("input[name='email']").val()
        var password = $("input[name='password']").val()
        var remember = $("input[name='remember']").prop('checked')
        zlajax.post({
            url:'/login',
            data:{
                email,
                password,
                remember: remember ? 1 : 0
            },
            success: function (result) {
                if(result['code'] == 200)
                {
                    window.location = '/'
                }
                else
                {
                    alert(result['message'])
                }
            }
        })
    })
}
LoginHadler.prototype.run = function () {
    this.listenSubmitEvent()
}

$(function(){
    var handler = new LoginHadler();
    handler.run()
})