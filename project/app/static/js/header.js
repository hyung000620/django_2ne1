document.addEventListener("DOMContentLoaded", function () {
    // Login 버튼 클릭 시
    document.getElementById("login_button").addEventListener("click", function () {
        window.location.href = "{% url 'login' %}";
    });

    // Just Write 버튼 클릭 시
    document.getElementById("write_button").addEventListener("click", function () {
        window.location.href = "{% url 'write' %}";
    });
});