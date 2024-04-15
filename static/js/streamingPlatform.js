$button = $("#loginButton");
$button.click(function () {
    let username = $("#Username").val();
    let password = $("#Password").val();
    console.log(username, password);
    $.ajax({
        url: "/api/Signin",
        type: "GET",
        data: {
            "username": username,
            "password": password,
        },
        success: resp => {
            let res = resp['data'];
            console.log(res);
        },
        error: () => {

        },
    });
});