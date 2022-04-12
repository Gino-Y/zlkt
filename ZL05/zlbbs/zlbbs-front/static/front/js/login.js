var LoginHadler = function () {

}
LoginHadler.prototype.listenSubmitEvent = function () {
    $('#submit-btn').on('click', function (event) {
        event.preventDefault()
        var email = $("input[name='email']").val()
        var password = $("input[name='password']").val()
        var remember = $("input[name='remember']").prop('checked')
        console.log(email, password, remember)
    })
}
LoginHadler.prototype.run = function () {

}

$(function(){
    var handler = new LoginHadler();
    handler.run()
})